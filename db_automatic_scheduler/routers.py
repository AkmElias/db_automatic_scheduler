from rest_framework import routers
from exam_scheduler import views
from django.urls import include, path
from exam_scheduler.viewsets import (UserViewSet, GroupViewSet, DepartmentViewSet, ProgramViewSet,
                                     CourseViewSet, BatchViewSet, FacultyViewSet, ExamViewSet, RoomViewSet, TimeSlotViewSet,
                                     CourseOfferedViewSet, CreateRoutineViewSet, RoutineViewSet)

# from exam_scheduler.views import ProgramAPIView
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'programs', ProgramViewSet)
# router.register(r'program/', ProgramAPIView)
router.register(r'courses', CourseViewSet)
router.register(r'batches', BatchViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'timeSlots', TimeSlotViewSet)
router.register(r'coursesOffered', CourseOfferedViewSet)
router.register(r'createRoutines', CreateRoutineViewSet)
router.register(r'routines', RoutineViewSet, base_name='routine')
