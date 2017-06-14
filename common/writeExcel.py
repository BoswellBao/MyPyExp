import os
import xlrd
from xlutils.copy import copy

class WriteExcle():
    def writeIn(self,file_path,sheet_name,case_name,flag,response_content):
        try:
            rf = xlrd.open_workbook(file_path)
            rf_sheet = rf.sheet_by_name(sheet_name)
            rownum = rf_sheet.nrows
            colnum = rf_sheet.ncols
            case_row_index = 0
            for i in range(rownum):
                if(case_name in rf_sheet.row_values(i)):
                    case_row_index = i
                    break

            wf = copy(rf)
            index = wf.sheet_index(sheet_name)
            wt_sheet = wf.get_sheet(index)
            wt_sheet.write(case_row_index,colnum - 2,flag)
            wt_sheet.write(case_row_index,colnum - 1,response_content)
            wf.save(os.path.join(os.path.dirname(__file__), 'getChannal.xls'))
        except Exception as e:
            print(e)


