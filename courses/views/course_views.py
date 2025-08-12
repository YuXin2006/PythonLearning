from django.http import HttpResponse,JsonResponse
from courses.models.course import Course
from courses.serializers.Course_Serializer import  CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework.status import *
@api_view(['GET','POST'])
def course_list(request):
    if request.method == "GET":
        courses=Course.objects.all()
   # return HttpResponse("".join([str(course) for course in courses])) #httpresponse
   # ------jsonresponse: query->dictionary->list->json
   #response={"courses":list(courses.values()) }
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data,HTTP_200_OK)
    elif request.method=='POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def course_detail(request,pk):
    courses=get_object_or_404(Course,pk=pk)
    if request.method=="GET":
        serializer=CourseSerializer(courses)
        return Response(serializer.data,status=HTTP_200_OK)
    elif request.method=="PUT":
        serializer=CourseSerializer(courses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        courses.delete()
        return Response({"status":"course deleted sucessfully!"},status=HTTP_200_OK)

class CourseListCreateView(APIView):
    def get(self,request):
        courses=Course.objects.all()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data,status=HTTP_200_OK)
            
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)        





class CoureseDetailUpdateDeleteView(APIView):
    def get(self,request,pk):
        courses=get_object_or_404(Course,pk=pk)
        serializer=CourseSerializer(courses)
        return Response(serializer.data,status=HTTP_200_OK)    
    def put(self,request,pk):
        courses=get_object_or_404(Course,pk=pk)
        serializer=CourseSerializer(courses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        courses=get_object_or_404(Course,pk=pk)
        courses.delete()
        return Response({"status":"course deleted sucessfully!"},status=HTTP_200_OK)
                