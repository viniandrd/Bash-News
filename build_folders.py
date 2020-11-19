import os
from datetime import date

def get_folder():
    dir_name = os.getcwd()

    dir_name = os.path.join(str(dir_name), "PDFS", "news", str(date.today()))
    return dir_name

def check_path_news():
    dir_name = os.getcwd()
    dir_name = os.path.join(str(dir_name), "PDFS")
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        #print("Directory ", dir_name,  " Created ")

    dir_name = os.path.join(str(dir_name), "news")

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        #print("Directory ", dir_name,  " Created ")

def create_folder():
    check_path_news()
    dir_name = get_folder()

    #cria a pasta caso ela ainda não exista
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("Directory ", dir_name,  " Created ")
    else:
        print("teste")

