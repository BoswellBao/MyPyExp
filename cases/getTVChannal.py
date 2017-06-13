import unittest
from common.httpRequests import HttpRequests


class GetTVChannal(unittest.TestCase):
    def setUp(self):
        '''测试用例执行前的初始化'''
        print("----------开始测试----------")

    def test_getTVChannal(self):
        req_url = "http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getTVchannelDataSet"
        req_data = {'theTVstationID': "ged"}
        req_head = {"Content-Type":"application/x-www-form-urlencoded"}
        list=[req_url,req_data,req_head]
        response = HttpRequests.sendPost(list)
        print(response.status_code)
        print(response.content.decode("utf-8"))
        # f=open('./test.txt','w')
        # f.write(response.content.decode("utf-8"))
        # f.close()

    def tearDown(self):
         '''测试用例执行完后释放资源'''
         print("----------结束测试----------")

    def suite(self):
        suit = unittest.TestSuite()
        suit.addTest(GetTVChannal("test_getTVChannal"))
        return suit

if __name__ == "__main__":
    unittest.main(defaultTest="suit")