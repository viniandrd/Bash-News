import os
from datetime import date

def set_kw(kw):
    global kw_
    kw_ = kw

def get_folder():
    global kw_
    dir_name = os.getcwd()

    dir_name = os.path.join(str(dir_name), "news", kw_, str(date.today()))
    return dir_name

def check_path_news():
    global kw_
    dir_name = os.getcwd()
    #dir_name = os.path.join(str(dir_name), "PDFS")
    #if not os.path.exists(dir_name):
    #    os.mkdir(dir_name)


    dir_name = os.path.join(str(dir_name), "news")

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


    dir_name = os.path.join(str(dir_name), kw_)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

def create_folder():
    check_path_news()
    dir_name = get_folder()

    #cria a pasta caso ela ainda não exista
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print("Directory ", dir_name,  " Created ")
    else:
        print("teste")
