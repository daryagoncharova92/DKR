from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from json import loads
from json import dumps
from .serializer import NoteSerialilzer
from .utils import DataBase
import redis
import os


host = os.environ.get("REDIS_HOST")
port = os.environ.get("REDIS_PORT")
db = os.environ.get("REDIS_DB")
redis = redis.Redis(host, port=port, db=db)


class NoteView(APIView):
    def __init__(self):
        super().__init__()
        self.database = DataBase()
        self.serializer = NoteSerialilzer


    def get(self, request: Request):
        id = request.query_params.get('id', None)
        if id is None:
            notes = self.database.all()
            serializer = self.serializer(notes, many=True)
            return Response(serializer.data, status=200)

        return self.get_detail(id)


    def post(self, request: Request):

        if not request.user.is_authenticated:
            return Response(status=400)

        serializer = self.serializer(data=loads(request.body))
        if not serializer.is_valid():
            return Response(status=400)

        self.database.update(serializer.data)
        redis.delete(serializer.data['id'])
        return Response(status=200)


    def put(self, request: Request):
        if not request.user.is_authenticated:
            return Response(status=400)

        serializer = self.serializer(data=loads(request.body))
        if not serializer.is_valid():
            return Response(status=400)

        self.database.create(serializer.data)
        return Response(status=200)


    def delete(self, request: Request):
        if not request.user.is_authenticated:
            return Response(status=400)

        id = loads(request.body)['id']
        self.database.delete(id)
        redis.delete(id)
        return Response(status=200)


    def get_detail(self, id: int):
        note = redis.get(id)
        if note:
            return Response(loads(note), status=200)
        note = self.database.get_by_id(id)
        if not note:
            return Response(status=400)

        data = self.serializer(note).data
        redis.set(id, dumps(data))
        return Response(data, status=200)