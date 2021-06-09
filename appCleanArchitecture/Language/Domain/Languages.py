import json
class Languages:
    def __init__(self, language, greetings):
        self.language         =  language
        self.greetings        =  greetings
     
    def getLanguage(self):
        return self.language
         
    def getGreeting(self):
        return self.greetings