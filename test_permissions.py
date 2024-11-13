import yt_dlp

def download_video(url, output_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Choose best video and audio quality
        'outtmpl': output_path,  # Save the file to the desktop
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
url = "https://ww4.fmovies.co/film/under-the-dome-season-1-4439/"
output_path = '/Users/macbook/Desktop/underthedome.mp4'

download_video(url, output_path)
