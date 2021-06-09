import json
import Language.Infraestructure.LanguageController as languageController
   
#Metodo para obtener los datos del usuario
def getLanguage(language):
    dataUser = languageController.getLanguage(language);
    return dataUser