import os
import xlrd
from xlwt import easyxf
from xlutils.copy import copy

class WriteExcle():

    def __init__(self, file_path, sheet_name, caseName, flag, content):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.caseName = caseName
        self.flag = flag
        self.content = content

    def writeIn(self):
        try:
            rf = xlrd.open_workbook(self.file_path,formatting_info=True)    # 保持格式
            rf_sheet = rf.sheet_by_name(self.sheet_name)
            rownum = rf_sheet.nrows
            colnum = rf_sheet.ncols
            case_row_index = 0
            for i in range(rownum):
                if(self.caseName in rf_sheet.row_values(i)):    # 根据用例名称找到刚刚执行的那条用例的行号
                    case_row_index = i
                    break

            """
           python不能直接打开一个已有的数据的excel然后修改数据，只能通过copy方法。
           copy方法相当于创建了一个和原来一样的excel，然后写入了一样的东西，再再上面改动数据。
           下面写死-2，-1是固定excel的倒数一、二列是returnData和executeResult
           """
            wf = copy(rf)    # 复制打开的excel
            index = wf.sheet_index(self.sheet_name)
            wt_sheet = wf.get_sheet(index)    # 指定要写入的工作表

            wt_sheet.write(case_row_index,colnum - 2,self.flag)    # 根据行号列号找到单元格并写入数据
            wt_sheet.write(case_row_index,colnum - 1,self.content)
            wf.save(self.file_path)
        except Exception as e:
            print(e)


