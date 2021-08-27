import pandas as pd
import numpy as np


## prints Highest factory price without taxes
def get_highest_factory_price(df):
    df = df.drop_duplicates(subset = ['PRODUTO'])
    hp = 0
    product_hp = np.array([])
    for index, row in df.iterrows():
        if float(row['PF Sem Impostos']) == hp:
            product_hp = np.append(product_hp,row['PRODUTO'])
        elif float(row['PF Sem Impostos']) > hp:
            hp = float(row['PF Sem Impostos'])
            product_hp = np.array([row['PRODUTO']])

    print("\nMaior preço: ", hp)
    print("\nProdduto mais caro: ", product_hp)


##  prints Types of products
def get_types_of_products(df):
    df2 = df.drop_duplicates(subset = ['TIPO DE PRODUTO (STATUS DO PRODUTO)'])
    print("\nOs tipos de produto são: ", df2['TIPO DE PRODUTO (STATUS DO PRODUTO)'].drop(index = 7776).to_numpy())


# Prints Most cheap generic product
def get_most_cheap_generic_product(df):
    df3 = df[df.PRODUTO == df.SUBSTÂNCIA]
    name_cheapest_generic = df3['PRODUTO'].to_numpy()[1]
    price_cheapest_generic = df3['PF Sem Impostos'].to_numpy()[1]
    for index, row in df3.iterrows():
        if float(row['PF Sem Impostos']) < price_cheapest_generic:
            price_cheapest_generic = float(row['PF Sem Impostos'])
            name_cheapest_generic = row['PRODUTO']
    print ("\nO generico mais barato é: ", name_cheapest_generic)
    print("\nSeu preço é: ", price_cheapest_generic)

def get_quantity_of_diferent_products(df):
    df2 = df.drop_duplicates(subset = ['PRODUTO'])
    print("\nO número de tipos diferentes de produto são: ", len(df2['PRODUTO']))

## Prints if is there any product from differenst data frame with the same substance
def is_there_product_with_same_substance(df1, df2):
    df1_temp = df1.drop_duplicates(subset = ['SUBSTÂNCIA'])
    df1_temp['PF Sem Impostos'] = pd.to_numeric(df1_temp['PF Sem Impostos'])
    df1_temp = df1_temp[df1_temp['PF Sem Impostos'] < 100.0]
    df2_temp = df2.drop_duplicates(subset = ['SUBSTÂNCIA'])
    condition = False
    for index1, row1 in df1_temp.iterrows():
        if condition:
            print("\nExiste um produto que possua a mesma substância de um outro produto do arquivo original com preço final sem impostos inferior a 100")
            break
        for index2, row2 in df2_temp.iterrows():
            if row1['SUBSTÂNCIA'] == row2['SUBSTÂNCIA']:
                condition = True
                break
    if not(condition):
        print("\nNão existe um produto que possua a mesma substância de um outro produto do arquivo original com preço final sem impostos inferior a 100")

''' Debug Functions

def get_answer_2020(df):
    df2 = df.drop_duplicates(subset = ['COMERCIALIZAÇÃO 2020'])
    print("\nRespostas da comercialização 2020: ", df2['COMERCIALIZAÇÃO 2020'].to_numpy())

def get_answer_tarja(df):
    df2 = df.drop_duplicates(subset = ['TARJA'])
    print("\nRespostas da Tarja: ", df2['TARJA'].to_numpy())
'''




def main():

    ## Reading precoMedicamento.csv file
    df = pd.read_csv('precoMedicamento.csv', decimal =',')

    ### Creating new output.csv

    ## Treating pattern in name "Tarja Vermelha"
    df.loc[(df['TARJA'] ==  "Tarja  Vermelha") | (df['TARJA'] ==  "Tarja Vermelha(*)") | (df['TARJA'] == "Tarja Vermelha (*)") , 'TARJA'] = "Tarja Vermelha"

    #df[(df['PF Sem Impostos'] > 100.0) & (df['TARJA'] == "Tarja Vermelha") & (df['COMERCIALIZAÇÃO 2020'] == "Sim")].to_csv(r'C:\Users\anton\OneDrive\Documentos\LexisNexis\PS-LexisNexis\firstTask\output.csv', index = False)

    ## reading and treating new csv file

    new_df = pd.read_csv('output.csv', decimal = ',')

    new_df = new_df.sort_values('PRODUTO')

    # descomentar caso queira
    # Lembrar de mudar o caminho
    #new_df.to_csv(r'C:\Users\anton\OneDrive\Documentos\LexisNexis\PS-LexisNexis\firstTask\output.csv', index = False)

    new_df['PF Sem Impostos'] = pd.to_numeric(new_df['PF Sem Impostos'])
    
    print("Olá! Bem vindo a solução da atividade proposta pela LexisNexis")
    while True:
        selection = int(input("\nInsira de 1 a 7 qual item deseja visualizar a resposta: "))
        if selection == 1: 
            print("Os nomes dos respectivos campos são: ", df.columns)
        elif selection == 2:
            get_highest_factory_price(df)
        elif selection == 3:
            get_types_of_products(df)
        elif selection == 4:
            get_most_cheap_generic_product(df)
        elif selection == 5:
            print("\nA soma de todos os preços sem imposto, a partir do novo arquivo, é: ", new_df['PF Sem Impostos'].sum())
        elif selection == 6:
            get_quantity_of_diferent_products(new_df)
        elif selection == 7:
            is_there_product_with_same_substance(df, new_df)
        else:
            print("\nInsira um valor válido")
        

# Função main
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBoa sorte na próxima vez!")