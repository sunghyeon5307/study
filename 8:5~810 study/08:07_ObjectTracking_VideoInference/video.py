from pytubefix import YouTube
import os

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

video_path = 'https://youtu.be/WVb-cQUID2A?si=l3Ex9ZtsBnfihUjU'
downloadYouTube(video_path, 'videos')