FROM python:3.8

WORKDIR /web

# Install fastapi & uvicorn
ADD requirements.txt .
RUN pip3 install -r requirements.txt

# Add code and run it
ADD . .
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]