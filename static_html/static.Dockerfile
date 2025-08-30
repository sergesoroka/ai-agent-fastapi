FROM python:latest

# docker build -f Dockerfile -t agent-app .
# docker run -it agent-app

WORKDIR /app

# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder

COPY ./src .

# RUN echo "hello" > index.html

# python -m http.server 8888
# docker run -it -p 8888:8888 agent-app
CMD [ "python", "-m", "http.server", "8888" ]