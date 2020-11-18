FROM python:3.7
 
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV DB_URI=${DB_URI} 

ENV KEY=${KEY}

ENTRYPOINT ["python", "app.py"]

