import Language.Infraestructure.LanguageRepository as languageRepository
    
#Metodo para obtener los datos del saludo
def getLanguage(language):
    dataLanguage = languageRepository.getLanguage(language);
    return dataLanguage

