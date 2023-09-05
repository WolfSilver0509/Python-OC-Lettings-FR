###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.6-alpine as builder

# set work directory
WORKDIR /usr/src/appserveur

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \cd && apk add postgresql-dev gcc python3-dev musl-dev


# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/appserveur/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9.6-alpine

# create directory for the app user
RUN mkdir -p /home/appserveur

# create the app user
RUN addgroup -S appserveur && adduser -S appserveur -G appserveur

# create the appropriate directories
ENV HOME=/home/appserveur
ENV APP_HOME=/home/appserveur/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/appserveur/wheels /wheels
COPY --from=builder /usr/src/appserveur/requirements.txt .
RUN pip install --no-cache /wheels/*


# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R appserveur:appserveur $APP_HOME

# change to the app user
USER appserveur

# run entrypoint.prod.sh
#ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]