# pylint: disable=missing-function-docstring
import pytest
from otlichnik import (
    create_app, init_db, password_validation, email_validation
)


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
    "name@r1-eu.p6-site.com",
    "pesho@ip127.a.c.d.abv.bg",
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
    "pesho@gosho@gmail.com",
    "__pesho@abv.bg",
    "___-@abv.bg",
])
def test_email_validation_invalid_email(email):
    assert not email_validation(email)


def test_request_invalid_email(client):
    response = client.post("/signup", data={
        "email": "mailmail.com",
        "password": "password",
    })
    assert response.status_code == 400


@pytest.mark.parametrize("password", [
    "a",
    "",
    "aA1#$",
    "aA11111111111111111111111",
    "aA####################",
    "a1$assssssssssssgg",
    "A1%AGJKMDSGSIDNFGSDIGN",
    "AAAaaa12*&^()&$#ufAd04AdjsgojsndsonginerofdANg3insvomecum" * 10,
    " ",
    "AAAAAAAAAAAAAAAAAAAAA",
    "111111111111111111111111",
    "^^^^^^^^^^^^^^^^^^^^^^^^^^",
    "aaaaaaaaaaaaaaaaaaaaaaaaaaa",
])
def test_password_validation_invalid_password(password):
    assert not password_validation(password)


@pytest.mark.parametrize("password", [
    "anG3i@@@LLLLLLLL@J4M3sCh4rl3s",
    "r3gEXSGaYge!!!!!",
    "8aA#8aA#8aA*8aaaaaaaa",
    "AAAAAAAaAAAAA4UGH$4",
    "mangalmanganovmanganovanganovalkanoV#3",
    "stringString0vStringcHov@StrivoIvongStringchovcong3",
    "NIKSATa3333333333333333333333###3#333333",
    "lowercaseUPPERCASE1234567890!@#$%^&*()QWERTYUIOPAASDFGHJKLZXCVBNM;",
    "HEEhe3#HEEHAWWWWGRRRRRRRRRRRRRR",
    "_a-A#3as______ASF",
    "mkaao@TRWAS(jf323412323t",
])
def test_password_validation_valid_password(password):
    assert password_validation(password)
