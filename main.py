from GoogleNews import GoogleNews
from newspaper import Article, Config
from build_pdf import create_pdf
from datetime import date
import pandas as pd
import nltk, argparse
from threading import Thread
import time
import build_folders as bf
nltk.download('punkt')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

# Variáveis globais
initialdate = None
finaldate = None
noticias = []
cont = 0


def search(keyword=None, datestart=None, dateend=None, pgs = 1):
    # Variáveis globais
    global noticias
    global cont
    global acabou

    # Parametros de busca
    print('Keyword: ', keyword)

    #Configuração da pesquisa
    googlenews = GoogleNews(start=datestart, end=dateend)
    googlenews.setlang('pt')
    googlenews.search(keyword)
    result = googlenews.result()

    # Passando os dados p/ um DataFrame
    df = pd.DataFrame(result)

    # Printando as 5 primeiras notícias
    print(df.head())

    # Pega um range de páginas obtidas do resultado acima
    for i in range(0,pgs):
        googlenews.getpage(i)
        result = googlenews.result()
        df = pd.DataFrame(result)

    # Converte o DataFrame acima para uma lista de dicionários
    for ind in df.index:
        print('Noticia numero: {}'.format(ind))
        dict = {}
        article = Article(df['link'][ind], config=config)
        article.download()
        try:
            article.parse()
            article.nlp()
            dict['Date'] = df['date'][ind]
            dict['Media'] = df['media'][ind]
            dict['Title'] = article.title
            dict['Article'] = article.text
            dict['Summary'] = article.summary
            dict['Created'] = False
            noticias.append(dict)
        except:
            print('Error')
        time.sleep(0)

def get_current_date():
    # Variáveis globais
    global initialdate
    global finaldate

    # Pega a data atual para busca de notícias
    today = date.today()
    today = str(today)
    separa = today.split("-")
    dia = separa[2]
    mes = separa[1]
    ano = separa[0]
    data_atual = '{}/{}/{}'.format(mes, dia, ano)

    # Caso for testar o código na IDE, definir os parametros de busca aqui.

    initialdate = data_atual
    finaldate = data_atual


def call_create_pdf(list):
    global noticias
    global cont

    for noticia in list:
        ind = noticias.index(noticia)
        create_pdf(cont, noticia)
        cont += 1
        time.sleep(0)
    #print('Tempo de execução com threads: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    #criação da pasta do dia


    start_time = time.time()
    # Variáveis globais
    #global noticias
    #global cont

    keyword = None
    qtd_paginas = None
    get_current_date()

    #Pegando as informações da linha de comando (nao necessario caso for rodar direto na IDE)
    parser = argparse.ArgumentParser()
    parser.add_argument("-key", "--keyword", help="Keyword")
    parser.add_argument("-pg", "--pages", help="Pages")
    if keyword == None:
        args = parser.parse_args()
        keyword = str(args.keyword)
        qtd_paginas = int(args.pages)

    bf.set_kw(keyword)
    bf.create_folder()

    #Faz a busca pelas notícias
    search(keyword, initialdate, finaldate, qtd_paginas)

    tamanho = len(noticias)
    metade = tamanho // 2

    primeira_metade = noticias[:metade]
    segunda_metade = noticias[metade:]

    print(len(primeira_metade))
    print(len(segunda_metade))

    th_create = Thread(target=call_create_pdf, args=[primeira_metade])
    th2_create = Thread(target=call_create_pdf, args=[segunda_metade])

    th_create.start()
    th2_create.start()

    #print('Tempo de execução com threads: {}'.format(time.time() - start_time))