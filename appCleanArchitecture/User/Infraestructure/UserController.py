import User.Infraestructure.UserRepository as userRepository
    
#Metodo para obtener los datos del usuario
def getUser(idUser, password):
    dataUser = userRepository.getUserItems(idUser, password);
    return dataUser

#Metodo para obtener los datos del usuario
def getUserData(idUser, idNumber):
    dataUser = userRepository.getUserData(idUser, idNumber);
    return dataUser
