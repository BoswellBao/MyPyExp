import unittest
import ddt
import os
from common.readExcel import ReadExcel
from common.writeExcel import WriteExcle
from common.httpRequests import PostRequest
from common.constant import Constant


global file_path,sheet_name

def dataForDDT():
    global file_path, sheet_name
    project_path = (os.path.split(os.path.dirname(__file__)))[0]
    file_path = os.path.join(project_path, Constant.EXCEL_NAME)
    sheet_name = 'getTVChannal'

    filter_para = ["caseName","remarks", "para_tvid", "expectedCode"]
    RE = ReadExcel(file_path, sheet_name, filter_para)
    RE.getExcelData()
    filter_data = RE.filterData()
    return tuple(filter_data)    # 要把列表转换为元组，ddt数据源是个tuple类型



@ddt.ddt
class GetTVChannal(unittest.TestCase):
    '''测试获取电视节目接口

    '''

    def setUp(self):
        '''测试用例执行前的初始化'''
        print("----------开始测试----------")


    @ddt.data(*dataForDDT())
    @ddt.unpack
    def test_getTVChannal(self,caseName,remarks,para_tvid,expectedCode):
        global file_path, sheet_name
        interface_url = "/ChinaTVprogramWebService.asmx/getTVchannelDataSet"
        req_url = Constant.BASIC_URL + interface_url
        req_data = {'theTVstationID': para_tvid}
        req_head = {"Content-Type": "application/x-www-form-urlencoded"}
        HttpReq = PostRequest(req_url, req_data, req_head)
        response = HttpReq.sendPost()
        content = response.content.decode('utf-8')
        flag = "fail"
        try:
            self.assertEqual(expectedCode, str(response.status_code))
            flag = "pass"
        finally:
            write=WriteExcle(file_path, sheet_name, caseName, flag, content)
            write.writeIn()


    def tearDown(self):
        '''测试用例执行完后释放资源'''
        print("----------结束测试----------")


if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(GetTVChannal("test_getTVChannal"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)