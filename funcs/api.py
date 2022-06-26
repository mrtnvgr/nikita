import requests
import json

class VkAPI:
    VK_API_VERSION = "5.154"
    VK_API_URL="https://api.vk.ru/method/"
    def __init__(self, maxMessagesPerChat, configname="config.json"):
        self.configname = configname
        self.maxMessagesPerChat = maxMessagesPerChat
        self.reloadConfig()
        self.reloadSession()

    def reloadConfig(self):
        self.config = json.load(open(self.configname))

    def reloadSession(self):
        self.session = requests.Session()

    def request(self, method, params):
        payload = params | {"access_token": self.config['vk']['token'], "v": self.VK_API_VERSION}
        response = self.session.get(f"{self.VK_API_URL}{method}", params=payload).json()
        if "response" not in response:
            if response["error"]["error_code"] not in (917, 13): # user 404, request is too big
                raise Exception(response)
        else:
            return response["response"]
        return None

    def getConversations(self):
        print("GETTING CONVERSATIONS...")
        return self.request(method="messages.getConversations", params={"count": 200})

    def getConversationMembers(self, peer_id):
        return self.request(method="messages.getConversationMembers", params={"peer_id": peer_id,
                                                                              "count": 1000})
    def getHistory(self, conversation_name, conversation_id):
        print(f"GETTING {conversation_name} HISTORY... (id: {conversation_id})")
        offset = 0
        count = 200
        if self.maxMessagesPerChat!=None:
            if self.maxMessagesPerChat<count:
                count = self.maxMessagesPerChat
        history = []
        while True:
            anotherOne = self.request(method="messages.getHistory", params={'offset': offset, 'count': count, 'rev': 1, 'extended': 1, 'peer_id': conversation_id})
            if anotherOne==None:
                break
            if ("items" not in anotherOne) or (anotherOne["items"]==[]):
                break
            if self.maxMessagesPerChat!=None:
                if offset>=self.maxMessagesPerChat:
                    break
            #previousOne = anotherOne
            offset += 200
            history += anotherOne["items"]
            print(f"{conversation_name}: {offset} messages parsed\r", end="")
        print("")
        return history

    @staticmethod
    def getApiTokenUrl():
        return "https://vkhost.github.io/"
