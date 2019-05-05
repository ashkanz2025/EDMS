# vim:set ft=dockerfile:

####################
# Base image start #
####################

FROM debian:9.4-slim as BASE_IMAGE

LABEL maintainer="Roberto Rosario roberto.rosario@mayan-edms.com"

ENV PYTHONUNBUFFERED=1 \
    LC_ALL=C.UTF-8 \
    PROJECT_INSTALL_DIR=/opt/mayan-edms

WORKDIR "${PROJECT_INSTALL_DIR}"

# Install base Ubuntu libraries
RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
        ghostscript \
        gnupg1 \
        gpgv \
        graphviz \
        libmagic1 \
        libreoffice \
        poppler-utils \
        python \
        python-setuptools \
        python-virtualenv \
        python-wheel \
        redis-server \
        sane-utils \
        sudo \
        supervisor \
        tesseract-ocr \
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

FROM BASE_IMAGE as BUILDER_IMAGE

RUN export DEBIAN_FRONTEND=noninteractive \
 && apt-get update \
 && apt-get install -y \
        default-libmysqlclient-dev \
        build-essential \
        libffi-dev \
        libfuse2 \
        libjpeg-dev \
        libpng-dev \
        libpq-dev \
        libssl-dev \
        libtiff-dev \
        python-dev \
        python-pip \
        zlib1g-dev

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

# Add all files, except the docker folder
#
# I know this is shit, but this is the only way to not invalidate the cache, when changing docker/*
# For god's sake, we don't have to care about the amount of layers in this build stage
# See also: https://github.com/moby/moby/issues/15771
COPY --chown=mayan:mayan \
       CONTRIBUTING.md \
       DCO \
       generate_setup.py \
       HISTORY_1_x.rst \
       HISTORY_2_x.rst \
       HISTORY.rst \
       increase_version.py \
       __init__.py \
       __init__.py.tmpl \
       LICENSE \
       Makefile \
       manage.py \
       MANIFEST.in \
       README.md \
       README.rst \
       removals.txt \
       requirements.txt \
       setup.cfg \
       setup.py \
       setup.py.tmpl \
       tox.ini \
       "${PROJECT_INSTALL_DIR}/"
COPY --chown=mayan:mayan "mayan"         "${PROJECT_INSTALL_DIR}/mayan"
COPY --chown=mayan:mayan "requirements"  "${PROJECT_INSTALL_DIR}/requirements"
COPY --chown=mayan:mayan "contrib"       "${PROJECT_INSTALL_DIR}/contrib"

RUN . "${PROJECT_INSTALL_DIR}/bin/activate" \
 && set -x \
 && pip install -r requirements/build.txt \
 && make wheel \
 && pip install --no-cache-dir --no-use-pep517 \
      dist/*.whl

RUN rm -r dist

#####################
# Final image start #
#####################

FROM BASE_IMAGE

COPY --from=BUILDER_IMAGE --chown=mayan:mayan "${PROJECT_INSTALL_DIR}/" "${PROJECT_INSTALL_DIR}/"

USER root

COPY docker/rootfs /

VOLUME ["/var/lib/mayan"]

ENTRYPOINT ["entrypoint.sh"]
CMD ["mayan"]
EXPOSE 8000

RUN find /var/log -type f | while read f; do echo -ne '' > $f; done;
