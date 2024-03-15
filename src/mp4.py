from pytube import YouTube

def download_youtube_video(url, quality, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available (mp4 format)
        video_stream = yt.streams.filter(progressive=True, resolution=quality).first()

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
quality = "" + 'p'
video_url = "https://www.youtube.com/watch?v=" + yt_watch
download_youtube_video(video_url, quality, output_path="")