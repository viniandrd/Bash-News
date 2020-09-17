from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk
import getopt, sys
import argparse
import pdfkit

nltk.download('punkt')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

def search(keyword=None, datestart=None, dateend=None):
    #Parametros
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
    for i in range(2,3):
        print(i)
        googlenews.getpage(i)
        result = googlenews.result()
        df = pd.DataFrame(result)

    list = []

    print('idxs: ', df.index)

    formated_datestart = datestart.split("/")
    datestart_save = formated_datestart[0] + '-' + formated_datestart[1] + '-' + formated_datestart[2]

    formated_dateend = dateend.split("/")
    dateend_save = formated_dateend[0] + '-' + formated_dateend[1] + '-' + formated_dateend[2]

    txt = open("{}_{}_{}.txt".format(keyword, datestart_save, dateend_save), 'a')

    for ind in df.index:
        print(ind)
        dict = {}
        article = Article(df['link'][ind],config=config)
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
            if(ind < 2):
                txt.write(article.title)
                txt.write(article.text)
                txt.write(article.summary)
                txt.write('\n')
                txt.write('EoA')
                txt.write('\n')

        except:
            print('error')
    txt.close()


    news_df = pd.DataFrame(list)


    news_df.to_excel("{}_{}_{}.xlsx".format(keyword, datestart_save, dateend_save))



if __name__ == '__main__':
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
    }
    #pdfkit.from_url('https://globoesporte.globo.com/basquete/nba/noticia/assistencia-magica-de-kawhi-e-recorde-pos-jordan-de-murray-os-destaques-de-domingo-na-nba.ghtml', 'teste.pdf', options=options)
    pdfkit.from_file('NBA_08-30-2020_08-31-2020.txt', 'teste.pdf')
    '''"#Pegando as informações da linha de comando (nao necessario caso for rodar direto na IDE)
    parser = argparse.ArgumentParser()
    parser.add_argument("-key", "--keyword", help="Database name")
    parser.add_argument("-dts", "--datestart", help="Initial Date")
    parser.add_argument("-dte", "--dateend", help="Final Date")

    args = parser.parse_args()
    keyword = str(args.keyword)
    initialdate = str(args.datestart)
    finaldate = str(args.dateend)
    search(keyword, initialdate, finaldate)'''