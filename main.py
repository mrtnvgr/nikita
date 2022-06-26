#!/bin/python
import os
from funcs.downloader import Downloader
from funcs import parser
from funcs import user
from funcs import api

class Main:
    def __init__(self, maxMessagesPerChat=None):
        configname = self.getConfigName()
        self.vk = api.VkAPI(configname=configname, maxMessagesPerChat=maxMessagesPerChat)
    
    @staticmethod
    def getConfigName():
        if os.path.exists("custom.json"):
            return "custom.json"
        else:
            return "config.json"

    def getUserHistories(self, targetNames):
        func = user.GetUserHistories(vk_session=self.vk, targetNames=targetNames)
        return func.result()

    def parseHistories(self, histories):
        func = parser.historiesParser(histories=histories)
        return func.result()

if __name__=="__main__":
    main = Main(maxMessagesPerChat=100)
    histories = main.getUserHistories(targetNames=["nerenegatik"])
    data = main.parseHistories(histories)
    #downloader = Downloader(data)
    #downloader.download(type="audio_messages")
