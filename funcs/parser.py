class historiesParser:
    def __init__(self, histories):
        self.histories = histories
        self.data = {"audio_messages": {},
                     "photos": {},
                     "videos": {}}
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
                    self.data["audio_messages"][message_id] = {"url": attachment["audio_message"]["link_mp3"]}
                elif attachment["type"]=="photo":
                    self.data["photos"][message_id] = {"date": attachment["photo"]["date"],
                                                       "text": attachment["photo"]["text"],
                                                       "url": attachment["photo"]["sizes"][-1]["url"]}
                elif attachment["type"]=="video":
                    self.data["videos"][message_id] = {"date": attachment["video"]["date"],
                                                       "title": attachment["video"]["title"],
                                                       "description": attachment["video"]["description"],
                                                       "url": max(attachment["video"]["files"])}
                elif attachment["type"] in ["sticker","gift"]:
                    pass # useless
                else:
                    print(f'Unknown attachment type: {attachment["type"]}')
    
    def result(self):
        return self.data
