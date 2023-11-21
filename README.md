## Working routs:
- `/api/v1/register/` - method POST, example body {"username": "admin", "password": "admin"}
- `/api/v1/login/` - method POST, example body {"username": "admin", "password": "admin"}
- `/api/v1/logout/` - method POST, example body {"refresh_token": "eyJhb..."}
***


## For starting through Docker:

### 1. Clone project:

```bash
git clone https://github.com/stepanenko-ya/notes
```

### 2. Build Docker images:

```bash
docker-compose build
```

### 3. Run containers:

```bash
docker-compose up
```
***

## For starting through environment:

### 1. Create Virtual Environment:

```bash
python3 -m pip install --user virtualenv
```

```bash
virtualenv -p python3 venv
or
python3 -m virtualenv venv
```

```bash
source venv/bin/activate
```

***

### 2. Clone project and install all libraries:

```bash
git clone https://github.com/stepanenko-ya/notes
```

```bash
cd notes/
```

```bash
pip3 install -r requirements.txt
```

***


### 3. Apply migrations and Run server:

<br>

```bash
python notes/manage.py migrate
```

```bash
python notes/manage.py runserver
```

***
### 4. In the second terminal run redis

```bash
redis-server --port 8888
```

***
### 5. In the third terminal run celery

```bash
cd notes
celery -A settings worker -l info
```

### 6. In the fourth terminal run celery beat

```bash
cd notes
celery -A settings beat -l info
```
***

### For testing:
Run test
```bash
python manage.py test notes_app.tests
python manage.py test user.tests
```
***
