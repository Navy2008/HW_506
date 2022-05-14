FROM python:3.10.4-slim-bullseye
RUN pip3 install flask flask-wtf email_validator requests flask-login flask-sqlalchemy
# Copy files into container
COPY app.py app.py
COPY wiki.py wiki.py
# Run the app
CMD python app.py
