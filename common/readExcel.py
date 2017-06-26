import xlrd


class ReadExcel():
    '''
    从excel文件中读取所有数据
    '''

    global excel_data, read_file, table, rownum, colnum

    def __init__(self, file_path, sheet_name, filter_para):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.filter_para = filter_para

    def getExcelData(self):
        global excel_data, read_file, table, rownum, colnum
        read_file = xlrd.open_workbook(self.file_path, 'r')
        table = read_file.sheet_by_name(self.sheet_name)
        rownum = table.nrows
        colnum = table.ncols
        excel_data = []
        for i in range(rownum):  # 把每行作为一个元素放到excel_data这个列表里面，excel_data就成为二维数组
            excel_data.append(table.row_values(i))

    def filterData(self):
        global excel_data, read_file, table, rownum, colnum
        para_num = len(self.filter_para)
        final_data = []
        dict = {}
        # 给要找的字段和列号做成字典
        for i in range(colnum):
            for j in range(para_num):
                if (excel_data[0][i] == self.filter_para[j]):
                    dict[excel_data[0][i]] = i    # 列名为key，列号为value
                    break

        # 找出要执行用例的数据
        for i in range(1, rownum):
            row_data = []    # 这个只能定义在这里，外循环一次完了就要初始化一次
            if "y" or "Y" in excel_data[i]:
                for j in range(para_num):
                    row_data.append(excel_data[i][dict[self.filter_para[j]]])
                final_data.append(row_data)
            else:
                continue

        return final_data

