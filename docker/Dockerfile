FROM ghcr.io/osgeo/gdal:alpine-small-latest
RUN apk add --no-cache python3 py3-pip
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt
WORKDIR /app
