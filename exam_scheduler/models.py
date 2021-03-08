from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Department(models.Model):
    # DepartmentID
    id = models.CharField(
        max_length=20, primary_key=True, verbose_name='Department ID')
    dpt_code = models.CharField(
        max_length=20, verbose_name='code', unique=True, blank=False, null=False)
    dpt_name = models.CharField(
        max_length=50, verbose_name='name', unique=True, blank=False, null=False)

    class Meta:
        db_table = '"tbl_department"'
        verbose_name_plural = "Department"

    def __str__(self):
        return self.dpt_name


class Program(models.Model):
    # programCode
    programCode = models.CharField(
        max_length=3, primary_key=True, verbose_name='Program Code', unique=True)
    pro_name = models.CharField(default='B.Sc. Engg. in CSE',
                                max_length=50, verbose_name='name', blank=False, null=False)
    pro_shortForm = models.CharField(
        default='CSE', max_length=20, verbose_name='short Form', blank=False, null=False)
    DepartmentID = models.ForeignKey(
        'Department', on_delete=models.CASCADE, verbose_name='department', db_column="DepartmentID")

    TYPE_CHOICES = (
        ('honours', 'honours'),
        ('masters', 'masters'),
        ('diploma', 'diploma'),
        ('PhD', 'PhD'),
    )

    pro_type = models.CharField(
        default='honours', max_length=10, choices=TYPE_CHOICES, verbose_name='type')

    class Meta:
        db_table = 'tbl_program'
        verbose_name_plural = "Program"

    def __str__(self):
        return self.pro_name


class Course(models.Model):
    # courseID
    id = models.AutoField(
        default=None, max_length=20, primary_key=True, verbose_name='course ID')
    courseCode = models.CharField(
        max_length=8, verbose_name='course Code', unique=True)
    crs_title = models.CharField(max_length=50, verbose_name='title')
    crs_shortName = models.CharField(
        max_length=9, verbose_name='short Name', unique=True)

    CATEGORY_CHOICES = (
        ('major', 'major'),
        ('core', 'core'),
        ('science & mathematics', 'science & mathematics'),
        ('general education', 'general education'),
        ('optional', 'optional'),
    )

    crs_category = models.CharField(
        max_length=25, choices=CATEGORY_CHOICES, verbose_name='category')
    
    crs_credit = models.FloatField(
        blank=True, null=True, verbose_name='credit')
        
    programCode = models.ForeignKey(
        'Program', on_delete=models.CASCADE, verbose_name='program', db_column="programCode")

    class Meta:
        db_table = '"tbl_course"'
        verbose_name_plural = "Course"

    def __str__(self):
        return '%s %s' % (self.courseCode, self.crs_title)
        # return self.crs_shortName


class Batch(models.Model):
    batchName = models.CharField(
        max_length=20, verbose_name='batch', null=False, blank=False)
    programCode = models.ForeignKey(
        'Program', default='115', on_delete=models.CASCADE, verbose_name='program', db_column="programCode")

    TERM_CHOICES = (
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
    )

    bat_term = models.CharField(
        max_length=6, choices=TERM_CHOICES, verbose_name='term')
    bat_year = models.IntegerField(verbose_name='year')

    class Meta:
        db_table = '"tbl_batch"'
        verbose_name_plural = "Batch"
        unique_together = (("batchName", "programCode"),)

    def __str__(self):
        return self.batchName
        # return self.sectionName
        # return str(self.batchName)


class Section(models.Model):
    sectionName = models.CharField(max_length=10, verbose_name='section')
    batchID = models.ForeignKey(
        'Batch', default='1', on_delete=models.CASCADE, verbose_name='batch', db_column="batchName")

    class Meta:
        db_table = '"tbl_section"'
        verbose_name_plural = "Section"

    def __str__(self):
        return self.sectionName


