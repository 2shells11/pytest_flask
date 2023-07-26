import pytest
import requests
import os
import sys 
import platform
import sysconfig
from utils.config_files import *


@pytest.fixture(scope="session")
def setup():
    #bb=request.config.getoption(url_1)
    print("Doing setup")
    res=requests.get(getBooksurl())
    assert res.status_code == 200
    print("application is running")
    yield
    print("\nDoing teardown")
            
def pytest_configure(config):
    from pwd import getpwuid
    from os import getuid

    username = getpwuid(getuid())[0]
    
    from platform import python_version
    py_version = python_version()
    config._metadata = {
        "user_name": username,
        "python_version": py_version,
        "sys.platform" : sys.platform,
        "os.name"   : os.name,
        "platform.system" : platform.system(),
        "sysconfig" : sysconfig.get_platform(),
        "platform": platform.machine()
         
    }


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    from py.xml import html
    prefix.extend([html.h3("Generating pytest report")])
    summary.extend([html.h3("##########################")])
    postfix.extend([html.h3("GENERATING RESULTS")])


def pytest_html_report_title(report):
    report.title = "Test Run"

@pytest.fixture(scope="function")
def put_fixture():
    def put_request(ide):
        url2=getBookurl() +str(ide)
        response_put= requests.put(url2)
        return response_put
    return put_request

@pytest.fixture(scope="function")
def get_request_by_id_fixture():
    def get_by_id_request(ide):
        url1= getBookurl()+str(ide)
        response_get_by_id= requests.get(url1)
        return response_get_by_id
    return get_by_id_request

