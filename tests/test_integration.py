import pytest
import requests
import subprocess
import time
import atexit

server = subprocess.Popen(['python3', 'app.py'])
time.sleep(1) # Server startup time. There's better ways to do this, but not easier.

def close_server():
    server.terminate()
    server.wait(10)
atexit.register(close_server)

# -----------------------------------------------------------------------------
# Endpoints that you need to implement
# -----------------------------------------------------------------------------

def test_get_wombats():
    '''
    You need to create the endpoint: GET /wombats

    It should produce a JSON response in the format: {
        "wombats": [
            { "id": 1, ... },
            ...
            { "id": n, ... },
        ]
    }

    This should reflect the current state of the wombat table.
    '''
    r = requests.get('http://localhost:8080/wombats')
    assert r.status_code == 200, r.text
    assert r.headers['content-type'].startswith('application/json')
    assert r.json() == {
        "wombats": [
            { "id": 1, "name": "Alice",  "dob": "1865-11-26" },
            { "id": 2, "name": "Queen",  "dob": "1951-07-26" },
            { "id": 3, "name": "Johnny", "dob": "2010-03-05" },
        ],
    }

def test_post_wombats():
    '''
    You need to create the endpoint: POST /wombats

    It should:

    1. Accept string arguments `name` and `dob`.
    2. Append a new row to the `wombat` table in the database.
    3. Produce a JSON response representing the newly created row:

        { "id": 4, "name": "Charlie", "dob": "2005-11-26" }

    Subsequent requests to the GET endpoint should show all added rows.
    '''
    def post(**kwargs):
        return requests.post('http://localhost:8080/wombats', data = kwargs)
    
    r = post()
    assert r.status_code == 400, r.text
    assert r.text == 'Missing parameter: name'

    r = post(name='Charlie')
    assert r.status_code == 400, r.text
    assert r.text == 'Missing parameter: dob'

    r = post(name='Charlie', dob='2005-11-26')
    assert r.status_code == 200, r.text
    assert r.headers['content-type'].startswith('application/json')
    assert r.json() == {
        "id": 4,
        "name": "Charlie",
        "dob": "2005-11-26"
    }
    
    # Check that it shows up in GET endpoint:
    r = requests.get('http://localhost:8080/wombats')
    assert r.json() == {
        "wombats": [
            { "id": 1, "name": "Alice",  "dob": "1865-11-26" },
            { "id": 2, "name": "Queen",  "dob": "1951-07-26" },
            { "id": 3, "name": "Johnny", "dob": "2010-03-05" },
            { "id": 4, "name": "Charlie", "dob": "2005-11-26" }
        ],
    }

@pytest.mark.parametrize('method', ['PUT', 'PATCH', 'DELETE', 'FARFAGNUGEN'])
def test_unsupported_methods(method):
    '''
    For other methods, the /wombats endpoint should respond with a 405 error.
    '''
    r = requests.request(method, 'http://localhost:8080/wombats')
    assert r.status_code == 405, r.text
    assert "Method Not Allowed" in r.text

# -----------------------------------------------------------------------------
# Starter behavior, that you just don't want to damage
# -----------------------------------------------------------------------------
def test_get_root():
    '''
    The root endpoint (GET /) should return a simple text response.
    '''
    r = requests.get('http://localhost:8080/')
    assert r.status_code == 200, r.text
    assert r.headers['content-type'].startswith('text/plain')
    assert r.text == 'Inspire Candidate Exercise'

def test_404():
    '''
    Other routes should result in 404 responses.
    '''
    r = requests.get('http://localhost:8080/nowhere')
    assert r.status_code == 404
