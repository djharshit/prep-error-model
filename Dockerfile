FROM python

LABEL maintainer="Harshit M"

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 6060

CMD ["python", "server.py"]