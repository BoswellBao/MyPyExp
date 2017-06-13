import xlrd


class ReadExcel():
    '''从excel文件中读取所有数据'''
    global excel_data,rf,table,rownum,colnum
    def getExcelData(self,file_url, sheetname):
        global excel_data, rf, table, rownum, colnum
        rf = xlrd.open_workbook(file_url, 'r')
        table = rf.sheet_by_name(sheetname)
        rownum = table.nrows
        colnum = table.ncols
        global excel_data
        excel_data = []
        for i in range(rownum):
            excel_data.append(table.row_values(i))

    def filterData(self,filter_para):
        global excel_data, rf, table, rownum, colnum
        para_num = len(filter_para)
        final_data = []
        map={}
        #给要找的字段和列号做成字典
        for i in range(colnum):
            for j in range(para_num):
                if(excel_data[0][i] == filter_para[j]):
                    map[excel_data[0][i]] = i
                    break

         #找出要执行用例的数据
        for i in range(1,rownum):
            row_data = []#这个只能定义在这里，外循环一次完了就要初始化一次
            if "y" in excel_data[i]:
                for j in range(para_num):
                    row_data.append(excel_data[i][map[filter_para[j]]])
                final_data.append(row_data)
            else:
                continue

        return final_data



