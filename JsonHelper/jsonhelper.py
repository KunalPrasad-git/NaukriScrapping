import json

class JsonHelper:
    
    __instance = None

    def __init__(self):
        if JsonHelper.__instance != None:
            raise Exception("This is a singleton class.Cannot be craeted from outside.Call the get instance function to get object")
        else:
            self.__instance = self


    @staticmethod
    def getInstance():
        if JsonHelper.__instance == None:
            JsonHelper.__instance = JsonHelper()
        return JsonHelper.__instance
        

    def readJson(self,fileName):
        print("Reading json")
        fileInstance = open(fileName)
        data=json.load(fileInstance)
        return data

