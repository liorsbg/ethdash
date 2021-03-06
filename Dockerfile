FROM python:3.6

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-W", "ignore", "-m", "ethdash.main"]