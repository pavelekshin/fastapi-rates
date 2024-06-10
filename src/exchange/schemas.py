import datetime
from decimal import Decimal
from typing import Annotated

from fastapi import Query
from pydantic import BaseModel, ConfigDict, Field, PlainSerializer
from pydantic_extra_types.currency_code import ISO4217

UTC = Annotated[
    datetime.datetime,
    PlainSerializer(lambda dt: dt.strftime("%Y-%m-%dT%H:%M:%S%z")),
]


class RatesAPIResponse(BaseModel):
    timestamp: int
    base: str
    rates: dict[str, Decimal]


class ExchangeQuery(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    from_currency: Annotated[
        ISO4217, Field(Query(description="from currency", alias="from", default="USD", example="USD"))
    ]
    to_currency: Annotated[
        ISO4217, Field(Query(..., description="to currency", alias="to", example="RUB"))
    ]
    value: Annotated[Decimal, Field(Query(..., description="value to exchange", example="1.5"))]


class ConverterResponse(BaseModel):
    sum: Decimal
    updated_at: UTC
