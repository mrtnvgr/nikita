import os

class Downloader:
    def __init__(self, data):
        self.data = data

    def download(self, type):
        for i in self.data[type]:
            url = self.data[type][i]
            os.system(f"curl -o result/{i}.mp3 {url}")
