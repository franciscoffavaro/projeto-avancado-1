## BUILDING
##   (from project root directory)
##   $ docker build -t python-for-franciscoffavaro-findplace .
##
## RUNNING
##   $ docker run python-for-franciscoffavaro-findplace

FROM gcr.io/stacksmith-images/minideb-buildpack:jessie-r8

MAINTAINER Bitnami <containers@bitnami.com>

ENV STACKSMITH_STACK_ID="mvy5jdl" \
    STACKSMITH_STACK_NAME="Python for franciscoffavaro/findplace" \
    STACKSMITH_STACK_PRIVATE="1"

# Install required system packages
RUN install_packages libc6 libssl1.0.0 libffi6 libncurses5 libtinfo5 zlib1g libreadline6 libsqlite3-0

RUN bitnami-pkg install python-3.6.0-0 --checksum 44db2c169a8eb6ae3c64649c811a285f232d24f9e4773b81b0af57d151e45d63

ENV PATH=/opt/bitnami/python/bin:$PATH

## STACKSMITH-END: Modifications below this line will be unchanged when regenerating

# Django template
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
