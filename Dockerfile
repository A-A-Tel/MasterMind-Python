FROM ubuntu:latest

# init env for debug
ARG debug
ENV DEBUG_PASS=${debug}

RUN apt update && apt-get -y -q install python3
RUN mkdir \usr\games\master_mind