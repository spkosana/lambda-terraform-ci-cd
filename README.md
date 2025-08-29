# lambda-terraform-ci-cd

## Pre-requisites
### Terraform
- Create AWS Role to get connected with AWS
### Run Lambda Locally
- Software required
  - Install Docker Desktop 
  - Docker should be up and running
  - Docker compose should be up and running 
  - Install make
- Invoke Lambda using docker compose
  - For docker up and running use below command
    - docker compose -f docker-compose.yaml up --build --remove-orphans -d
  - For tearing down the lambda use below command
    - docker compose -f docker-compose.yaml down
  - Check the status of docker containers use below command
    - docker compose ps
