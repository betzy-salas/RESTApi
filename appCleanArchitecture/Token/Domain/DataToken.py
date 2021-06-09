import json
class DataToken:
    def __init__(self, idUser, userName, greetings):
        self.idUser         =  idUser
        self.userName       =  userName
        self.greetings      =  greetings

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)