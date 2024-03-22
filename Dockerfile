# Final image
FROM python:3.9-alpine3.13
LABEL maintainer="hassan Salim"

#It's recommned when runing python in docker container. It tells python that you dont need to buffer the output
ENV PYTHONUNBOUFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

WORKDIR /app

EXPOSE 8000

# To install some dependancy in my machine (python image)
# 1) python -m -venv /py: Create new virtual envronnment  that we gonna to store our depondencies, just to avoid any conflection dependencies that may come in the base image that i am using
#2 ) /py/bin/pip install --upgrade pip, we specify the full path for our virtual environnment, so we wanna upgrade pipe, for the virtual environnement that we just created , so will upgrade the python package manager inside our environnment 
# 3) /py/bin/pip install -r /tmp/requirements.txt, to install this list of the requirement inside the docker image
# 4) rm -rf /tmp, then we remove the tmp, because we don't any extra dependecies in the image when our image once been crreated 
#5)  adduser \--disabled-password \--no-create-home \ django-user, this will call the commande adduser to add a new user inside our image, because it's best practeies not to use the root user , the root user is the user that has the full access, not recommende run the applicatio using root user, so we dont creat home r password for the user, finaly we give a name to our user (django)

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# ENV PATH="/py/bin:$PATH", to update the environment variable inside pur image, so the path is the envrionment variable that automatically create in linux operating system
ENV PATH="/py/bin:$PATH"


# This will specifies the user that we are we're wwitching to 
USER django-user
