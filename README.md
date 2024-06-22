# Test for nginx service

This is a simple web application (index.html) with nginx reverse proxy and an e2e test. It has its own docker image, which is built, tested, pushed and deployed to production through github actions (the deployment to production is done by ansible behind the scenes). [The devops flow diagram](https://docs.google.com/drawings/d/1TFNIVpcPsQ_52gYD98uO4XHaDl41_lfCrueD-KizCOk/edit?usp=sharing).

## Install requirements

`pip install -r requirements.txt`

## Run the app
`docker run -d -p 80:80 kaniuxxjd/nginx-test-app:latest`

## Run the test

`python3 test_nginx.py`
