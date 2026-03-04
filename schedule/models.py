from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TeacherInfo(models.Model):
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="info"
    )
    phone = models.CharField(max_length=20, blank=True)
    experience_years = models.IntegerField(default=0)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Info for {self.teacher}"


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses"
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentCourse(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "schedule_student_courses"
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student} - {self.course}"