import requests

class HttpRequests():
    def sendPost(self,requesturl,data,heades):
        self.requestURL=requesturl
        self.data=data
        self.heades=heades
        response=requests.post(self.requestURL,self.data,self.heades)
        return response