class Faculty(models.Model):
    # facultyID
    id = models.AutoField(
        default=None, max_length=20, primary_key=True, verbose_name='faculty ID')

    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof'),
    )

    fac_title = models.CharField(
        max_length=200, choices=TITLE_CHOICES, verbose_name='title')
    fac_firstName = models.CharField(max_length=20, verbose_name='first Name')
    fac_lastName = models.CharField(max_length=20, verbose_name='last Name')
    fac_shortName = models.CharField(max_length=3, verbose_name='short Name')

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    fac_gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, verbose_name='gender')

    DESIGNATION_CHOICES = (
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Senior Lecturer', 'Senior Lecturer'),
        ('Lecturer', 'Lecturer'),
        ('Head', 'Head'),
        ('Dean', 'Dean'),
    )

    fac_designation = models.CharField(
        max_length=20, choices=DESIGNATION_CHOICES, verbose_name='designation')
    DepartmentID = models.ForeignKey(
        'Department', on_delete=models.CASCADE, verbose_name='department', db_column="DepartmentID")

    class Meta:
        db_table = 'tbl_faculty'
        verbose_name_plural = "Faculty"

    def __str__(self):
        # return self.fac_title
        # def __str__(self):
        return '%s %s' % (self.fac_firstName, self.fac_lastName)


class Exam(models.Model):
    # examID
    id = models.AutoField(default=None, max_length=20, primary_key=True)

    TYPE_CHOICES = (
        ('Supplymentary', 'Supplymentary'),
        ('Mid Term', 'Mid Term'),
        ('Final', 'Final'),
    )

    exm_type = models.CharField(
        max_length=13, choices=TYPE_CHOICES, verbose_name='type')

    TERM_CHOICES = (
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
    )

    exm_term = models.CharField(
        max_length=6, choices=TERM_CHOICES, verbose_name='term')
    exm_year = models.IntegerField(verbose_name='year')

    class Meta:
        db_table = 'tbl_exam'
        verbose_name_plural = "Exam"

    def __str__(self):
        return self.exm_type


class Room(models.Model):
    roomCode = models.CharField(
        max_length=10, primary_key=True, verbose_name='room Code')
    rom_capacity = models.IntegerField(verbose_name='capacity')
    rom_floor = models.CharField(max_length=4, verbose_name='floor')

    TYPE_CHOICES = (
        ('LAB', 'LAB'),
        ('Classroom', 'Classroom'),
        ('Seminar Hall', 'Seminar Hall'),
        ('Library', 'Library'),
    )

    rom_type = models.CharField(
        max_length=12, choices=TYPE_CHOICES, verbose_name='type')

    class Meta:
        db_table = 'tbl_room'
        verbose_name_plural = "Room"

    def __str__(self):
        return self.roomCode


class TimeSlot(models.Model):
    # timeSlotID
    id = models.AutoField(
        default=None, max_length=20, primary_key=True, verbose_name='timeSlot ID')

    startingTime = models.CharField(
        default=None, max_length=20, verbose_name='start', blank=False, null=False)
    endingTime = models.CharField(
        default=None, max_length=20, verbose_name='start', blank=False, null=False)

    class Meta:
        db_table = 'tbl_timeSlot'
        verbose_name_plural = "TimeSlot"

    # def __str__(self):
    # 	return self.tst_duration

    def __str__(self):
        return '%s %s %s' % (self.startingTime, ' to ', self.endingTime)


class Day(models.Model):
    id = models.AutoField(default=None, primary_key=True)
    dayName = models.CharField(
        default=None, max_length=10, blank=False, null=False)

    class Meta:
        db_table = 'tbl_day'
        verbose_name_plural = 'Day'

    def __str__(self):
        return self.dayName


