#Use Node LTS image
FROM python:3.11-slim

#Set working directory
WORKDIR /usr/src/app

#Install Dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

#Copy app code
COPY . . 

#Expose port 80 inside container
EXPOSE 80 

#Run FastAPI with Uvicorn (adjust if using Flask + Gunicor)
CMD ["uvicorn" , "main:app", "--host", "0.0.0.0", "--port", "80"]