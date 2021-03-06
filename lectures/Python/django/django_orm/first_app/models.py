from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # hidden key called Students, a list of students
    # hidden key called visited_by, a list of students

    def __repr__(self):
        return f"<Dojo object: Name = {self.name}, number of students: {self.Students.count()}, number of visits: {self.visited_by.count()}>"

class Student(models.Model):
    # id -> Django generates this for us
    name = models.CharField(max_length=55)
    email = models.EmailField()
    dojo = models.ForeignKey(Dojo, related_name="Students", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visited = models.ManyToManyField(Dojo, related_name = "visited_by")

    def __repr__(self):
        return f"<Student object: Name = {self.name}, Email = {self.email} dojo = {self.dojo.name}, dojos visited = {self.visited.count()}>"


# class Like(models.Model):
#     student = models.ForeignKey(Student, related_name="likes", on_delete=models.CASADE)
#     dojo = models.ForeignKey(Dojo, related_name="liked", on_delete=models.CASADE)
#     #other other columns