from fastapi import APIRouter, Depends
from starlette import status

from src.exchange.client import Client
from src.exchange.exceptions import ConvertOperationError
from src.exchange.schemas import ConverterResponse, ExchangeQuery, RatesAPIResponse
from src.exchange.utils import converter

router = APIRouter()


@router.get(
    "/rates",
    response_model=ConverterResponse,
    status_code=status.HTTP_200_OK,
)
async def rates_converter(
    query: ExchangeQuery = Depends(),
):
    client = Client()
    response: bytes = await client.rates(base=query.from_currency)
    exchange_rates = RatesAPIResponse.model_validate_json(response)

    if not (convert_rates := exchange_rates.rates.get(query.to_currency)):
        raise ConvertOperationError(
            "Convert to selected currency {} not supported!".format(query.to_currency)
        )

    converted_sum = await converter(convert_rates, query.value)
    return {
        "sum": converted_sum,
        "updated_at": exchange_rates.timestamp,
    }
