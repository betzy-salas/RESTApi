import json

def getConfiguration(fileConfiguration):
    with open(fileConfiguration) as file: configuration = json.load(file)
    return configuration
