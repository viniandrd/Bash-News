from GoogleNews import GoogleNews
from newspaper import Article, Config
from buildPDF import create_pdf
from datetime import date
import pandas as pd
import nltk, argparse


nltk.download('punkt')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

def search(keyword=None, datestart=None, dateend=None):
    #Parametros de busca
    print('Keyword: ', keyword)

    #Configuração da pesquisa
    googlenews = GoogleNews(start=datestart, end=dateend)
    googlenews.setlang('pt')
    googlenews.search(keyword)
    result = googlenews.result()

    #Passando os dados p/ um DataFrame
    df = pd.DataFrame(result)

    #Printando as 5 primeiras notícias
    print(df.head())

    #Pega um range de páginas obtidas do resultado acima
    for i in range(0,1):
        googlenews.getpage(i)
        result = googlenews.result()
        df = pd.DataFrame(result)

    list = []

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
            list.append(dict)
            create_pdf(ind, list)
        except:
            print('Error')

    #--------Convertendo o DataFrame pra um arquivo do Excel
    #news_df = pd.DataFrame(list)
    #news_df.to_excel("{}_{}_{}.xlsx".format(keyword, datestart_save, dateend_save))


if __name__ == '__main__':
    # Pega a data atual para busca de notícias
    today = date.today()
    today = str(today)
    separa = today.split("-")
    dia = separa[2]
    mes = separa[1]
    ano = separa[0]
    data_atual = '{}/{}/{}'.format(mes, dia, ano)

    # Caso for testar o código na IDE, definir os parametros de busca aqui.
    keyword = 'Corona Virus'
    initialdate = data_atual
    finaldate = data_atual


    #Pegando as informações da linha de comando (nao necessario caso for rodar direto na IDE)
    parser = argparse.ArgumentParser()
    parser.add_argument("-key", "--keyword", help="Keyword")

    if keyword == None:
        args = parser.parse_args()
        keyword = str(args.keyword)

    #Faz a busca pelas notícias
    search(keyword, initialdate, finaldate)
