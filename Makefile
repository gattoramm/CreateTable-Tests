deploy:
  docker-compose build app
  docker-compose run app make deploy