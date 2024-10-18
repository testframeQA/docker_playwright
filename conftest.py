import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--device-type",
        action="store",
        default="desktop",  # default to desktop
        help="Specify the device type: desktop or mobile"
    )
    '''
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",  # default to chromium
        help="Specify the browser: chromium, firefox, or webkit"
    )
    '''

@pytest.fixture
def device_type(request):
    return request.config.getoption("--device-type")
'''
@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")
    '''