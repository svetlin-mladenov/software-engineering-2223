# pylint: disable=missing-function-docstring
import pytest
from otlichnik import *


@pytest.fixture
def app(tmp_path):
    app = create_app({
        "DATABASE": str(tmp_path / "otlichnik.db"),
    })
    with app.app_context():
        init_db()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_signup_get_page(client):
    response = client.get("/signup")
    assert response.status_code == 200


def test_signup_new_user(client):
    response = client.post("/signup", data={
        "email": "mail@mail.com",
        "password": "password",
    })
    assert response.headers["Location"] == "/"


def test_signup_existing_user(client):
    client.post("/signup", data={
        "email": "mail@mail.com",
        "password": "password",
    })
    response = client.post("/signup", data={
        "email": "mail@mail.com",
        "password": "password",
    })
    assert response.headers.get("Location") != "/"
    assert response.status_code == 400


def test_invalid_email():
    assert email_validation("hsafiuashfi@gmail.com")
    assert not email_validation("sidhiudshsweh")
    assert not email_validation("")
    assert not email_validation("sidhiudshsweh@")
    assert not email_validation("@sidhiudshsweh")


def test_request_invalid_email(client):
    response = client.post("/signup", data={
        "email": "mailmail.com",
        "password": "password",
    })
    assert response.status_code == 400
