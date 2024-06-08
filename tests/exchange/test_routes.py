import pytest
from async_asgi_testclient import TestClient
from fastapi import status

from tests.conftest import idtype


@pytest.mark.parametrize(
    "params",
    [
        {
            "from": "USD",
            "to": "USD",
            "value": 1,
        }
    ],
    ids=idtype,
)
async def test_rates(client: TestClient, params) -> None:
    resp = await client.get("/api/rates", query_string=params)
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_200_OK
    assert resp_json["sum"] == "1.00"


@pytest.mark.parametrize(
    "params",
    [
        {
            "from": "USD",
            "to": "USD",
        }
    ],
    ids=idtype,
)
async def test_rates_wo_value_in_params(client: TestClient, params) -> None:
    resp = await client.get("/api/rates", query_string=params)
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert resp_json["detail"] == [
        {
            "type": "missing",
            "loc": ["query", "value"],
            "msg": "Field required",
            "input": None,
        }
    ]


@pytest.mark.parametrize(
    "params",
    [
        {
            "from": "USD",
            "to": "XXX",
            "value": 1,
        }
    ],
    ids=idtype,
)
async def test_rates_w_wrong_currency(client: TestClient, params) -> None:
    resp = await client.get("/api/rates", query_string=params)
    resp_json = resp.json()

    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert (
        resp_json["error"]["error_detail"]
        == "Convert to selected currency XXX not supported!"
    )
