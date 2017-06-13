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
        row_data = [para_num - 1]
        map={}
        #给要找的字段和列号做成字典
        for i in range(colnum):
            for j in range(para_num):
                if(excel_data[0][i] == filter_para[j]):
                    map[excel_data[0][i]] = i
                    break
         #找出要执行用例的数据
        rj = 0
        for i in range(1,rownum):
            if "y" in excel_data[i]:
                for j in range(para_num):
                    row_data[j]=excel_data[i][map[filter_para[j]]]
                final_data.append(row_data)
                rj += 1
            else:
                continue
        #for m in final_data: print(m)

        return final_data



