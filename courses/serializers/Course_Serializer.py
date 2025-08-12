#from rest_framework import serializers
from rest_framework.serializers import *
from courses.models.course import Course
from rest_framework.validators import UniqueValidator
class CourseSerializer(Serializer): 
    '''class Meta:
        model = Course  # 指定关联模型
        fields = ['id', 'name', 'code', 'description']  # 包含所有字段
        extra_kwargs = {
            'name': {
                'validators': [UniqueValidator(queryset=Course.objects.all())]
            },
            'code': {
                'validators': [UniqueValidator(queryset=Course.objects.all())]
            }
        }'''
    id=IntegerField()
    name=CharField(
        max_length=100,
#字段级验证器
        validators=[UniqueValidator(queryset=Course.objects.all(),message="course name must unique")
                    ])

    code=CharField(
       validators=[UniqueValidator(queryset=Course.objects.all(),message="course code must unique! ")
                   ])
    description=CharField(max_length=1000)
#函数验证器    
    def validate_description(self,value):
        if 'fuck' in value.lower() or 'shit' in value.lower():
            raise ValidationError("course description violates standford standard")
        return value
    def validate_code(self,value):
        if not value.startswith("csc"):
            raise ValidationError("course code must start with 'csc'")
        return value

   
    #class Meta:
        #validators=[
           # UniqueTogetherValidator(
               # queryset=Course.objects.all(),
               # fields=["name","code"],
               # message="every courses must have unique name and code"
            #)
        #]
#uniquetogethervalidator：只要有一个属性不同就可以创建        
    
    
    def create(self, validated_data):
        """
        Create and return a new `Course` instance, given the validated data.
        """
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Course` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance    