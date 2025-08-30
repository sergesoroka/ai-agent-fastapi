FROM python:latest

# create virtual environment
RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY requirements.txt /temp/requirements.txt
RUN pip install -r /temp/requirements.txt

COPY ./src .

CMD [ "python", "-m", "http.server", "8888" ]