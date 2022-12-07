from yt_dlp import YoutubeDL
from pathlib import Path

def download_videos_simple(url, output_loc, max="100M"):
    Path(output_loc).mkdir(parents=True, exist_ok=True)
    out = output_loc + "%(title)s-%(id)s.%(ext)s"
    ydl_opts = {
    'format': 'best',
    'max': '100M',
    'outtmpl': out,
    '--download-sections' :"*10:15-inf",
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    # subprocess.run(['youtube-dl', '-o', output_loc, '-f', 'best', '--max-filesize', max, url], capture_output=True)
    print("video downloaded")

def download_videos_in_list(list_v, output_loc, max="100M"):
    for video in list_v:
        download_videos_simple(video, output_loc, max)
    print("all videos downloaded")

# download_videos_in_list(the_ids, output_location, max="100M")
urls = ['https://www.youtube.com/watch?v=_7FWUGeJmsI', 'https://www.youtube.com/watch?v=CFZe_TBe4CE', 'https://www.youtube.com/watch?v=ovaf5H1UZnQ', 'https://www.youtube.com/watch?v=Qvb8z5djGv4', 'https://www.youtube.com/watch?v=2714Cr3SWPU']
download_videos_simple(urls[0], "content/youtube-downloads/")