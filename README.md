# FastAPI Project Template

The REST API template repository for a FastAPI back-end project.

[![Version](https://img.shields.io/badge/version-1.0-brightgreen.svg)](https://pypi.org/project/ad-topic-recommender/)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Description

This is a template repository for a FastAPI back-end project. It is intended to be used as a starting point for a new project.
It has OAuth2 authentication and JWT token generation. It also has a basic user model and CRUD operations for users.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip 20.0 or higher
- fastapi
- uvicorn
- pydantic
- jose
- passlib
- mysql

### Installation Steps

#### 1. Clone the repository

```bash
git clone https://github.com/dilshankarunarathne/secure-fastapi-template.git
```

#### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

#### 3. Create a MySQL database

```postgresql
create database fastapi;
GRANT ALL PRIVILEGES ON DATABASE fastapi TO fastapi_user;
```

```postgresql
-- Switch to the fastapi database
\c fastapi

-- Create tables
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(256),
    email VARCHAR(256),
    is_admin BOOLEAN DEFAULT FALSE,
    hashed_password VARCHAR(512)
);

CREATE TABLE IF NOT EXISTS blacklist (
    token VARCHAR(512) NOT NULL,
    blacklist_on TIMESTAMP,
    id BIGSERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS task (
    task_id SERIAL PRIMARY KEY,
    task VARCHAR(250) NOT NULL,
    status VARCHAR(30) NOT NULL
);

-- Insert initial data into the task table
INSERT INTO task (task, status) VALUES ('Read an article on React.js', 'Done');
INSERT INTO task (task, status) VALUES ('Organize a meeting', 'Pending');

```

#### 4. Create a `.env` file in the root directory and add the following environment variables

```bash
PGSQL_USER="your mysql user"
PGSQL_PASSWORD="your mysql password"
PGSQL_HOST="localhost"
PGSQL_DATABASE="fastapi"
PGSQL_PORT=5432
```

#### 5. Run the project

```bash
uvicorn main:app --reload
```

#### 6. Open the local URL in a browser to access the Swagger UI

```bash
http://127.0.0.1:8000/auth/login
```

#### 7. Open swagger ui via the following link:

http://127.0.0.1:8000/docs

#### 8. More considerations

We need consider more issues as follows:

- connection pool `done`
- sql injection
- orm framework `done`
- http security config
- unit test
- code generation
- app scale up
- db cluster mgmt

#### 9. Manage k8s cluster

Login as an user Docker Hub:

```bash
docker login

docker image tag secure-fastapi-template-app:latest sunrise2075/secure-fastapi-template-app:2.0

docker push sunrise2075/secure-fastapi-template-app:2.0
````

Test the process of docker composing after removing all prebuilt image: 

```bash
docker-compose up --force-recreate
```

Convert into k8s files in ./k8s:
```bash
kcompose convert --out ./k8s
```

Set up:

```bash

kubectl apply -f ./k8s

kubectl port-forward service/app 8080:80

```

Shut down:
    
```bash
kubectl delete -f ./k8s
```


## Contributing

If you'd like to contribute to this project, please check the contribution guidelines for more information.

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]  
[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa] 

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Contact Information

For questions or feedback, please contact the author:

- Author: Dilshan M. Karunarathne
- Email: ceo@altier.tech
- Website: [http://altier.tech](http://altier.tech)

