FROM  python:3.9
ENV PYTHONUNBUFFERED 1

COPY ./src/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /app

EXPOSE 6543
CMD python server.py