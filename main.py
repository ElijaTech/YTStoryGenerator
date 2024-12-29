from langchain_ollama import OllamaLLM
from gtts import gTTS
import os
from moviepy import VideoFileClip, AudioFileClip
import google.auth
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
model = OllamaLLM(model="llama3.2")
result = model.invoke(input="You are tasked with creating videos for Youtube that can be converted using text to speech and need no oversight on my part. The topics you can make a video about is Guess The Country(For guess the country, the format is you give 5 clues about the country that you chose at random and the viewer has to guess it. Ensure to tell the viewer to comment if they got it. And do not forget to reveal the country at the end and not before you have given all the clues.). You only choose one of these topics to do each time you are run so do not do two topics at once. You do not talk about the task you just make the script for my text to speech ai to read. Do not ask me if you have done a good job or ask me to follow up. Also, do not include things like **Intro:**, just say what you want read. Do one topic per video you create. Ensure to make no geographical errors. Also, do not state that it is a script just write what you want read.")
print(result)

mytext = result
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("output.mp3")

video = VideoFileClip("input.mp4")
audio = AudioFileClip("output.mp3")
video_with_audio = video.with_audio(audio)
video_with_audio.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret.json', SCOPES)
creds = flow.run_local_server(port=0)

youtube = build('youtube', 'v3', credentials=creds)

video_file = '/home/serverlogin/PycharmProjects/YTVidGen/.venv/output_video.mp4'
title = 'Guess The Country'
description = 'Guess the country'
tags = ['guess' , 'country', 'geography', 'quiz', 'fun']
category_id = 22

body = {
    'snippet': {
        'title': title,
        'description': description,
        'tags': tags,
        'categoryId': category_id
    },
    'status': {
        'privacyStatus': 'public'
    }
}

media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

request = youtube.videos().insert(
    part="snippet,status",
    body=body,
    media_body=media
)

try:
    response = request.execute()
    print(f"Video uploaded successfully! Video ID: {response['id']}")
except Exception as e:
    print(f"An error occurred during upload: {e}")