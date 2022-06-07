from loguru import logger
from flask.testing import FlaskClient


def test_app_is_listening(client: FlaskClient):
    try:
        response = client.get("/")
    except Exception as exc:
        logger.debuge(exc)

    assert response.status == "200 OK"
    assert response.text.startswith("<!DOCTYPE html>")
    assert response.text.endswith("</html>")
