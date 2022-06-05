from loguru import logger
from bs4 import BeautifulSoup


def test_frontend_index_page_get_method(client):
    """
    Testing for basic index search page

    Testing for:
        - get request returning basic html with single search bar
        - has a form with button for submit
    """
    response = client.get("/")

    soup = BeautifulSoup(response.text, "html.parser")

    # Check if frontend get responds with 200
    assert response.status == "200 OK"

    # Check for basic navbar and html element
    assert soup.find("html") is not None
    assert soup.find("nav") is not None

    # Check for basic form and search button
    form = soup.find("form")
    assert form is not None
    assert form.button is not None


def test_frontend_search_page_get_method(client):
    """
    Test for search results page when retrieving search results

    Testing for:
        - get method without params
    """
    response = client.get("/search")

    assert response.status == "200 OK"

    # Check for basic html element
    assert soup.find("html") is not None


def test_frontend_search_page_spongebob(client):
    """
    Test for search term response with frontend search page

    Testing for:
        - get method with params
        - returning search results
        - correct search results with given search term
    """
    response = client.get("/search", params={"term": "spongebob"})

    assert response.status == '200 OK'

    # Check search results aren't empty
    assert soup.select('.search-result') is not None
