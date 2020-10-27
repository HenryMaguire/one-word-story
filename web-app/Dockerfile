# Pull a pre-built alpine docker image with nginx and python3 installed
#FROM tiangolo/uwsgi-nginx-flask:python3.7
FROM python:3.7.7

#COPY nginx.conf /etc/nginx/nginx.conf

#RUN adduser --disabled-password --gecos '' ml-api-user

# Set the port on which the app runs; make both values the same.
#
# IMPORTANT: When deploying to Azure App Service, go to the App Service on the Azure 
# portal, navigate to the Applications Settings blade, and create a setting named
# WEBSITES_PORT with a value that matches the port here (the Azure default is 80).
# You can also create a setting through the App Service Extension in VS Code.
ENV LISTEN_PORT=5001
EXPOSE 5001

# Indicate where uwsgi.ini lives
#ENV UWSGI_INI uwsgi.ini
ENV STATIC_PATH /app/app/static


WORKDIR /app

# Copy the app contents to the image
COPY . /app

RUN pip install --no-cache-dir -U pip wheel pytest
RUN pip install --no-cache-dir -r requirements.txt


RUN chmod +x run.sh
CMD ["bash", "./run.sh"]