# Demo app
FastAPI

# Table of contents

1. [Setup](#setup)
2. [Swagger](#swagger)
3. [Logic](#logic)
4. [Todo](#todo)


## Setup

- Create [poetry](https://python-poetry.org/docs/#installation) environment (using [pyenv](https://github.com/pyenv/pyenv#installation) to manage python version)

```shell
poetry env use python
```
or specific version if you don't use pyenv


- Login to poetry shell

```shell
poetry shell
```

- Install dependencies

```shell
poetry install
```

- Copy .env.example and change value if needed

```shell
cp .env.example .env
```

- Develop using docker for environment consistency
```shell
docker-compose -f docker/dev.docker-compose.yml up -d
```

## Swagger

For a list of API endpoints navigate to [http://localhost:8000/docs](http://localhost:8000/docs)

## Logic

- Search employee at `/api/search`
- Need to get the configuration from `/api/config` before searching to get the list of fields to display

## Todo
- Add unit test
- Improve query logic (Update to Keyset pagination for large data set)
- Add authentication for user and define scope of access for the user
