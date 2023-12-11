from .models import Course
from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    discount = serializers.DecimalField(max_digits=5, decimal_places=2)
    duration = serializers.IntegerField()
    authername = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self, course, validated_data):
        course.name = validated_data.get('name',course.name)
        course.price = validated_data.get('price',course.price)
        course.discount = validated_data.get('discount',course.discount)
        course.duration = validated_data.get('duration',course.duration)
        course.authername = validated_data.get('authername',course.authername)
        course.save()
        return course
    
    # Or way-2 to update
    '''    
    def update(self, course, validated_data):
        updatedcourse = Course(**validated_data)
        updatedcourse.id = course.id
        updatedcourse.save()
        return updatedcourse
    '''
  
  
  
  
  
  
  
  
  
  
  
  