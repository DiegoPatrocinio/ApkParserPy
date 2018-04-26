FROM python:2.7.12-onbuild

RUN apt-get update
RUN apt-get install libssl-dev -y
RUN apt-get install swig -y
RUN pip install --global-option=build_ext --global-option="-I/usr/include/x86_64-linux-gnu" m2crypto
RUN pip install apk_parse_ph4

