# vim:set ft=dockerfile:

####################
# Base image start #
####################

FROM debian:9.4-slim as BASE_IMAGE

LABEL maintainer="Roberto Rosario roberto.rosario@mayan-edms.com"

ENV PYTHONUNBUFFERED=1 \
    LC_ALL=C.UTF-8 \
    PROJECT_INSTALL_DIR=/opt/mayan-edms

# Install base Ubuntu libraries
RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev \
        g++ \
        gcc \
        ghostscript \
        gnupg1 \
        gpgv \
        graphviz \
        libffi-dev \
        libfuse2 \
        libjpeg-dev \
        libmagic1 \
        libpng-dev \
        libpq-dev \
        libreoffice \
        libssl-dev \
        libtiff-dev \
        poppler-utils \
        python-dev \
        python-setuptools \
        python-virtualenv \
        python-wheel \
        redis-server \
        sane-utils \
        sudo \
        supervisor \
        tesseract-ocr \
        zlib1g-dev \
 && apt-get clean autoclean \
 && apt-get autoremove --purge -y \
 && rm -rf /var/lib/apt/lists/* \
 && rm -f /var/cache/apt/archives/*.deb

RUN adduser mayan \
      --disabled-login \
      --disabled-password \
      --gecos "" \
      --no-create-home \
# Pillow can't find zlib or libjpeg on aarch64 (ODROID C2)
 && if [ "$(uname -m)" = "aarch64" ]; then \
         ln -s /usr/lib/aarch64-linux-gnu/libz.so /usr/lib/ \
      && ln -s /usr/lib/aarch64-linux-gnu/libjpeg.so /usr/lib/ \
    ; fi \
# Pillow can't find zlib or libjpeg on armv7l (ODROID HC1)
 && if [ "$(uname -m)" = "armv7l" ]; then \
         ln -s /usr/lib/arm-linux-gnueabihf/libz.so /usr/lib/ \
      && ln -s /usr/lib/arm-linux-gnueabihf/libjpeg.so /usr/lib/ \
    ; fi \
# Discard data when Redis runs out of memory
 && echo 'maxmemory-policy allkeys-lru' >> /etc/redis/redis.conf \
# Disable saving the Redis database
 && echo 'save ""' >> /etc/redis/redis.conf \
# Only provision 1 database
 && echo 'databases 1' >> /etc/redis/redis.conf

#####################
# Build image start #
#####################

FROM debian:9.4-slim as BUILDER_IMAGE

ENV LC_ALL=C.UTF-8

RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get update \
 && apt-get install -y \
      make \
      python-dev \
      python-pip

WORKDIR /code
COPY . /code

RUN pip install -r requirements/build.txt \
 && make wheel \
 && chmod -R 777 dist

#####################
# Final image start #
#####################

FROM BASE_IMAGE

RUN mkdir -p "${PROJECT_INSTALL_DIR}" \
 && chown -R mayan:mayan "${PROJECT_INSTALL_DIR}"

USER mayan
RUN python -m virtualenv "${PROJECT_INSTALL_DIR}" \
 && . "${PROJECT_INSTALL_DIR}/bin/activate" \
 && pip install --no-cache-dir --no-use-pep517 \
      librabbitmq==1.6.1 \
      mysql-python==1.2.5 \
      psycopg2==2.7.3.2 \
      redis==2.10.6

WORKDIR "${PROJECT_INSTALL_DIR}"

COPY --from=BUILDER_IMAGE --chown=mayan:mayan \
       /code/dist/*.whl \
       /code/contrib/scripts/docker/run-tests.sh \
       /code/docker/version \
       /code/requirements/testing-base.txt \
       ./

# Install build Mayan EDMS
RUN . "${PROJECT_INSTALL_DIR}/bin/activate" \
 && pip install --no-cache-dir --no-use-pep517 \
      *.whl

USER root

COPY docker/rootfs /

VOLUME ["/var/lib/mayan"]

ENTRYPOINT ["entrypoint.sh"]
CMD ["mayan"]
EXPOSE 8000

RUN find /var/log -type f | while read f; do echo -ne '' > $f; done;
