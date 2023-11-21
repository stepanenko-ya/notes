import random
import requests
import nltk
from settings.celery import app
from django.conf import settings


nltk.download('words')
word_list = nltk.corpus.words.words()


def generate_random_words(num_words=3):
    return random.sample(word_list, num_words)


@app.task
def generation_task():
    random_words = generate_random_words()
    random_words_string = ' '.join(random_words).capitalize()

    login_request = requests.post(
        url='http://web:8000/api/v1/login/',
        data={"username": "admin", "password": "admin"}
    )
    token = login_request.json()['access']

    url = 'http://web:8000/api/v1/app/notes/'
    data = {"title": random_words_string, "content": ""}
    headers = {'Authorization': f'Bearer {token}'}
    requests.post(url=url, data=data, headers=headers)
