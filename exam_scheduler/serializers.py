from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (Department, Program, Course, Batch, Section, Faculty, Exam, Room, TimeSlot,
                     CourseOffered, CreateRoutine, Routine)
from django_filters import rest_framework as filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'groups', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        authentication_classes = (TokenAuthentication,)
        permission_classes = (TokenAuthentication,)


class UserMiniSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {'password' : {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
# HyperlinkedModelSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'dpt_code', 'dpt_name')

# class DepartmentListSerializer9ModelSerializer)
# url = HyperlinkedIdentityField


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class ProgramMiniSerializer(serializers.ModelSerializer):
    # class ProgramMiniSerializer(serializers.HyperlinkedModelSerializer):
    # programCode = serializers.HyperlinkedRelatedField(many=True, view_name='program-detail', read_only=True)

    class Meta:
        model = Program
        # fields = '__all__'
        fields = ('programCode', 'pro_name',  'pro_shortForm',
                  'pro_type', 'DepartmentID')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'crs_title', 'courseCode',
                  'crs_shortName', 'crs_category', 'programCode')


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ('id', 'batchName', 'programCode', 'bat_term', 'bat_year')
# ('id', 'batchName', 'sectionName', 'bat_term', 'bat_year')


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class BatchMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        # fields = ('id', 'batchName', 'sectionName', 'programCode')
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class FacultyMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        # fields = ('facultyID', 'fac_title', 'fac_firstName', 'fac_lastName', 'fac_shortName' )
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ExamMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'exm_type', 'exm_term', 'exm_year')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('roomCode', 'rom_capacity', 'rom_floor', 'rom_type')


class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__'


class TimeSlotMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ('id',)


class CourseOfferedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOffered
        fields = '__all__'


class CourseOfferedMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseOffered
        # fields = ('courseID', 'batchName', 'facultyID')
        fields = '__all__'


class CreateRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateRoutine
        fields = '__all__'


class CreateRoutineMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateRoutine
        fields = ('__all__')


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = '__all__'


class RoutineMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = ('__all__')
