import pytest
import requests
from utils.config_files import *

# #from config_files import parse_ini_file
# # @pytest.fixture
# # def var(request):
# #     return request.config.getoption('book_url')
# from configparser import ConfigParser

# file = 'config.ini'
# config = ConfigParser()
# config.read(file)


# books_url = config['pytest']['url_2']
# book_url = config['pytest']['url_1']
# print(book_url)

@pytest.fixture(scope="session")
def setup():
    #bb=request.config.getoption(url_1)
    print("Doing setup")
    #bb=config.getoption('book_url')
    res=requests.get(getBooksurl())
    assert res.status_code == 200
    print("application is running")
    yield
    print("\nDoing teardown")
            


# @pytest.fixture(scope="function")
# def get_url_fixture():
#     def get_request():
#         response_get=requests.get(books_url)
#         return response_get
#     return get_request
    # def get_url_request(id2):
    #     url2= book_url+id2
    #     response_put= requests.put(url2)

    #     return response_put
    # return get_url_request



@pytest.fixture(scope="function")
def put_fixture():
    def put_request(id2):
        url2=getBookurl() +id2
        response_put= requests.put(url2)
        return response_put
    return put_request

@pytest.fixture(scope="function")
def get_request_by_id_fixture():
    def get_by_id_request(id1):
        url1= getBookurl()+id1
        response_get_by_id= requests.get(url1)
        return response_get_by_id
    return get_by_id_request

