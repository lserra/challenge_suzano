FROM python:3

LABEL maintainer="laercio.serra@gmail.com"
LABEL version="1.0"
LABEL description="Challenge for Data Engineer at SUZANO"

# set a directory for the app
WORKDIR /Users/lserra/PyProjects/challenge_suzano

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD ["bash", "start.sh"]