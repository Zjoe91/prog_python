"""
NOTICE:

You may want to run these tests to check your solution agains the expectation.
However, notice that when running they may modify the DB and subsequent runs MAY
FAIL.

You may want to revert the changes to flight_reservation.db after each run to
ensure this works as expected.
"""

import pytest
import requests

BASE_URL = "http://localhost:8080"  # Replace with your API base URL


def create_url(*parts):
    return "/".join([str(part) for part in parts])


def test_airports():
    endpoint = "airports"

    response = requests.get(create_url(BASE_URL, endpoint))
    json = response.json()
    assert response.status_code == 200
    assert isinstance(json, list)
    assert json[0]["code"] == "JFK"
    assert json[0]["id"] == 1


@pytest.mark.parametrize(
    "departure_airport, arrival_airport, expected_status_code",
    [
        ("JFK", "LHR", 200),
        ("LAX", "CDG", 200),
        ("MAD", "ACE", 404),
    ],
)
def test_flight_search(departure_airport, arrival_airport, expected_status_code):
    endpoint = "flights/search"
    params = {
        "departure_airport": departure_airport,
        "arrival_airport": arrival_airport,
    }
    response = requests.get(create_url(BASE_URL, endpoint), params=params)
    assert response.status_code == expected_status_code
    if response.status_code == 200:
        assert isinstance(response.json(), list)


@pytest.mark.parametrize(
    "airline, departure, arrival, departure_datetime, arrival_datetime, price, flight_id, expected_status_code",
    [
        (
            "American Airlines",
            "JFK",
            "LHR",
            "2024-03-15 08:00:00",
            "2024-03-15 11:00:00",
            "350.0",
            "1",
            200,
        ),
        (
            "",
            "",
            "",
            "",
            "",
            "",
            "666",
            404,
        ),
    ],
)
def test_flight_details(
    airline,
    departure,
    arrival,
    departure_datetime,
    arrival_datetime,
    price,
    flight_id,
    expected_status_code,
):
    endpoint = f"flights"
    response = requests.get(create_url(BASE_URL, endpoint, flight_id))
    assert response.status_code == expected_status_code
    if response.status_code == 200:
        assert response.json()["id"] == int(flight_id)
        assert response.json()["airline"] == airline
        assert response.json()["departure"] == departure
        assert response.json()["arrival"] == arrival
        assert response.json()["departure_datetime"] == departure_datetime
        assert response.json()["arrival_datetime"] == arrival_datetime
        assert response.json()["price"] == float(price)


@pytest.mark.parametrize(
    "airline_id, departure_airport_id, arrival_airport_id, departure_datetime, arrival_datetime, price, expected_status_code",
    [
        (1, 1, 2, "2024-03-15 08:00:00", "2024-03-15 11:00:00", 200, 201),
    ],
)
def test_create_flight(
    airline_id,
    departure_airport_id,
    arrival_airport_id,
    departure_datetime,
    arrival_datetime,
    price,
    expected_status_code,
):
    endpoint = "flights"
    data = {
        "airline_id": airline_id,
        "departure_airport_id": departure_airport_id,
        "arrival_airport_id": arrival_airport_id,
        "departure_datetime": departure_datetime,
        "arrival_datetime": arrival_datetime,
        "price": price,
    }
    response = requests.post(create_url(BASE_URL, endpoint), json=data)
    assert response.status_code == expected_status_code
    if response.status_code == 201:
        response = requests.get(
            create_url(BASE_URL, endpoint, str(response.json()["id"]))
        )
        assert response.status_code == 200



@pytest.mark.parametrize(
    "flight_id, passenger_name, passenger_email, num_tickets, expected_status_code",
    [
        (1, "John Smith", "john@example.com", 2, 201),
        (2, "Emma Johnson", "emma@example.com", 1, 201),
    ],
)
def test_flight_reservation(
    flight_id, passenger_name, passenger_email, num_tickets, expected_status_code
):
    endpoint = "reservations"
    data = {
        "flight_id": flight_id,
        "passenger_name": passenger_name,
        "passenger_email": passenger_email,
        "num_tickets": num_tickets,
    }
    response = requests.post(create_url(BASE_URL, endpoint), json=data)
    assert response.status_code == expected_status_code
    if response.status_code == 201:
        assert "id" in response.json()
        assert response.json()["flight_id"] == flight_id
        assert response.json()["passenger_name"] == passenger_name

        response = requests.get(create_url(BASE_URL, endpoint, response.json()["id"]))
        assert response.status_code == 201


if __name__ == "__main__":
    pytest.main()