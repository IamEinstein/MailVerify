import uuid
from django.http.response import HttpResponse
from django.urls import path


def create_id():
    id = uuid.uuid4()
    print(id)
    file = open("random.txt", mode="a", newline='')
    check = open("random.txt", mode="r", newline='')
    if str(id) in check:
        print('id exists')
        id = uuid.uuid4()
    else:
        file.write(str(id)+'\n')
    file.close()
    return id