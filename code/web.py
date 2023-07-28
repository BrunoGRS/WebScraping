import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto = input('Qual produto você deseja pesquisar? ')

response = requests.get(url_base + produto)

produto_buscado = BeautifulSoup(response.text, 'html.parser')

resultados = produto_buscado.find_all('div', 
                                     attrs='ui-search-result__wrapper shops__result-wrapper')

for resultado in resultados:
    
    titulo = resultado.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})
    link = resultado.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})
    moeda = resultado.find('span', attrs={'class': 'andes-money-amount__currency-symbol'})
    preco_inteiro = resultado.find('span', attrs={'class': 'andes-money-amount__fraction'})
    preco_centavos = resultado.find('span', attrs={'class': 'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

    print('Nome do Produto ->', titulo.text)
    print('Link para Compra ->', link['href'])

    if (preco_centavos):
        print('Preço do produto ->' + moeda.text + ' ' + preco_inteiro.text + ',' + preco_centavos.text)
    else:
        print('Preço do produto ->' + moeda.text + ' ' + preco_inteiro.text)
        
    print()



    

