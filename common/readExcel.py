import xlrd

class ReadExcel():
    '''从excel文件中读取所有数据'''

    def getData(file_url, sheetname):
        rf=xlrd.open_workbook(file_url, 'r')
        table=rf.sheet_by_name(sheetname)
        rownum=table.nrows
        colnum=table.ncols
        excel_data=[rownum-1][colnum-1]
        for i in range(rownum):
            excel_data.append(table.row_values(i))
