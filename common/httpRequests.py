import requests

class PostRequest():

    def __init__(self, req_url, req_data, req_head):
        self.req_url = req_url
        self.req_data = req_data
        self.req_head = req_head

    def sendPost(self):
        response=requests.post(self.req_url, self.req_data, self.req_head)
        return response


from xml.etree import ElementTree as ET
class GetRequest():
    def __init__(self, req_url, req_data):
        self.req_url = req_url
        self.req_data = req_data


    def sendGet(self):
        response = requests.get(self.req_url, self.req_data)
        return response