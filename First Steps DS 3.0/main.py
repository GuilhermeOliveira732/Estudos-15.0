import pandas as pd
import sqlite3
import matplotlib
import matplotlib.pyplot as plt
import numpy

# lendo o arquivo xls
df = pd.read_excel(r"C:\Users\guiga\Desktop\Pasta\Superstore.xlsx")
print(df.dtypes)

# verificando a cidade com maior valor de vendas de produtos na
# categoria "Office Supplies"
df1 = df[['City', 'Category', 'Sales']]
office_sup = df1.loc[df1['Category'] == 'Office Supplies'].groupby('City')['Sales'].sum().reset_index(name='Vendas Cidades')

# printa na tela o resultado com a cidade com maior número de vendas
# de artigos do tipo "Office Supplies"
print('A cidade que mais vendeu foi: ')
print(office_sup.sort_values(by='Vendas Cidades', ascending=False).head(1))
print('*'*100)

# procurar o total de vendas por data do pedido,
# fazer um gráfico de barras com tal informação
df2 = df[['Order Date', 'Sales']]
venda_data = df2.groupby('Order Date')['Sales'].sum().reset_index(name='Vendas Período')
print('Vendas totais por data:')
print(venda_data)
print('*'*100)

plt.bar(venda_data['Order Date'], venda_data['Vendas Período'])
plt.title('Vendas totais por data')
plt.ylabel('Vendas Totais')
plt.xlabel('Data')
plt.show()

# procurar total de vendas por estado e fazer um gráfico de barras
# com tal informação
df3 = df[['State', 'Sales']]
venda_estado = df3.groupby('State')['Sales'].sum().reset_index(name='Vendas Estado')
print('Vendas totais por estado')
print(venda_estado)
print('*'*100)

plt.bar(venda_estado['State'], venda_estado['Vendas Estado'])
plt.xticks(rotation=80)
plt.title('Vendas totais por estado:')
plt.ylabel('Vendas Totais')
plt.xlabel('Estado')
plt.show()

# procurar as 10 cidades com maior total de vendas
# demonstrar o resultado com um gráfico de barras
df4 = df[['City', 'Sales']]
venda_cidade = df4.groupby('City')['Sales'].sum().reset_index(name='Vendas Cidade').sort_values(by='Vendas Cidade', ascending=False).head(10)
print('Vendas totais por cidade (10 primeiras)')
print(venda_cidade)

plt.bar(venda_cidade['City'], venda_cidade['Vendas Cidade'])
plt.xticks(rotation=80)
plt.title('Vendas totais por cidade (10 primeiras)')
plt.ylabel('Vendas Totais')
plt.xlabel('cidade')
plt.show()

# procurar o segmento que apresentou maior total de vendas
# demostrar através de um gráfico de pizza
df5 = df[['Segment', 'Sales']]
venda_categoria = df5.groupby('Segment')['Sales'].sum().reset_index(name='Vendas Categoria').sort_values(by='Vendas Categoria', ascending=False)
print('Vendas totais por categoria')
#print(round(venda_categoria))

# faz com que o valor não seja mostrado em notação científica
pd.set_option('display.float_format', lambda x: '%.3f' % x)
print(venda_categoria)


plt.pie(venda_categoria['Vendas Categoria'], labels=venda_categoria['Segment'], autopct='%1.1f%%')
plt.show()

# procurar o total de vendas por ano
# primeiro verificando os anos os quais o dataframe abrange
anos = df['Order Date'].apply(lambda x: x.year).unique()
anos.sort()
print('Anos os quais o DF abrange: ', anos)

# verificando o total de vendas por segmento e por ano (2014, 2015, 2016 e 2017)
for ano in anos:
    for segment in df['Segment'].unique():
        vendas_ano = df.loc[(df['Order Date'].dt.year == ano) & (df['Segment'] == segment), 'Sales'].sum()
        print('*'*100)
        print(ano)
        print(segment)
        print(vendas_ano)
print('*'*100)

'''df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
print(df.dtypes)
df['anos'] = df['Order Date'].dt.year
print(df.head())

df6 = df.groupby(['anos', 'Segment'])['Sales'].sum()
print(df6)'''


# simulação de quantas vendas receberiam 15% de desconto caso
# Valor_Venda for maior do que 1000 receber 15% de desconto
df6 = df['Sales']
itens15 = []
itens10 = []

for item in df6:
    if item > 1000:
        itens15.append(item)
    elif item < 1000:
        itens10.append(item)

print(len(itens15))
print(len(itens10))
print(len(df6))

# outra maneira de fazer o exercício anterior seria usando a
# seguinte linha de de código:
# df['Discount'] = np.where(df['Sales'] > 1000, 0.15, 0.10)
# efetivamente, o bloco de código feito, faz o mesmo que essa linha


# calculando a média do valor de venda antes do desconto
print('*'*100)
print('Média: ')
print(df6.mean())

# calculando a média com o desconto de 15% para vendas acima de 1000
vendas_desc = []
for item in df6:
    if item > 1000:
        vendas_desc.append(item*0.85)
    else:
        vendas_desc.append(item)
print('Média após aplicação do desconto de 15% para vendas acima de 1000:')
print(numpy.mean(vendas_desc))
print('*'*100)

# calculando a média de vendas por segmento, por ano e por mês
# demostrando através de um gráfico
segmentos = df['Segment'].unique()
anos = df['Order Date'].apply(lambda x: x.year).unique()
print('Anos os quais o DF abrange: ', anos)
print('Segmentos: ', segmentos)
print('*'*100)

# verificando o total de vendas por segmento e por ano (2014, 2015, 2016 e 2017)
# criando listas vazias para armazenar as informações a serem usadas pelos gráficos
cat_consumer = []
cat_corporate = []
cat_HO = []

for ano in anos:
    for segmento in segmentos:
        if segmento == 'Consumer':
            filtragem = df.loc[(df['Order Date'].dt.year == ano) & (df['Segment'] == 'Consumer')]
            vendas_ano = filtragem['Sales'].mean().round()
            cat_consumer.append(vendas_ano)

        elif segmento == 'Corporate':
            filtragem = df.loc[(df['Order Date'].dt.year == ano) & (df['Segment'] == 'Corporate')]
            vendas_ano = filtragem['Sales'].mean().round()
            cat_corporate.append(vendas_ano)

        elif segmento == 'Home Office':
            filtragem = df.loc[(df['Order Date'].dt.year == ano) & (df['Segment'] == 'Home Office')]
            vendas_ano = filtragem['Sales'].mean().round()
            cat_HO.append(vendas_ano)
#print('*'*100)

# criando listas para ordenar os valores de cada item
novaCons = dict(zip(anos, cat_consumer))
novaCons = dict(sorted(novaCons.items()))
novaCorp = dict(zip(anos, cat_corporate))
novaCorp = dict(sorted(novaCorp.items()))
novaHO = dict(zip(anos, cat_HO))
novaHO = dict(sorted(novaHO.items()))

# plotando as informações de média de vendas por ano por categoria no gráfico
plt.plot(novaCons.keys(), novaCons.values(), label='Consumer')
plt.plot(novaHO.keys(), novaHO.values(), label='Home Office')
plt.plot(novaCorp.keys(), novaCorp.values(), label='Corporate')
plt.title("Média de vendas por ano por segmento:")
plt.xlabel("Categorias")
plt.ylabel("Média")
plt.legend()
plt.show()