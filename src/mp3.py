from pytube import YouTube

def download_mp3_from_youtube(video_url, output_path):
    try:
        # Create a YouTube object for the given video URL
        yt = YouTube(video_url)

        # Filter for only audio streams with the file extension 'mp4'
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

        if not audio_stream:
            raise Exception("No MP4 audio stream found for the given URL.")

        # Download the audio stream to the output path
        audio_stream.download(output_path)

        print("MP3 download successful!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'YOUR_YOUTUBE_URL' with the URL of the video you want to download
yt_watch = ""
youtube_url = "https://www.youtube.com/watch?v=" + yt_watch

# Replace 'YOUR_OUTPUT_PATH' with the desired download location on your system
output_path = ""

download_mp3_from_youtube(youtube_url, output_path)
