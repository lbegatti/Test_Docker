FROM python:3.9
# create a work directory in the base directory of the container
WORKDIR /code

# add the requirements.txt from the venv in the /code/ and you name them the same
# COPY ./SOURCE /DESTINATION
COPY ./requirements.txt /code/requirements.txt

# do not use cache with pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# 0.0.0.0 is the local host
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8080"]
