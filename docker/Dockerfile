FROM continuumio/miniconda3:4.7.12

# python-blosc, cytoolz, lz4 and nomkl are optimization for low-level operations 
# http://python-blosc.blosc.org/intro.html#what-is-python-blosc
# https://pypi.org/project/cytoolz/
# https://github.com/lz4/lz4
# https://docs.anaconda.com/mkl-optimizations/

RUN conda install --yes \
    -c conda-forge \
    python-blosc \
    cytoolz \
    lz4 \
    nomkl \
    tini==0.18.0 \
    python=3.6.* \
    numpy=1.14.2 \
    pandas=0.22.* \
    fastavro=0.17.10 \
    python-confluent-kafka=1.1 \
    # pyyaml=3.12 \
    # requests=2.* \
    # openssl=* \
    # pip=9.0.1 \
    # pymysql=0.8.1 \
    # sqlalchemy=1.2.8 \
    # alembic=0.9.9 \
    jsonnet=0.11.2 \
    && conda clean -tipsy \
    && find /opt/conda/ -type f,l -name '*.a' -delete \
    && find /opt/conda/ -type f,l -name '*.pyc' -delete \
    && find /opt/conda/ -type f,l -name '*.js.map' -delete \
    # && find /opt/conda/lib/python*/site-packages/bokeh/server/static -type f,l -name '*.js' -not -name '*.min.js' -delete \
    && rm -rf /opt/conda/pkgs

COPY docker/prepare.sh /usr/bin/prepare.sh

RUN mkdir /opt/app; \
    chmod +x /usr/bin/prepare.sh

COPY src /opt/app/

ENTRYPOINT ["tini", "-g", "--", "/usr/bin/prepare.sh"]