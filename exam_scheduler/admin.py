from django.contrib import admin
from django.db import models
from .models import Department, Program, Course, Batch, Section, CourseOffered, Faculty, Exam, Room, TimeSlot, Routine, Day


admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Batch)
admin.site.register(Section)
admin.site.register(Faculty)
admin.site.register(CourseOffered)
# admin.site.register(Exam)
admin.site.register(Room)
# admin.site.register(TimeSlot)
admin.site.register(Routine)
# admin.site.register(Day)
