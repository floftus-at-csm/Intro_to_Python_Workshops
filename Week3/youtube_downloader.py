from yt_dlp import YoutubeDL
def download_videos_simple(url, output_loc, max="100M"):
    Path(output_loc).mkdir(parents=True, exist_ok=True)
    out = output_loc + "%(title)s-%(id)s.%(ext)s"
    ydl_opts = {
    'format': 'best',
    'max': '100M',
    'outtmpl': out,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    # subprocess.run(['youtube-dl', '-o', output_loc, '-f', 'best', '--max-filesize', max, url], capture_output=True)
    print("video downloaded")