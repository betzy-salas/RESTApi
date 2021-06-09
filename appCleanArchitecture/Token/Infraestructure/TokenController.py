import jwt
import datetime
import Token.Infraestructure.TokenProperties as tokenProperties
import Token.Domain.Token as tokenObject

#Metodo que genera un token basado en los datos del usuario
def getToken(dataUser):
    configuration = tokenProperties.getConfiguration('Token/Infraestructure/properties.json')
    if dataUser:
        dataToken = setDataToken(dataUser, configuration)
        token = jwt.encode(dataToken, configuration['JwtSecret'], configuration['JwtAlgorithm'])
        token = tokenObject.Token(token)
        return token.toJSON()
    return None

def setDataToken(dataUser, configuration):
    dataToken = {
            'id_number' : dataUser.getIdNumber(),
            'user_id'   : dataUser.getIdUser(),
            'user_name' : dataUser.getCompleteName(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=configuration['JwtExpDeltaSeconds'])
        }
    return dataToken

def testToken(requestToken):
    configuration = tokenProperties.getConfiguration('Token/Infraestructure/properties.json')
    try:
        tokenReceived = requestToken["token"]
        dataToken = jwt.decode(tokenReceived, configuration['JwtSecret'], configuration['JwtAlgorithm'])
        return dataToken
    except:
        return None