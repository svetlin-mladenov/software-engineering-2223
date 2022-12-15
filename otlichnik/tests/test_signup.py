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


@pytest.mark.parametrize("email", [
    "hsafiuashfi@gmail.com",
    "name.name@gmail.com",
])
def test_email_validation_valid_email(email):
    assert email_validation(email)


@pytest.mark.parametrize("email", [
    "sidhiudshsweh",
    "",
    "sidhiudshsweh@",
    "@sidhiudshsweh",
    "name@gmail.",
    ".name@gmail.com",
    "name.@gmail.com",
    "name..name@gmail.com",
    "pesho@.@gmail.com",
    "pesho!!@gmail.com",
    "pesho+@gmail.com",
    "pesho-@gmail.com",
    "pesho-gosho@gmail.com",
])
def test_email_validation_invalid_email(email):
    assert not email_validation(email)


def test_request_invalid_email(client):
    response = client.post("/signup", data={
        "email": "mailmail.com",
        "password": "password",
    })
    assert response.status_code == 400
