import yt_dlp
import sys


def progress_hook(d):
    """Display download progress."""
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "N/A")
        speed = d.get("_speed_str", "N/A")
        eta = d.get("_eta_str", "N/A")
        sys.stdout.write(f"\r⬇  {percent} | Speed: {speed} | ETA: {eta}   ")
        sys.stdout.flush()
    elif d["status"] == "finished":
        print(f"\n✅ Downloaded: {d.get('filename', 'unknown')}")


def download_video_or_playlist(url):
    ydl_opts = {
        # --- Output ---
        "outtmpl": "Downloads/%(title)s.%(ext)s",

        # --- Quality ---
        # Download best video + best audio separately, then merge.
        # Falls back to "best" single file if merge isn't possible.
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio/best",
        "merge_output_format": "mp4",

        # --- Post-processing ---
        "postprocessors": [
            # Embed subtitles into the video file
            {
                "key": "FFmpegEmbedSubtitle",
                "already_have_subtitle": False,
            },
            # Embed metadata (title, description, etc.)
            {
                "key": "FFmpegMetadata",
            },
            # Embed thumbnail as cover art
            {
                "key": "EmbedThumbnail",
            },
        ],

        # --- Subtitles ---
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],

        # --- Thumbnails ---
        "writethumbnail": True,

        # --- Reliability ---
        "ignoreerrors": True,
        "retries": 10,
        "fragment_retries": 10,
        "concurrent_fragment_downloads": 4,

        # --- Progress ---
        "progress_hooks": [progress_hook],

        # --- Miscellaneous ---
        "noplaylist": False,         # Allow playlists
        "consoletitle": True,        # Show title in console titlebar
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    print("🎬 Video Downloader (High Quality)")
    print("=" * 40)
    link = input("Enter YouTube video or playlist link: ").strip()
    if link:
        try:
            download_video_or_playlist(link)
            print("\n🎉 All downloads completed!")
        except Exception as e:
            print(f"\n❌ Download failed: {e}")
    else:
        print("⚠️ No link provided.")
