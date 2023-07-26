import configparser
from pathlib import Path

cfgFile = 'config.ini'
cfgFileDirectory = 'config'

config = configparser.ConfigParser()
BASE_DIR =Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(cfgFile)

config.read(CONFIG_FILE)

def getBookurl():
    return(config['pytest']['url_1'])

def getBooksurl():
    return(config['pytest']['url_2'])




# file = 'config.ini'
# config = ConfigParser()
# config.read(file)


# books_url = config['pytest']['url_2']
# book_url = config['pytest']['url_1']
#x= input("enter")
#print(book_url+x)