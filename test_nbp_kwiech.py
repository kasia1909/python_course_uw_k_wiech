
import nbp_change
import requests
import pytest

#mock
class MockResponse:


    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_courses(monkeypatch):


    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)


    result = nbp_change.get_courses('currency_code, days')


@pytest.fixture
def mock_test_database(monkeypatch):
    monkeypatch.setitem(nbp_change.calc_statistics(currency_list, days), "database", "test_db")