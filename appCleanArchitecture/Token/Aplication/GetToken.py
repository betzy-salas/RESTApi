import User.Aplication.SearchUser as searchUser
import Token.Infraestructure.TokenController as tokenController

def getToken(requestData):
    dataUser = searchUser.getUser(requestData);
    if dataUser:
        return tokenController.getToken(dataUser)
    return None