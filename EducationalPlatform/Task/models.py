from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.name}"


class Enrollment(models.Model):
    student = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"
    
class Assignment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    max_score = models.IntegerField()

    def __str__(self):
        return self.title


class Grade(models.Model):
    student = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='grades')
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, null=True, blank=True)
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE, null=True, blank=True)
    score = models.FloatField()
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.score}"


class Payment(models.Model):
    student = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='payments')
    status = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment by {self.student.name} for {self.course.title}"


class Message(models.Model):
    teacher = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='sent_messages')
    student = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.teacher.name} to {self.student.name}"


class Complaint(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='complaints')
    problem = models.TextField()

    def __str__(self):
        return f"Complaint by {self.user.name}"


class Report(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='reports')
    report = models.TextField()

    def __str__(self):
        return f"Report by {self.user.name}"


class Quiz(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='quizzes')
    time_limit = models.IntegerField()
    avg_rating = models.FloatField()

    def __str__(self):
        return f"Quiz for {self.course.title}"
