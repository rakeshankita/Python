import pandas as pd

excel1='Book1.xlsx'
excel2='Book2.xlsx'

df1=pd.read_excel(excel1)
df2=pd.read_excel(excel2)

values1 = df1[['Name','Country','Account','Grade']]
values2= df2[['Name','Country','Account','Grade']]


final=[values1,values2]

combo= pd.concat(final)

combo.to_excel('out.xlsx')
print(combo)


