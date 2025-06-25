FROM python:3

EXPOSE 8000
WORKDIR /acs_coffee_management 
COPY requirements.txt /acs_coffee_management
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /acs_coffee_management 
RUN mkdir -p /usr/share/acs-coffee
COPY db.sqlite3 /usr/share/acs-coffee
RUN rm -rf ./usr
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]