FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y mc \
    && rm -rf /var/lib/apt/lists/*

CMD ["mc"]
