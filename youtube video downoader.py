import yt_dlp

def download_highest_quality_video():
    try:
        video_url = input("your video link?: ").strip()
        save_path = input("where do you want to save video): ").strip() or "./"
        ydl_opts = {
            'format': 'bestvideo',  
            'outtmpl': f'{save_path}/%(title)s.%(ext)s', 
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("downloading...")
            ydl.download([video_url])
            print("download successfull")
    except Exception as e:
        print(f"an error occured: {e}")
download_highest_quality_video()
