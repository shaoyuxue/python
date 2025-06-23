import pandas as pd
workbook_vbaQF=pd.read_excel('C:\\Users\\shaoyuxue\\Desktop\\账.xls',sheet_name='企业付')
workbook_pyQF=workbook_vbaQF.reindex(columns=['Unnamed: 5', '摘要', '付'])

workbook_vbaQS=pd.read_excel('C:\\Users\\shaoyuxue\\Desktop\\账.xls',sheet_name='企业收')
workbook_pyQS=workbook_vbaQS.reindex(columns=['Unnamed: 5', '摘要', '收'])

workbook_vbaYF=pd.read_excel('C:\\Users\\shaoyuxue\\Desktop\\银行流水.xls',sheet_name='银行付')
workbook_pyYF=workbook_vbaYF.reindex(columns=['日期', '摘要', '借方发生额（支出）'])

workbook_vbaYS=pd.read_excel('C:\\Users\\shaoyuxue\\Desktop\\银行流水.xls',sheet_name='银行收')
workbook_pyYS=workbook_vbaYS.reindex(columns=['日期', '摘要', '贷方发生额（收入）'])

'''核对收款唯一值'''
df_merge=workbook_pyYS.merge(workbook_pyQS,left_on='贷方发生额（收入）',right_on='收',how='outer')
pd.set_option('display.max_columns', None)
df_merge.to_excel('C:/Users/shaoyuxue/Desktop/收.xlsx')


'''核对付款唯一值'''
df_merge=workbook_pyYF.merge(workbook_pyQF,left_on='借方发生额（支出）',right_on='付',how='outer')
pd.set_option('display.max_columns', None)
df_merge.to_excel('C:/Users/shaoyuxue/Desktop/付.xlsx')