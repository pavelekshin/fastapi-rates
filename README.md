# FastAPI RESTAPI Example Project

- well-structured easy to understand and scale-up project structure

```bash
.
├── Dockerfile
├── README.md
├── docker-compose.yml
├── logging.ini
├── requirements.txt
├── ruff.toml
├── pytest.ini
├── .env.example
├── tests                         - tests
│   ├──  __init__.py
│   ├── conftest.py
│   └── exchange                  - testing module
├── scripts                       - scripts
│   └── start-dev.sh
└── src                           - global staff
    ├── __init__.py
    ├── config.py                      
    ├── constants.py              - constants
    ├── exception_handlers.py     - exception_handlers
    ├── exceptions.py             - exceptions
    ├── main.py                   
    ├── redis.py                  - redis query
    ├── settings.py               
    └── exchange                  - exchange app
        ├── __init__.py
        ├── client.py             - client
        ├── constants.py          
        ├── exceptions.py         
        ├── helper.py             - helper func
        ├── router.py             
        ├── schemas.py            - pydantic schemas            
        └── utils.py            

```

> [!CAUTION]
> External API for rates - https://openexchangerates.org/ \
> Changing the base currency is available only for paid plans.
> Free plan support only USD base

> [!NOTE]
> The "from" - query parameter by default assigned to "USD"

> [!NOTE]
> Pydantic attempts to convert the value to a string, then passes the string to Decimal(v)

- async IO operations
- easy local development
    - Dockerfile optimized for small size and fast builds with a non-root user
    - Docker-compose for easy deployment
    - environment with configured Redis cache
- redis cache
- pydantic model
- decimal in rates calculation
- pytest
- linters / format with ruff
- global custom exceptions

## Local Development

### First Build Only

1. `cp .env.example .env`
2. `docker network create app_exchange`
3. `docker-compose up -d --build`

### Swagger UI

```shell
http://localhost:17000/docs
```

### Query example

```shell
curl -X GET "http://127.0.0.1:17000/api/rates?from=USD&to=RUB&value=1"

or

curl -X GET "http://127.0.0.1:17000/api/rates?to=RUB&value=1"

```

### Run tests

```shell
docker compose exec app pytest -v
```