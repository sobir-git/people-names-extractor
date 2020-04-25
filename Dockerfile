FROM python:3.7

RUN pip3 install spacy  && \
    python3 -m spacy download en_core_web_sm

ADD ./* /app/
WORKDIR /app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "extract.py"]
