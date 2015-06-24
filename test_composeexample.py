import os

import pytest
import requests


@pytest.fixture
def docker_url():
    host = os.environ.get('DOCKER_IP', 'localhost')
    return 'http://{host}:8000/'.format(host=host)


def test_it_works(docker_url):
    assert requests.get(docker_url).status_code == 200
