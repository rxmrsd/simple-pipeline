##########################################
# base image
##########################################
FROM python:3.11.7-slim as base

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    # for install
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH /root/.local/bin:$PATH
RUN poetry config virtualenvs.create false

WORKDIR /workspace

COPY pyproject.toml ./components/display-component/poetry.lock ./components/display-component/dependencies.txt ./
RUN poetry export --without-hashes --with $(cat dependencies.txt) --output requirements.txt

##########################################
# production image for deploy
##########################################
FROM python:3.11.7-slim

ENV PYTHONUNBUFFERED True
ENV PYTHONPATH /workspace/src/:$PYTHONPATH

WORKDIR /workspace

RUN pip install --no-cache-dir --upgrade pip
COPY --from=base /workspace/requirements.txt ./
COPY ./components/display-component/src/ src/

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "src/main.py"]