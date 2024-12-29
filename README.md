# YTStoryGenerator
# YouTube Video Automation Tool
This repository contains a Python script that automates the creation and uploading of YouTube videos. The tool uses AI to generate dynamic content, converts text to speech, merges audio with a base video, and uploads the final output directly to a YouTube channel.
## **Features**
1. **Script Generation**:
    - Uses an AI model to generate scripts based on the "Guess The Country" game format.
    - Users are presented with five clues to guess a random country, and the country is revealed at the end.

2. **Text-to-Speech Conversion**:
    - Converts the generated script into an audio file using Google Text-to-Speech (gTTS).

3. **Audio-Video Merging**:
    - Combines the TTS-generated audio with a base video to create the final video.

4. **YouTube Upload**:
    - Uploads the final edited video directly to a YouTube account using the YouTube Data API v3.

## **Setup**
### 1. Prerequisites
- Python (recommended version >= 3.8).
- Google Cloud Project with the **YouTube Data API v3** enabled.
- Base video file for the final video (e.g., `input.mp4`).
- The `client_secret.json` file for YouTube API credentials.
- Internet connection for API calls and uploading to YouTube.

### 2. Installation
Install the required dependencies by running:
``` bash
pip install langchain-ollama gtts moviepy google-auth google-auth-oauthlib google-api-python-client
```
### 3. Configuration
- Ensure the base video (`input.mp4`) is available in the root folder.
- Place `client_secret.json` (YouTube credentials file) in the same directory.
- Optional: Update the title, description, tags, and category of the video in the script.

## **Usage**
1. Run the script with:
``` bash
   python main.py
```
1. Follow the on-screen prompt to authorize access to your YouTube channel.
2. Once authorized, the script will:
    - Generate the video.
    - Merge the audio and video.
    - Upload the final video to your YouTube account with the provided metadata.

3. Upon a successful upload, the script will display the **Video ID** of the uploaded video.

## **Customization Options**
1. **Video Topics**
The script is currently hardcoded for the "Guess The Country" game format. You can customize the LLM (Large Language Model) prompt to experiment with new topics. Update the following line in the script:
``` python
model.invoke(input="Your custom prompt here")
```
1. **Video Metadata**
Change variables in the script for:
    - Title: `title`
    - Description: `description`
    - Tags: `tags` (list of keywords)
    - Category ID: `category_id` (YouTube categories. Example: `22` is for People & Blogs)

2. **Input Video File**
Replace `input.mp4` with another video to use as your base template.

## **How It Works**
1. **Script Creation**:
The AI model generates a script for a video topic (e.g., "Guess The Country").
2. **Text-to-Speech**:
The generated script is converted into speech using Google Text-to-Speech (gTTS).
3. **Audio Merging**:
The speech audio is synced and merged with the base video file using MoviePy.
4. **YouTube Upload**:
The merged video is automatically uploaded, using metadata predefined in the script.

## **Required File Structure**
Your project folder should look like this:
``` 
project_directory/
│
├── main.py                 # The main script containing the logic
├── input.mp4               # Base video for the final content
├── client_secret.json      # YouTube API credentials
├── output.mp3              # Generated audio file (TTS output)
├── output_video.mp4        # Resulting video after merging audio and video
├── requirements.txt        # List of dependencies (optional)
```
## **Dependencies**
- **LangChain Ollama**: Used for language model interaction.
- **gTTS (Google Text-to-Speech)**: Converts text scripts into audio.
- **MoviePy**: Handles video editing tasks (audio merging).
- **Google Auth and YouTube API Client**: Uses the YouTube Data API to upload the video.

Install dependencies with:
``` bash
pip install -r requirements.txt
```
## **Known Problems and Troubleshooting**
1. **YouTube API Authorization**:
    - If the browser doesn't open for authorization or access is denied, ensure `client_secret.json` is correctly configured.

2. **Dependency Issues**:
    - Use `pip` to verify and (re)install any missing libraries:
``` bash
     pip install <library_name>
```
1. **Invalid Input Files**:
    - Ensure `input.mp4` exists in the directory and is a valid video file.

2. **Upload Errors**:
    - If upload fails, verify internet connectivity and ensure your YouTube account has permissions enabled for the API.

## **Future Improvements**
- Add support for automating the generation of various topics.
- Introduce scheduling for automatic uploads (e.g., daily or weekly).
- Expand customization options through configuration files.

## **License**
This project is licensed under the MIT License.
Use this tool to seamlessly create and share YouTube videos with minimal manual effort! Enjoy! 🎥✨
