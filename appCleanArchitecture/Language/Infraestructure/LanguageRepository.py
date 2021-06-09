from Language.Domain.Languages import Languages
from botocore.exceptions import ClientError
import Language.Infraestructure.LanguageConnection as DynamoDBLanguage

#Metodo para ejecutar un query condicionado sobre la tabla  Users.
def getLanguage(language):
    client=DynamoDBLanguage.getDynamodbClient()
    dataLanguage = {}
    try:
        response = client.query(
            TableName="Language",
            IndexName="LanguageIndex",
            KeyConditions={
                "Language":{
                    "ComparisonOperator":"EQ",
                    "AttributeValueList": [ {"S": language} ]
                }
            }
        )
        dataLanguage = getDataLanguage(response["Items"])
    except ClientError as e:
        return dataLanguage

    return dataLanguage

#Metodo para retornar la información de un objeto con los datos del Usuario.
def getDataLanguage(items):
    dataLanguage= {}
    if(len(items) > 0):
        dataLanguage= Languages(items[0]["Language"]["S"], items[0]["Greetings"]["S"])
    return dataLanguage
