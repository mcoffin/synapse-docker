FROM alpine:3.5

RUN apk add --update ruby ruby-dev supervisor build-base zlib zlib-dev python py-pip haproxy git
RUN pip install pyyaml
# RUN gem install synapse --no-document
RUN mkdir -p /etc/smartstack/synapse/build
COPY . /etc/smartstack/synapse/build
WORKDIR /etc/smartstack/synapse/build/synapse
RUN gem build synapse.gemspec
RUN find . -mindepth 1 -maxdepth 1 -name 'synapse-*.gem' | xargs gem install --no-document
WORKDIR /

RUN mkdir -p /etc/smartstack/synapse
RUN rm /etc/haproxy/haproxy.cfg

COPY docker-entrypoint.py /docker-entrypoint.py
COPY supervisord.conf /etc/supervisord.conf

ENTRYPOINT ["/docker-entrypoint.py"]
CMD ["synapse"]
