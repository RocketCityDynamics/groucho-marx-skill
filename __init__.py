from mycroft import MycroftSkill, intent_file_handler


class GrouchoMarx(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('marx.groucho.intent')
    def handle_marx_groucho(self, message):
        self.speak_dialog('marx.groucho')


def create_skill():
    return GrouchoMarx()

