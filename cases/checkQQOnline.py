import unittest
import ddt
import os
from common.readExcel import ReadExcel
from common.writeExcel import WriteExcle
from common.httpRequests import GetRequest
from common.constant import Constant
from xml.etree import ElementTree as ET


global file_path,sheet_name

def dataForDDT():
    global file_path, sheet_name
    project_path = (os.path.split(os.path.dirname(__file__)))[0]
    file_path = os.path.join(project_path, Constant.EXCEL_NAME)
    sheet_name = 'checkQQOnline'

    filter_para = ["caseName","remarks", "para_QQ", "expectedCode"]
    RE = ReadExcel(file_path, sheet_name, filter_para)
    RE.getExcelData()
    filter_data = RE.filterData()
    return tuple(filter_data)    # 要把列表转换为元组，ddt数据源是个tuple类型



@ddt.ddt
class CheckQQOnline(unittest.TestCase):

    def setUp(self):
        '''测试用例执行前的初始化'''
        print("----------开始测试----------")

    @ddt.data(*dataForDDT())
    @ddt.unpack
    def test_checkQQOnline(self, caseName, remarks, para_QQ, expectedCode):
        global file_path, sheet_name
        interface_url = "/qqOnlineWebService.asmx/qqCheckOnline"
        req_url = Constant.BASIC_URL + interface_url
        print(para_QQ)
        req_data = {"qqCode": para_QQ}
        # req_head = {"Content-Type": "text/xml"}
        HttpReq = GetRequest(req_url, req_data)
        response = HttpReq.sendGet()
        #获取xml格式内容
        xml_content = response.text
        # 解析xml格式内容
        node = ET.XML(xml_content)
        '''
        Y：在线    N：离线    E：qq号码错误
        '''
        flag = "fail"
        try:
            self.assertEqual(expectedCode, node.text)
            flag = "pass"
        finally:
            write=WriteExcle(file_path, sheet_name, caseName, flag, xml_content)
            write.writeIn()

    def tearDown(self):
        '''测试用例执行完后释放资源'''
        print("----------结束测试----------")


if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(CheckQQOnline("test_checkQQOnline"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
