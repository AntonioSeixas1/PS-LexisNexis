import pandas as pd
import numpy as np

df = pd.read_csv('precoMedicamento.csv', decimal =',')
#df['PF Sem Impostos']=df['PF Sem Impostos'].str.replace(',','.')
#df = df.dtype = {'PF Sem Impostos' : float}

## Output file fields's name
print(df.columns)

## Highest factory price without taxes
'''
hp = np.array([0])
product_hp = np.array([])

for index, row in df.iterrows():
    if float(row['PF Sem Impostos']) == hp:
        np.append(hp,float(row['PF Sem Impostos']))
        np.append(product_hp,row['PRODUTO'])
    elif float(row['PF Sem Impostos']) > hp[0]:
        hp = np.array([float(row['PF Sem Impostos'])])
        product_hp = np.array([row['PRODUTO']])

print("Highest Price: ", hp)
print("Most expensive product: ", product_hp)
'''

## Types of products

types = ['']
#print(df['TIPO DE PRODUTO (STATUS DO PRODUTO)'])

for index, row in df.iterrows():
    for i in types:
        #print(row['TIPO DE PRODUTO (STATUS DO PRODUTO)'])
        if str(row['TIPO DE PRODUTO (STATUS DO PRODUTO)']) != str(i):
            types.append(str(row['TIPO DE PRODUTO (STATUS DO PRODUTO)']))
print(types)
