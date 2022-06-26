import os

class Downloader:
    def __init__(self, data):
        self.data = data

    def download(self, type):
        for i in self.data[type]:
            file = self.data[type][i]
            ext = {"audio_messages": "mp3",
                   "photos": "jpg",
                   "videos": "mp4"}
            os.system(f"curl -o result/{i}.{ext[type]} {file['url']}")

