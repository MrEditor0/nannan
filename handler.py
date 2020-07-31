import  pandas  as pd
import os
from openpyxl.workbook import Workbook
import numpy as np
import math
path = r''
excelFile = os.path.join(path,'expression_GSEA.xls')

down_common_p_0_001 = []
down_common_p_0_0001 = []
down_MET_minus_p_0_001 = []
down_MET_minus_p_0_0001 = []
down_MET_plus_p_0_001 = []
down_MET_plus_p_0_0001 = []

up_common_p_0_0001 = []
up_common_p_0_0001 = []
up_MET_minus_p_0_001 = []
up_MET_minus_p_0_0001 = []
up_MET_plus_p_0_001 = []
up_MET_plus_p_0_0001 = []
test_list = ['ENSG00000049541','ENSG00000173110','ENSG00000125618','ENSG00000125618']

res_list = []
file_paths = [r'0.001.xlsx',
r'0.0001.xlsx',
r'0.00001.xlsx']

sheet_names = [r'0.001',
r'0.0001',
r'0.00001']

# file_paths = [r'downcommonp0.001.xlsx',
# r'downcommonp0.0001.xlsx',
# r'downMETp0.001.xlsx',
# r'downMETp0.0001.xlsx',
# r'downmetplusp0.001.xlsx',
# r'downmetplusp0.0001.xlsx',
# r'upcommonp0.001.xlsx',
# r'upcommonp0.0001.xlsx',
# r'upmetp0.001.xlsx',
# r'upmetp0.0001.xlsx',
# r'upmetplusp0.001.xlsx',
# r'upmetplusp0.0001.xlsx']

# sheet_names = [r'down_common_p0.001',
# r'down_common_p0.0001',
# r'down_MET-_p0.001',
# r'down_MET-_p0.0001',
# r'down_met+_p0.001',
# r'down_met+_p0.0001',
# r'up_common_p0.001',
# r'up_common_p0.0001',
# r'up_met-_p0.001',
# r'up_met-_p0.0001',
# r'up_met+_p0.001',
# r'up_met+_p0.0001']

def is_str(temp):
    string = str(temp)
    return string.isalnum()

def get_list():
    global res_list
    for path in file_paths:
        print('读取文件{0}'.format(path))
        df = pd.read_excel(path,sheet_name=0)
        row = df.iloc[0:df.shape[0],0].tolist()
        res_list.append(row)
    # df = pd.read_excel(r'upmetp0.0001.xlsx',sheet_name=0,header = 2)
    # row = df.iloc[0:df.shape[0],0].tolist()
    # print(len(list(filter(None, row))))
    # res_list.append(row)
 

def main():
    #df=pd.read_excel('test.xlsx')
    df=pd.read_excel('newdb.xlsx',sheet_name=0,header = 0)
    print(df.head())
    # row = df.iloc[0:df.shape[0],0]
    # up_MET_plus_p_0_0001 = row.tolist()
    # print(type(row))
    # print('------')
    # print(up_MET_plus_p_0_0001)
    
    #print(data.shape[0])
    data_frames = []
    for res in res_list:
        print(len(res))
        frame_data = df[df['ID'].isin(res)]
        data_frames.append(frame_data)
        #print(frame_data)
        #class_data.to_excel('output.xlsx', sheet_name='Sheet2',index=False)
        print(frame_data.shape)
    with pd.ExcelWriter('output_res_newdb.xlsx') as writer:  
        for i in range(len(sheet_names)):
            print('The {0}rd times write ---'.format(i))
            print('sheetname {0}'.format(sheet_names[i]))

            data_frames[i].to_excel(writer, sheet_name=sheet_names[i],index = False)
    print('finished !!!')
    # class_data = data[data['NAME'].isin(test_list)]
    # temp_data = class_data.head()
    # print('选取的值{0}'.format(temp_data))
    # #data=df.index(0).value''s
    # print("获取到所有的值:\n{0}".format(data['NAME']))


if __name__ == "__main__":
    print('handler starting .............')
    #main()
    get_list()
    main()
    print('handler finished .............')    


