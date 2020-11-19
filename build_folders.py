import os
from datetime import date

#print(date.today())
def createFolder():
    dirName = os.getcwd()
    dirName = str(dirName) + '/news/' + str(date.today())


    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:
        print("Teste")
