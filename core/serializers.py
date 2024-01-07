from rest_framework import serializers
from core.models import Student, Institute, AppUser, Grade
from rest_framework.response import Response


def email(name):
    return f'send email {name}'

class AppuserSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['username','first_name','last_name']

class GradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('__all__')
    

class InstituteSerializers(serializers.ModelSerializer):
    grade = GradeSerializers(many=True) 
    name = serializers.CharField() 
    num_stars = serializers.IntegerField()
    class Meta:
        model = Institute
        fields = ('__all__')

    def create(self, validated_data):
        data = validated_data.pop('grade')
        institute = Institute.objects.create(**validated_data)
        g_id = []
        for g in data:
            grade = Grade.objects.create(**g)
            g_id.append(grade.id)
        
        institute.grade.add(*g_id)
        institute.save()
        
        return institute   


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        return instance
    
    def save(self, **kwargs):
        name = self.validated_data['name']
        p = email(name)
        print(p)
    

    def validate_num_stars(self,obj):
        print(obj)
        if obj > 5:
            raise serializers.ValidationError("data is incurrect")  
        return obj

        

class StudentSerializers(serializers.ModelSerializer):
    student = AppuserSerializers(read_only=True)
    grade = GradeSerializers(read_only=True)
    institute = InstituteSerializers(read_only=True)

    class Meta:
        model = Student
        fields = ('__all__')
    


class CustomStudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    institute__name = serializers.CharField()