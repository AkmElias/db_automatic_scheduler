from exam_scheduler.models import (Department, Program, Course, Batch, Faculty, Exam, Room, TimeSlot,
                                   CourseOffered, CreateRoutine, Routine, Section)
from .serializers import (UserSerializer, UserMiniSerializer, GroupSerializer, DepartmentSerializer,
                          DepartmentMiniSerializer, ProgramSerializer, ProgramMiniSerializer, CourseSerializer, CourseMiniSerializer,
                          BatchSerializer, BatchMiniSerializer, SectionSerializer, FacultySerializer, FacultyMiniSerializer, ExamSerializer, ExamMiniSerializer,
                          RoomSerializer, RoomMiniSerializer, TimeSlotSerializer, TimeSlotMiniSerializer, CourseOfferedSerializer, CourseOfferedMiniSerializer,
                          CreateRoutineSerializer, CreateRoutineMiniSerializer, RoutineSerializer, RoutineMiniSerializer)

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from django.contrib.auth.models import User, Group
import django_filters
from rest_framework.views import APIView, Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserFilter(filters.FilterSet):

    class Meta:
        model = User
        fields = ('username', 'email')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (TokenAuthentication,)
    filterset_class = UserFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('username', 'email')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        users = User.objects.all()
        serializer = UserMiniSerializer(users, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DepartmentFilter(filters.FilterSet):

    class Meta:
        model = Department
        fields = ('id', 'dpt_code', 'dpt_name')


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('id', 'dpt_code', 'dpt_name')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        departments = Department.objects.all()
        serializer = DepartmentMiniSerializer(departments, many=True)
        return Response(serializer.data)


class ProgramFilter(filters.FilterSet):

    class Meta:
        model = Program
        fields = ('programCode', 'pro_name', 'pro_shortForm', 'DepartmentID')


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filterset_class = ProgramFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('programCode', 'pro_name',
                      'pro_shortForm', 'DepartmentID')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ('programCode', 'DepartmentID')
    search_fields = ('DepartmentID')

    def list(self, request,  *args, **kwargs):
        programs = Program.objects.all()
        serializer = ProgramMiniSerializer(
            programs, many=True, context={'request': request})
        return Response(serializer.data)

    def get_queryset(self):
        programs = Program.objects.all()
        return programs

    def retrieve(self, request,  *args, **kwargs):
        params = kwargs
        print(params['pk'])
        # programs = Program.objects.all()
        programs = Program.objects.filter(DepartmentID=params['pk'])
        serializer = ProgramMiniSerializer(
            programs, many=True,  context={'request': request})
        return Response(serializer.data)
        # programs = Program.objects.filter(programCode = params['pk'])
        # programs = Program.objects.filter(pro_shortForm = params['pk'])


class CourseFilter(filters.FilterSet):

    class Meta:
        model = Course
        fields = ('courseCode', 'crs_title', 'crs_shortName', 'crs_category')


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filterset_class = CourseFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('id', 'courseCode', 'crs_title',
                      'crs_shortName', 'programCode')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseMiniSerializer(courses, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        courses = Course.objects.all()
        return courses

    def retrieve(self, request,  *args, **kwargs):
        params = kwargs
        print(params['pk'])
        courses = Course.objects.filter(id=params['pk'])
        serializer = CourseMiniSerializer(courses, many=True)
        return Response(serializer.data)


class BatchFilter(filters.FilterSet):

    class Meta:
        model = Batch
        fields = ('id', 'batchName', 'programCode')


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    filterset_class = BatchFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('id', 'batchName', 'programCode')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        batches = Batch.objects.all()
        serializer = BatchMiniSerializer(batches, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        batches = Batch.objects.all()
        return batches

    def retrieve(self, request,  *args, **kwargs):
        params = kwargs
        print(params['pk'])
        # programs = Program.objects.all()
        batches = Batch.objects.filter(id=params['pk'])
        serializer = BatchMiniSerializer(batches, many=True)
        return Response(serializer.data)


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class FacultyFilter(filters.FilterSet):

    class Meta:
        model = Faculty
        fields = ('fac_title', 'fac_firstName',
                  'fac_lastName', 'fac_shortName')


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filterset_class = FacultyFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('fac_firstName', 'fac_lastName', 'fac_shortName')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        faculty = Faculty.objects.all()
        serializer = FacultyMiniSerializer(faculty, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        faculties = Faculty.objects.all()
        return faculties

    def retrieve(self, request,  *args, **kwargs):
        params = kwargs
        print(params['pk'])
        faculties = Faculty.objects.filter(id=params['pk'])
        serializer = FacultyMiniSerializer(faculties, many=True)
        return Response(serializer.data)


class ExamFilter(filters.FilterSet):

    class Meta:
        model = Exam
        fields = ('id', )


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filterset_class = ExamFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('id', 'exm_type', 'exm_term', 'exm_year')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        exams = Exam.objects.all()
        serializer = ExamMiniSerializer(exams, many=True)
        return Response(serializer.data)


class RoomFilter(filters.FilterSet):

    class Meta:
        model = Room
        fields = ('rom_capacity', 'roomCode')


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_class = RoomFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('rom_capacity', 'roomCode', 'id')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        rooms = Room.objects.all()
        serializer = RoomMiniSerializer(rooms, many=True)
        return Response(serializer.data)


class TimeSlotFilter(filters.FilterSet):

    class Meta:
        model = TimeSlot
        fields = ('id', 'tst_day')


class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
    filterset_class = TimeSlotFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('id', 'tst_day')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        timeSlots = TimeSlot.objects.all()
        serializer = TimeSlotMiniSerializer(timeSlots, many=True)
        return Response(serializer.data)


class CourseOfferedFilter(filters.FilterSet):

    class Meta:
        model = CourseOffered
        fields = ('batchName', 'courseID', 'facultyID')


class CourseOfferedViewSet(viewsets.ModelViewSet):
    queryset = CourseOffered.objects.all()
    serializer_class = CourseOfferedSerializer
    filterset_class = CourseOfferedFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('Batch', 'Course', 'Faculty')
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

    def list(self, request,  *args, **kwargs):
        coursesOffered = CourseOffered.objects.all()
        serializer = CourseOfferedMiniSerializer(coursesOffered, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        coursesOffered = CourseOffered.objects.all()
        return coursesOffered

    def retrieve(self, request,  *args, **kwargs):
        params = kwargs
        print(params['pk'])
        # programs = Program.objects.all()
        coursesOffered = CourseOffered.objects.filter(id=params['pk'])
        serializer = CourseOfferedMiniSerializer(coursesOffered, many=True)
        return Response(serializer.data)


class CreateRoutineFilter(filters.FilterSet):

    class Meta:
        model = CreateRoutine
        fields = ('dpt_code', 'roomCode')


class CreateRoutineViewSet(viewsets.ModelViewSet):
    queryset = CreateRoutine.objects.all()
    serializer_class = CreateRoutineSerializer
    filterset_class = CreateRoutineFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('dpt_code', 'roomCode')
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_fields = __basic_fields
    #search_fields = __basic_fields
    #filter_backends = (filters.SearchFilter,)
    #search_fields = ('Batch', 'Room')

    #filterset_fields = ('Batch', 'Room')
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def list(self, request,  *args, **kwargs):
        createRoutines = CreateRoutine.objects.all()
        serializer = CreateRoutineMiniSerializer(createRoutines, many=True)
        return Response(serializer.data)


class RoutineFilter(filters.FilterSet):

    class Meta:
        model = Routine
        fields = ('examID', 'roomCode')


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    filterset_class = RoutineFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    __basic_fields = ('examID', 'roomCode')
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_fields = __basic_fields
    #search_fields = __basic_fields
    #filter_backends = (filters.SearchFilter,)
    #search_fields = ('Batch', 'Room')

    #filterset_fields = ('Batch', 'Room')
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    def list(self, request,  *args, **kwargs):
        routines = Routine.objects.all()
        serializer = RoutineMiniSerializer(routines, many=True)
        return Response(serializer.data)

    # def get_queryset(self):
    # 	coursesOffered = CourseOffered.objects.all()
    # 	return coursesOffered

    # def retrieve(self, request,  *args, **kwargs):
    # 	params=kwargs
    # 	print(params['pk'])
    # 	# programs = Program.objects.all()
    # 	coursesOffered = CourseOffered.objects.filter(batchName = params['pk'])
    # 	serializer = CourseOfferedMiniSerializer(coursesOffered, many=True)
    # 	return Response(serializer.data)
