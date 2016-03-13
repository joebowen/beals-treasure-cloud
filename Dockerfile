FROM django:onbuild

RUN apt-get update
RUN apt-get -y install libgmp-dev
RUN pip install -r requirements2.txt