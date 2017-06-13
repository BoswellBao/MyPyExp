import requests

class HttpRequests():
    def sendPost(self,list):
        response=requests.post(list[0],list[1],list[2])
        return response