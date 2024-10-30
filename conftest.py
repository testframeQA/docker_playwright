import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--device-type",
        action="store",
        default="desktop", 
        help="Specify the device type: desktop or mobile"
    )

@pytest.fixture
def device_type(request):
    return request.config.getoption("--device-type")
