class historiesParser:
    def __init__(self, histories):
        self.histories = histories
        self.data = {"audio_messages": {},
                     "photos":  {},
                     "videos":  {},
                     "reposts": {},
                     "polls":   {},
                     "audios":   {}}
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
                elif attachment["type"]=="wall":
                    self.data["reposts"][message_id] = {"date": attachment["wall"]["date"],
                                                        "text": attachment["wall"]["text"]}
                    if "attachments" in attachment["wall"]:
                        self.data["reposts"][message_id]["attachments"] = attachment["wall"]["attachments"]
                elif attachment["type"]=="poll":
                    answers = {}
                    for answer in attachment["poll"]["answers"]:
                        answers[answer["text"]] = answer["votes"]
                    self.data["polls"][message_id] = {"date": attachment["poll"]["created"],
                                                      "question": attachment["poll"]["question"],
                                                      "answers": answers}
                elif attachment["type"]=="audio":
                    self.data["audios"][message_id] = {"date": attachment["audio"]["date"],
                                                       "artist": attachment["audio"]["artist"],
                                                       "title": attachment["audio"]["title"],
                                                       "url": attachment["audio"]["url"]}
                elif attachment["type"] in ["sticker","gift","graffiti"]:
                    pass # useless
                else:
                    print(f'Unknown attachment type: {attachment["type"]}')
    
    def result(self):
        return self.data
