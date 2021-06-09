import boto3
import json

#Conexión a cliente Dynamo
def getDynamodbClient():
    credentials = getCredentials('Infraestructure/properties.json')
    client = boto3.client(credentials["service_name"], region_name=credentials["region_name"], aws_access_key_id=credentials["aws_access_key_id"], aws_secret_access_key=credentials["aws_secret_access_key"])
    return client

def getCredentials(fileCredential):
    with open(fileCredential) as file: credentials = json.load(file)
    return credentials

