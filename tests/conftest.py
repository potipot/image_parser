import pytest
from pathlib import Path


@pytest.fixture()
def value():
    return 5


@pytest.fixture(scope="session")
def data_dir():
    return Path(__file__).absolute().parent / "data"


@pytest.fixture()
def names_json_file(data_dir):
    return data_dir / 'label_names_test.json'


@pytest.fixture()
def ids_json_file(data_dir):
    return data_dir / 'label_ids_test.json'

