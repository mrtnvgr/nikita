import os

class Downloader:
    def __init__(self, data):
        self.data = data

    def download(self, type):
        for i in self.data[type]:
            file = self.data[type][i]
            if type=="audio_messages":
                os.system(f"curl -o result/{i}.mp3 {file['link']}")
            elif type=="photo":
                os.system(f"curl -o result/{i}.jpg {file['url']}")
