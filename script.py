import yt_dlp

def download_video_or_playlist(url):
    ydl_opts = {
        "outtmpl": "Downloads/%(title)s.%(ext)s",  # Save file as video_title.mp4
        "format": "best"                 # Download best quality
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    link = input("Enter YouTube video or playlist link: ").strip()
    if link:
        download_video_or_playlist(link)
        print("✅ Download completed!")
    else:
        print("⚠️ No link provided.")
