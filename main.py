from __future__ import print_function
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk, getopt, sys, argparse, pdfkit, time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint
from buildPDF import create_pdf

nltk.download('punkt')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

def search(keyword=None, datestart=None, dateend=None):
    #Parametros de busca
    print('Key: ', keyword)
    print('Date start: ', datestart)
    print('Date end: ', dateend)

    #Configuração da pesquisa
    googlenews = GoogleNews(start=datestart, end=dateend)
    googlenews.search(keyword)
    result = googlenews.result()

    #Passando os dados p/ um DataFrame
    df = pd.DataFrame(result)

    #Printando as 5 primeiras notícias
    print(df.head())

    #Pega um range de páginas obtidas do resultado acima
    for i in range(0,1):
        print('idx', i)
        googlenews.getpage(i)
        result = googlenews.result()
        df = pd.DataFrame(result)

    list = []

    print('idxs: ', df.index)

    formated_datestart = datestart.split("/")
    datestart_save = formated_datestart[0] + '-' + formated_datestart[1] + '-' + formated_datestart[2]

    formated_dateend = dateend.split("/")
    dateend_save = formated_dateend[0] + '-' + formated_dateend[1] + '-' + formated_dateend[2]

    #---Fazendo testes com arquivos de texto
    #txtfilename = "./txts/sumario.txt"
    #txt = open(txtfilename, 'w')

    for ind in df.index:
        if(ind < 2):
            print(ind)
            dict = {}
            article = Article(df['link'][ind],config=config)
            article.download()
            #try:
            article.parse()
            article.nlp()
            dict['Date'] = df['date'][ind]
            dict['Media'] = df['media'][ind]
            dict['Title'] = article.title
            dict['Article'] = article.text
            dict['Summary'] = article.summary
            list.append(dict)
            resumo = str(article.summary)
            create_pdf(df['date'][ind], df['media'][ind], article.title, resumo, ind)
            #except:
            #    print('error')
    #txt.close()

    #--------Convertendo o DataFrame pra um arquivo do Excel
    #news_df = pd.DataFrame(list)
    #news_df.to_excel("{}_{}_{}.xlsx".format(keyword, datestart_save, dateend_save))


if __name__ == '__main__':
    #Caso for testar o código na IDE, definir os parametros de busca aqui.
    keyword = 'NBA'
    initialdate = '10/12/2020'
    finaldate = '10/12/2020'

    #Pegando as informações da linha de comando (nao necessario caso for rodar direto na IDE)
    parser = argparse.ArgumentParser()
    parser.add_argument("-key", "--keyword", help="Database name")
    parser.add_argument("-dts", "--datestart", help="Initial Date")
    parser.add_argument("-dte", "--dateend", help="Final Date")

    if keyword == None and initialdate == None and finaldate == None:
        args = parser.parse_args()
        keyword = str(args.keyword)
        initialdate = str(args.datestart)
        finaldate = str(args.dateend)

    #Faz a busca pelas notícias
    search(keyword, initialdate, finaldate)
