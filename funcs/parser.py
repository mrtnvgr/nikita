class historiesParser:
    def __init__(self, histories):
        self.histories = histories
        self.data = {"audio_messages": {}}
        self.parseHistories()

    def parseHistories(self):
        for history in self.histories:
            for message in history:
                message_id = message["id"]
                self.attachmentsHandler(message, message_id)
        return None

    def attachmentsHandler(self, message, message_id):
        if len(message["attachments"])>0:
            for attachment in message["attachments"]:
                if attachment["type"]=="audio_message":
                    self.data["audio_messages"][message_id] = attachment["audio_message"]["link_mp3"]
                else:
                    print(f'Unknown attachment type: {attachment["type"]}')
    
    def result(self):
        return self.data
