# TEST for APP
import pytest
import requests 


# Function to Test if app is running
def test_app_running():
    url = 'http://127.0.0.1:5001/' # or http://localhost:5001/

    try:
        # try reaching the url and wait for 5s to get response
        response = requests.get(url, timeout=5)
        # assert response is 200
        assert response.status_code == 200

    except requests.exceptions.RequestException as e:
        pytest.fail(f'Application at {url} is NOT available. Error: {e}')