from loguru import logger
from bs4 import BeautifulSoup
from flask import url_for
from flask.testing import FlaskClient


def test_frontend_index_page_get_method(client: FlaskClient) -> None:
    """
    Testing for basic index search page

    Testing for:
        - get request returning basic html with single search bar
        - has a form with button for submit
    """
    response = client.get(url_for("frontend.index"))

    soup = BeautifulSoup(response.text, "html.parser")

    # Check if frontend get responds with 200
    assert response.status == "200 OK"

    # Check for basic navbar and html element
    assert soup.find("html") is not None
    assert soup.find("nav") is not None

    # Check for basic form and search button
    form = soup.find("form")
    assert form is not None
    assert form.find("button") is not None


def test_index_search_button_links_to_search_page(client: FlaskClient) -> None:
    """
    Test for index page search button link

    Testing for:
     - search button link
    """
    response = client.get(url_for("frontend.index"))
    soup = BeautifulSoup(response.text, "html.parser")

    src_btn = soup.select("button#search")[0]
    assert src_btn is not None

    form = soup.find("form")
    assert form is not None
    assert form.attrs["action"] == url_for("frontend.search")


def test_frontend_search_page_get_method(client: FlaskClient) -> None:
    """
    Test for search results page when retrieving search results

    Testing for:
     - get method without params
    """
    response = client.get(url_for("frontend.search"))

    assert response.status == "302 FOUND"

    soup = BeautifulSoup(response.text, "html.parser")
    # Check for basic html element
    assert soup.find("html") is not None


def test_frontend_search_page_spongebob(client: FlaskClient,
                                        setup_spongebob_pages: int) -> None:
    """
    Test for search term response with frontend search page

    Testing for:
        - get method with params
        - returning search results
        - correct search results with given search term
    """
    num_of_inserted_pages = setup_spongebob_pages
    response = client.get(url_for("frontend.search", q="spongebob"))

    assert response.status == "200 OK"

    soup = BeautifulSoup(response.text, "html.parser")
    # Check search results aren't empty
    assert len(soup.select(".search-result")) == num_of_inserted_pages


def test_frontend_search_page_no_results(client: FlaskClient) -> None:
    """
    Test for search page with no results

    Testing for:
        - get method with params
        - returning no search results for given search term
    """
    response = client.get(url_for("frontend.search", q="patrick"))

    assert response.status == "200 OK"

    soup = BeautifulSoup(response.text, "html.parser")
    assert len(soup.select(".search-result")) == 0

def test_frontend_search_page_returns_search_page(client: FlaskClient) -> None:
    """
    Test for search page search button returns search page

    Testing for:
        - get method with params
        - check whether form is method get
        - check whether form is sending to search url
        - check whether input name is q
    """
    response = client.get(url_for('frontend.search', q='spongebob'))

    assert response.status == '200 OK'
    soup = BeautifulSoup(response.text, 'html.parser')

    # Checkt whether search page form returns correct urls
    form_el = soup.find('form')
    assert form_el.attrs.get('action') == url_for('frontend.search')
    assert form_el.attrs.get('method') == 'get'

    input_el = soup.find('form').find('input')
    assert input_el.attrs.get('name') == 'q'
