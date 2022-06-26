import os

class Downloader:
    def __init__(self, data):
        self.data = data

    def download(self, type):
        ext = {"audio_messages": "mp3",
               "audios": "mp3",
               "photos": "jpg",
               "videos": "mp4"}
        if type in list(ext.values()):
            for i in self.data[type]:
                file = self.data[type][i]
                os.system(f"curl -o result/{type}/{i}.{ext[type]} {file['url']}")
        elif type=="docs":
            for i in self.data["docs"]:
                file = self.data[type][i]
                os.system(f"curl -o result/{type}/{i}.{file['ext']} {file['url']}")
        else:
            print("o_o")
