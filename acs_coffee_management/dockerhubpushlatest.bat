docker build -t django-coffee .
docker run -it -dp 8000:8000 django-coffee
docker login -u uniquedockeraccount
docker tag django-coffee uniquedockeraccount/django-coffee
docker push uniquedockeraccount/django-coffee
