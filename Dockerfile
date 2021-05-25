# Dockerfile
# pull official base image
FROM python:3.8.9
# accept arguments
ARG PIP_REQUIREMENTS=production.txt
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN echo ${DJANGO_SECRET_KEY}


# install dependencies
RUN pip install --upgrade pip setuptools wheel
# create user for the Django project
RUN useradd -ms /bin/bash project
# set current user
USER project
# set work directory
WORKDIR /home/project
# create and activate virtual environment
RUN python3 -m venv venv

RUN ./venv/bin/python3 -m pip install pip setuptools wheel --upgrade

# copy and install pip requirements
COPY --chown=project ./src/backend/requirements/ /home/project/requirements/
RUN ./venv/bin/pip3 install -r /home/project/requirements/${PIP_REQUIREMENTS}
# copy Django project files
COPY --chown=project ./src/backend/ /home/project/
# RUN ./venv/bin/python3 manage.py migrate
# RUN ./venv/bin/python3 manage.py collectstatic
