FROM python:3.12-alpine as bigimage
COPY ./app ./app

RUN pip wheel --wheel-dir=/root/wheels -r ./app/requirements.txt
FROM python:3.12-alpine as smallimage
COPY --from=bigimage /root/wheels /root/wheels
COPY ./app ./app
RUN pip install \
    --no-index \
    --find-links=/root/wheels --no-cache-dir -r ./app/requirements.txt
ENV PYTHONUNBUFFERED 1
COPY ./app ./app