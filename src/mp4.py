from pytube import YouTube

def download_youtube_video(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available (mp4 format)
        video_stream = yt.streams.filter(file_extension="mp4").first()

        if video_stream is not None:
            # Set the output path if provided, otherwise use the current directory
            if output_path:
                video_stream.download(output_path)
            else:
                video_stream.download()
            print("Download complete!")
        else:
            print("No mp4 video found for the provided URL.")
    except Exception as e:
        print(f"An error occurred: {e}")

yt_watch = ""
video_url = "https://www.youtube.com/watch?v=" + yt_watch
download_youtube_video(video_url, output_path="")

"""
    It still lack in quality
"""