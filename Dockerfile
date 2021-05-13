FROM python:3.7
WORKDIR /FastApi
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "15400"]