import json
class Token:
    def __init__(self, token):
        self.token         =  token
     
    def getToken(self):
        return self.token

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)