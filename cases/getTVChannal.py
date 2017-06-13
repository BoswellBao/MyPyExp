import unittest
import ddt
import os
from common.readExcel import ReadExcel
from common.httpRequests import HttpRequests



def beforeTest():
    file_path = os.path.join(os.path.dirname(__file__), 'getChannal.xls')
    sheet_name = 'getTVChannal'

    RE = ReadExcel()
    RE.getExcelData(file_path, sheet_name)

    filter_para = ["remarks", "para_tvid", "expectedCode"]
    filter_data = RE.filterData(filter_para)
    return tuple(filter_data)#要把列表转换为元组，ddt数据源是个tuple类型



@ddt.ddt
class GetTVChannal(unittest.TestCase):

    def setUp(self):
        '''测试用例执行前的初始化'''
        print("----------开始测试----------")


    @ddt.data(*beforeTest())
    @ddt.unpack
    def test_getTVChannal(self,remarks,para_tvid,expectedCode):
        req_url = "http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx/getTVchannelDataSet"
        req_data = {'theTVstationID': para_tvid}
        req_head = {"Content-Type": "application/x-www-form-urlencoded"}
        list = [req_url, req_data, req_head]
        HttpR = HttpRequests()
        response = HttpR.sendPost(list)
        self.assertEqual(expectedCode,str(response.status_code))
        # print(response.status_code)
        # print(response.content.decode("utf-8"))
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
