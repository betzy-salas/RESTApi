import Token.Infraestructure.TokenController as tokenController
import User.Aplication.SearchUser as searchUser
import Language.Aplication.SearchLanguage as searchLanguage
import Token.Domain.DataToken as dataGreetings

def testToken(requestToken):
    dataToken = {}
    dataToken = tokenController.testToken(requestToken)
    if dataToken:
        dataUser = searchUser.getUserData(dataToken);
        if dataUser:
            dataLanguage = searchLanguage.getLanguage(requestToken["language"])
            greetingResponse = dataGreetings.DataToken(dataUser.getIdUser(), dataUser.getCompleteName(), dataLanguage.getGreeting())
            return greetingResponse.toJSON()
        else:
           return None
    return None