import pytest
import json
import requests
import jsonpath
from utils.config_files import *
def test_setup(setup):
    print("Executing")

@pytest.mark.get
def test_get_request():
    response = requests.get(getBooksurl())
    print(response)
    print(response.text)
    json_response = json.loads(response.text)
    print(json_response)

# def test_get_request(get_url_fixture):
    
#     #url = "http://127.0.0.1:5000/books"
#     response = get_url_fixture()
#     print(response)
#     print(response.text)
#     json_response = json.loads(response.text)
#     print(json_response)


def test_get_request_by_id(get_request_by_id_fixture):
    id1 = input("enter id")
    response1= get_request_by_id_fixture(id1)
    print(response1)
    assert response1.status_code == 200
@pytest.mark.post
def test_post_request():
    response_post = requests.post(getBooksurl())
    print(response_post)
    assert response_post.status_code == 201


def test_put_request(put_fixture):
    id2 = input("enter id")
    response_putt= put_fixture(id2)
    print(response_putt)
    assert response_putt.status_code == 200

def test_delete_request(put_fixture):
    id3 = input("enter id")
    #url3= getBookurl()+id3
    response_del= requests.delete(getBookurl()+id3)
    print(response_del)
    assert response_del.status_code == 200