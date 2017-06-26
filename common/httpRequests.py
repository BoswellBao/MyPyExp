import requests

class HttpRequests():

    def __init__(self, req_url, req_data, req_head):
        self.req_url = req_url
        self.req_data = req_data
        self.req_head = req_head

    def sendPost(self):
        response=requests.post(self.req_url, self.req_data, self.req_head)
        return response