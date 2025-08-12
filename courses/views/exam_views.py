from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *
from courses.models.exam import Exam
from courses.serializers.exam_Serializer import ExamSerializer
from django.shortcuts import get_object_or_404

class ExamListCreateView(APIView):
    def get(self,request):
        exams=Exam.objects.all()
        serializer=ExamSerializer(exams,many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    def post(self,request):
        serializer=ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST) 
class ExamDetailUpdateDeleteView(APIView):
    def get(self,request,pk):
        exam=get_object_or_404(Exam,pk=pk)
        serializer=ExamSerializer(exam,many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    def put(self,request,pk):
        exam=get_object_or_404(Exam,pk=pk)
        serializer=ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST) 
    def delete(self,request,pk):
        exam=get_object_or_404(Exam,pk=pk)   
        exam.delete()        
        return Response({"status":"exam delete successfully"},status=HTTP_200_OK)