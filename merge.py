import os
import pandas as pd
path=os.getcwd()
files=os.listdir(path)
files_xls=[f for f in files if f[-4:]=='xlsx']
worksheets=[]
for f in files_xls:
	df=pd.read_excel(f,ignore_index=True)
	worksheets.append(df)
worksheets_append=pd.concat(worksheets,axis=0,ignore_index=False)
worksheets_append.to_excel('merged.xlsx',header=False,index=False)
