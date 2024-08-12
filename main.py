import pandas as pd
df_new = pd.DataFrame({'name': ['sindhu','bindu','indhu']})
print(df_new.head())

from utils import add_column,remove_column,filter_rows,rename_columns,sum_column
df = add_column(df_new, 'age', [33,44,55])
df = add_column(df, 'gender', ['F','F',"F"])
df = add_column(df, 'salary', [33000,4500,45600])
print(df)

df = remove_column(df, 'salary')
print(df)

df = rename_columns(df,{'name':'fullname'})
print(df)

df = sum_column(df,'age')
print("sum of age:",df)

condition = lambda row:row['age']>40
df = filter_rows(df,condition)
print(df)

#pull operation

 
