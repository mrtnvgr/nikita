class GetUserHistories:
    def __init__(self, vk_session, targetNames: list):
        self.vk = vk_session
        self.getTargets(targetNames)
    
    def result(self):
        return self.getConversationsHistory()

    def parseConversations(self):
        conversations = self.vk.getConversations()["items"]
        targetConversations = []
        for conversation in conversations:
            conversation_name, conversation_id = self.getConversationData(conversation)
            checkResult = self.checkConversation(conversation_id)
            if checkResult:
                print(f"Target: {conversation_name} (id: {conversation_id})")
                targetConversations.append([conversation_name, conversation_id])
        return targetConversations

    def getConversationData(self, conversation):
        conversation_id = conversation["conversation"]["peer"]["id"]
        conversation_name = conversation["conversation"].get("chat_settings", "")
        if type(conversation_name) is not str:
            conversation_name = conversation_name["title"]
        return conversation_name, conversation_id

    def checkConversation(self, peer_id):
        members = self.vk.getConversationMembers(peer_id)
        if members==None: return False
        for member in members["profiles"]:
            name = member.get("screen_name", "")
            for targetName in self.targets["name"]:
                if targetName in name:
                    return True
        return False

    def getConversationsHistory(self):
        targetConversations = self.parseConversations()
        histories = []
        for conversation in targetConversations:
            history = self.vk.getHistory(conversation[0], conversation[1])
            histories.append(self.getTargetMessages(history))
        return histories

    def getTargetMessages(self, history):
        for message in history[:]:
            for id in self.targets["id"]:
                if id!=message["from_id"]:
                    history.remove(message)
            if message in history and message["out"]==1:
                history.remove(message)
        return history

    def getTargets(self, usernames):
        if type(usernames) is str: usernames = [usernames]
        users = self.vk.request(method="users.get", params={"user_ids": ','.join(usernames)})
        self.targets = {"name": [],
                        "id": []}
        self.targets["name"] = usernames
        for i in range(len(users)):
            self.targets["id"].append(users[i]["id"])