class CourseOffered(models.Model):
    # courseOfferID = models.AutoField(default = None, max_length=20, primary_key = True)
    # courseOfferedID
    id = models.AutoField(
        default=None, max_length=20, primary_key=True, verbose_name='courseOffer ID')

    TERM_CHOICES = (
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn'),
    )

    ofr_term = models.CharField(
        max_length=6, choices=TERM_CHOICES, verbose_name='term')
    ofr_year = models.IntegerField(verbose_name='year')
    # courseCode = models.ForeignKey(
    #     'Course', default=None, on_delete=models.CASCADE, verbose_name='course', db_column="courseCode")
    programID = models.ForeignKey(
        'Program', default=None, on_delete=models.CASCADE, blank='true', null='true', verbose_name='program', db_column="programCode")
    courseID = models.ForeignKey(
        'Course', default=None, on_delete=models.CASCADE, blank='true', null='true', verbose_name='course', db_column="courseID")
    batchName = models.ForeignKey(
        'Batch', default=None, on_delete=models.CASCADE, verbose_name='batch', db_column="batchName")
    sectionName = models.ForeignKey('Section', default=None, on_delete=models.CASCADE,
                                    related_name='section_Name', verbose_name='sectionName', db_column="sectionName")
    facultyID = models.ForeignKey(
        'Faculty', default=None, on_delete=models.CASCADE, verbose_name='faculty', db_column="facultyID")
# to_fields='' unique='True'

    class Meta:
        db_table = 'tbl_courseOffered'
        verbose_name_plural = "CourseOffered"

    def __str__(self):
        return '%s' % (self.id)
        # return self.ofr_term


class CreateRoutine(models.Model):
    # createRoutineID
    id = models.AutoField(
        default=None, max_length=20, primary_key=True, verbose_name='createRoutine ID')
    dpt_code = models.ForeignKey(
        'Department', default=None, on_delete=models.CASCADE, verbose_name='dpt_code', db_column="dpt_code")
    fac_shortName = models.ForeignKey(
        'Faculty', default=None, on_delete=models.CASCADE, verbose_name='fac_shortName', db_column="fac_shortName")
    batch = models.ForeignKey(
        'Batch', default=None, on_delete=models.CASCADE, verbose_name='batch', db_column="batchName")
    section = models.ForeignKey('Section', default=None, on_delete=models.CASCADE,
                                related_name='section', verbose_name='section', db_column="sectionName")
    crs_shortName = models.ForeignKey(
        'Course', default=None, on_delete=models.CASCADE, verbose_name='crs_shortName', db_column="crs_shortName")
    courseCode = models.ForeignKey('Course', default=None, on_delete=models.CASCADE,
                                   related_name='Code', verbose_name='courseCode', db_column="courseCode")
    roomCode = models.ForeignKey(
        'Room', default=None, on_delete=models.CASCADE, verbose_name='roomCode', db_column="room")
    day = models.ForeignKey('TimeSlot', default=None,
                            on_delete=models.CASCADE, verbose_name='day', db_column="day")
    duration = models.ForeignKey('TimeSlot', default=None, on_delete=models.CASCADE,
                                 related_name='duration', verbose_name='duration', db_column="duration")

    class Meta:
        db_table = '"tbl_createRoutine"'
        verbose_name = "CreateRoutine"
        verbose_name_plural = "CreateRoutine"


class Routine(models.Model):
    # routineID
    id = models.AutoField(
        default=None, max_length=20, primary_key=True, verbose_name='routine ID')
    title = models.CharField(default=None, max_length=250,
                             verbose_name='title', blank=False, null=False)
    
    day = models.CharField(default=None, blank=True, null=True, max_length=12)

    # batch and section select individually to get the offered courses but save batch and section as one field
    batchAndSection = models.CharField(
        max_length=20, default=None, blank=False, null=False)
    timeSlot = models.CharField(
        default=None, max_length=20, verbose_name='timeSlot')
    # get courseName and faculty id after selecting the
    courseName = models.CharField(
        max_length=20, default=None, blank=False, null=False)
    courseTitle = models.CharField(max_length=60,default=None,blank=True, null=True)
    facultyFullName = models.CharField(max_length=60,default=None,blank=True, null=True)
    faculty = models.CharField(
        max_length=20, blank=False, null=False, verbose_name='faculties', default=None)

    room = models.CharField(
        default=None, max_length=20, blank=False, null=False, verbose_name='room')

    class Meta:
        db_table = '"tbl_routine"'
        verbose_name = "Routine"
        verbose_name_plural = "Routine"

    # def __str__(self):
    #     return '%s %s %s' % (self.day, self.term, self.year)
        # return self.ofr_term
