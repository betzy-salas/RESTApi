from User.Domain.Users import Users
from botocore.exceptions import ClientError
import User.Infraestructure.UserConnection as DynamoDBUsers

#Metodo para ejecutar un query condicionado sobre la tabla  Users.
def getUserItems(ParamOne, ParamTwo):
    client=DynamoDBUsers.getDynamodbClient()
    dataUser = {}
    try:
        response = client.query(
            TableName="Users",
            IndexName="ValidUserIndex",
            KeyConditions={
                "IdUser":{
                    "ComparisonOperator":"EQ",
                    "AttributeValueList": [ {"S": ParamOne} ]
                },
                "Password":{
                    "ComparisonOperator":"EQ",
                    "AttributeValueList": [ {"S": ParamTwo} ]
                }
            }
        )
        dataUser = getUserJson(response["Items"])
    except ClientError as e:
        return dataUser

    return dataUser

#Metodo para retornar la información de un objeto con los datos del Usuario.
def getUserJson(items):
    dataUser= {}
    if(len(items) > 0):
            dataUser= Users(items[0]["IdUser"]["S"], items[0]["CompleteName"]["S"], items[0]["IdNumber"]["N"])
    return dataUser

def getUserData(idUser, idNumber):
    client=DynamoDBUsers.getDynamodbClient()
    dataUser = {}
    try:
        response = client.query(
            TableName="Users",
            IndexName="IndexNumber",
            KeyConditions={
                "IdUser":{
                    "ComparisonOperator":"EQ",
                    "AttributeValueList": [ {"S": idUser} ]
                },
                "IdNumber":{
                    "ComparisonOperator":"EQ",
                    "AttributeValueList": [ {"N": idNumber} ]
                }
            }
        )
        dataUser = getUserDataJson(response["Items"])
    except ClientError as e:
        return dataUser

    return dataUser

#Metodo para retornar la información de un objeto con los datos del Usuario.
def getUserDataJson(items):
    dataUser= {}
    if(len(items) > 0):
            dataUser= Users(items[0]["IdUser"]["S"], items[0]["CompleteName"]["S"], items[0]["IdNumber"]["N"])
    return dataUser