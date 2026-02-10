import yt_dlp

def download_video_or_playlist(url):
    ydl_opts = {
        "outtmpl": "Downloads/%(title)s.%(ext)s",  # Save file as video_title.mp4
        "format": "best",                           # Download best quality
        "ignoreerrors": True,                        # Skip videos that fail (DRM, unavailable, etc.)
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    link = input("Enter YouTube video or playlist link: ").strip()
    if link:
        try:
            download_video_or_playlist(link)
            print("\n✅ Download completed!")
        except Exception as e:
            print(f"\n❌ Download failed: {e}")
    else:
        print("⚠️ No link provided.")
