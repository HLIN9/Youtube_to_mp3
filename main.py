import os
from pytube import YouTube

def download_audio(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Select the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

        # Download the audio stream
        audio_stream.download(output_path=output_path)

        print(f"Audio from '{yt.title}' has been downloaded and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Get the YouTube video URL from user input
    video_url = input("Enter the YouTube video URL: ")

    # Define the directory where you want to save the audio
    output_directory = 'audio_downloads'

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Download and save the audio
    download_audio(video_url, output_directory)
