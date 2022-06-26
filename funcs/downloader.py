import os

class Downloader:
    def __init__(self, data):
        self.data = data

    def download(self, type):
        ext = {"audio_messages": "mp3",
               "audios": "mp3",
               "photos": "jpg"}
               #"videos": "mp4"}
        print(f"Downloading {type}...")
        if type in list(ext.keys()):
            for i in self.data[type]:
                file = self.data[type][i]
                # if type=="videos":
                #     if "mp4" not in file["quality"]:
                #         continue
                os.system(f"curl -o result/{type}/{i}.{ext[type]} {file['url']} ")
                print(file['url'])
        elif type=="docs":
            for i in self.data["docs"]:
                file = self.data[type][i]
                print(file['url'])
                os.system(f"curl -o result/{type}/{i}.{file['ext']} {file['url']} ")
        else:
            print("o_o")

    def downloadAll(self):
        for type in list(self.data.keys()):
            self.download(type)
