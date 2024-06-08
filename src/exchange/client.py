import httpx

from src.exchange.exceptions import (
    InvalidResponseError,
    InvalidTokenError,
    NotAuthorizedOperationError,
)
from src.exchange.helper import cache
from src.settings import settings


class Client:
    """
    This is the client to Public APIs service, which return exchange rates
    """

    BASE_URL: str = "https://openexchangerates.org/api/latest.json"
    APIKEY: str = settings.EXCHANGE_SERVICE_APIKEY

    @property
    def client(self):
        return httpx.AsyncClient(timeout=5.0)

    @cache(seconds=60)
    async def rates(self, base: str) -> bytes:
        async with self.client as client:
            params = {
                "app_id": self.APIKEY,
                "base": base,
            }

            response = await client.get(url=self.BASE_URL, params=params)
            if not response.is_success:
                if response.status_code == 401:
                    raise InvalidTokenError()
                elif response.status_code == 403:
                    raise NotAuthorizedOperationError()
                raise InvalidResponseError(response.json())
            return response.content
