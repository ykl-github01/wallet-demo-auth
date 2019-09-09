import xlrd

class ReadExcle(object):
    '''
    classdoc
    '''

    def __init__(self, file, tag='True'):
        self.file = file
        self.tag = tag

    '''
                输入参数，返回某个sheet列表中的所有值
        sheetname:excel文件的具体sheet名称
        n：开始行数，从第n行开始读
        num:读取num行
    '''

    def read(self, sheetname, n=1, num=1000):  # i,sheet索引
        ExcelFile = xlrd.open_workbook(self.file)
        table = ExcelFile.sheet_by_name(sheetname)
        nrows = table.nrows  # 行数
        ncols = table.ncols  # 列数
        j = 0  # 循环次数
        for row in range(1, nrows):
            j += 1
            line = []
            if self.tag == 'True':
                for col in range(0, ncols):
                    line.append(table.cell(row, col).value)
                yield line
            elif self.tag == 'False':
                if j >= n and j < n + num:
                    for col in range(0, ncols):
                        line.append(table.cell(row, col).value)
                    yield line

    '''
                 读取页面元素表
         list1 页面元素路径列表
         list2 页面元素js列表
    '''

    def get(self, sheetname):
        ExcelFile = xlrd.open_workbook(self.file)
        sheet = ExcelFile.sheet_by_name(sheetname)  # 'Sheet1'
        nrows = sheet.nrows  # 总行数
        list0 = []  # 元素名称列表
        list1 = []  # 元素路径列表
        list2 = []  # js列表
        for i in range(1, nrows):  # i为行数
            if sheet.row(i)[2].value != 'null':
                r1 = sheet.row(i)[2].value
                r2 = sheet.row(i)[3].value
                list0.append(sheet.row(i)[0].value)
                list1.append(r1 + '=>' + r2)
                dict1 = dict(zip(list0, list1))
            else:
                list2.append(sheet.row(i)[3].value)
        return dict1, list2

    '''
                返回excel文件具体sheet的具体某个单元格的值
        i,j为单元格所在位置
    '''

    def read_1(self, sheetname, i, j):
        ExcelFile = xlrd.open_workbook(self.file)
        table = ExcelFile.sheet_by_name(sheetname)
        # print(table.cell(1,0).value)
        return table.cell(i, j).value

    '''
               读取给定列数，如读取该表中第3
    '''

    def read_ncols(self, sheetname,i):  # i,sheet索引
        ExcelFile = xlrd.open_workbook(self.file)
        table = ExcelFile.sheet_by_name(sheetname)
        lins=table.col_values(i)
        return lins
