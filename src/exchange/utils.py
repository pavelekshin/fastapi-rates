from decimal import ROUND_HALF_EVEN, Decimal


async def converter(rates: Decimal, value: Decimal):
    return (rates * value).quantize(Decimal("0.01"), ROUND_HALF_EVEN)
