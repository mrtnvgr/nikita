#!/bin/python
from funcs import parser
from funcs import user
from funcs import api
import os

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

    def getConversations(self):
        conversations = self.vk.getConversations()["items"]
        return conversations

    def getConversationHistory(self, conversation):
        title = conversation["conversation"].get("chat_settings", {}).get("title", "")
        id = conversation["conversation"]["peer"]["id"]
        return self.vk.getHistory(title, id)

    def parseHistories(self, histories):
        func = parser.historiesParser(histories=histories)
        return func.result()

if __name__=="__main__":
    main = Main(maxMessagesPerChat=100)
    conversation = main.getConversations()[0]
    print(main.getConversationHistory(conversation))
    
    # names = input("Target names: ").split(" ")
    # histories = main.getUserHistories(targetNames=names)#["nerenegatik"])
    # data = main.parseHistories(histories)
    
    #print(data["videos"])
    # for i in data:
    #     print(f"{i}:")
    #     print(data[i])
