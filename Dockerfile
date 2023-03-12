FROM python:alpine
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install datetime 
RUN pip install flask
# CMD ["source", "venv/bin/activate"]
CMD ["python", "main.py"]
