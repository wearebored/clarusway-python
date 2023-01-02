from rest_framework import serializers
from .models import Students

# class StudentSerializers(serializers.Serializer):
#     first_name =serializers.CharField(max_length=50)
#     last_name =serializers.CharField(max_length=50)
#     number =serializers.CharField(max_length=50)

#     def create(self,validate):
#         return Students.objects.create(**validate)

    
#     def update(self, instance, validated_data):
#         instance.first_name =validated_data.get("first_name", instance.first_name)
#         instance.last_name = validated_data.get("last_name",instance.last_name)
#         instance.number = validated_data.get("number", instance.number)

#         instance.save()
#         return instance


# ---------------KULLANIŞLI SERİALİZERS METODU------------

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields="__all__"