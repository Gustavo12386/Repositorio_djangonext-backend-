import email
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response
from teacher.models import Aula, Professor
from teacher.serializers import ProfessorSerializers, CadastrarAulaSerializers, AulaSerializers
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

class ProfessorAPIView(APIView):
    def get(self, request, format=None):
        professores = Professor.objects.all()
        serializer = ProfessorSerializers(professores, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class CadastrarAulaAPIView(APIView):
    def post(self, request, id, format=None):
       professor = get_object_or_404(Professor, id=id)
       serializer = CadastrarAulaSerializers(data=request.data)
       if serializer.is_valid():
            aula = Aula(nome = serializer.validated_data.get('nome'),
            email = serializer.validated_data.get('email'),
            professor = professor
            )
            aula.save()
            aula_serializer = AulaSerializers(aula, many=False)
            return Response(aula_serializer.data, status=HTTP_201_CREATED)           
       return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)