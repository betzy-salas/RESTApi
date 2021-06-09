import json
class Users:
    def __init__(self, idUser, completeName, idNumber):
        self.idUser         =  idUser
        self.completeName   =  completeName
        self.idNumber       =  idNumber
     
    def getIdUser(self):
        return self.idUser
         
    def getCompleteName(self):
        return self.completeName

    def getIdNumber(self):
        return self.idNumber

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)