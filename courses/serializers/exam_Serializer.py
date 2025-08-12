from rest_framework import serializers
from rest_framework.serializers import *
from courses.models.exam import Exam
from courses.serializers.Course_Serializer import CourseSerializer
class ExamSerializer(serializers.ModelSerializer):
    #course_id时外键关联，integerfield（）处理外键会无法直接将course模型转化为整数 
    class Meta:
        model=Exam
        fields='__all__'
    course=CourseSerializer(read_only=True)
    title=CharField(max_length=50)
    total_marks=IntegerField()
    date=DateTimeField()
    duration_minutes=IntegerField()
    
    def create(self, validated_data):
        """
        Create and return a new `Course` instance, given the validated data.
        """
        return Exam.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Course` instance, given the validated data.
        """
        instance.course_id=validated_data.get('course_id',instance.course.id)
        instance.title = validated_data.get('title', instance.title)
        instance.total_marks = validated_data.get('total_marks', instance.total_marks)
        instance.date=validated_data.get('date',instance.date)
        instance.duration_minutes=validated_data.get('duration_minutes',instance.duration_minutes)
        instance.save()
        return instance    