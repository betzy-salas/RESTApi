import Token.Infraestructure.TokenController as tokenController
import Language.Aplication.SearchLanguage as searchLanguage
import Token.Domain.DataToken as dataGreetings

def testToken(requestToken):
    dataToken = {}
    dataToken = tokenController.testToken(requestToken)
    if dataToken:
        dataLanguage = searchLanguage.getLanguage(requestToken["language"])
        greetingResponse = dataGreetings.DataToken(dataToken['user_id'], dataToken['user_name'], dataLanguage.getGreeting())
        return greetingResponse.toJSON()

    return None