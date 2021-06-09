import json
import User.Infraestructure.UserController as userController
   
#Metodo para obtener los datos del usuario
def getUser(requestData):
    dataUser = userController.getUser(requestData["IdUser"], requestData["Password"]);
    return dataUser

#Metodo para obtener los datos del usuario
def getUserData(requestData):
    dataUser = userController.getUserData(requestData["user_id"], requestData["id_number"]);
    return dataUser