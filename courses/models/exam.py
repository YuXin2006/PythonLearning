from django.db.models import *
from courses.models.course import Course
from courses.serializers.Course_Serializer import CourseSerializer
class Exam(Model):
    #course=CourseSerializer(read_only=True)
    course_id=ForeignKey(Course,on_delete=CASCADE)
    title=SlugField(primary_key=True)
    total_marks=IntegerField()
    date=DateTimeField()
    duration_minutes=IntegerField()