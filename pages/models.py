from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    # We need a field here for the detailed description
    technologies = models.CharField(max_length=200) 

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, help_text="e.g., Languages, AI & ML, Frameworks")

    def __str__(self):
        return self.name

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100, help_text="e.g., May 2025 - Present")
    description = models.TextField()
    degree_image = models.ImageField(upload_to='degrees/', blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.company}"
    
class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    result_details = models.CharField(max_length=200, help_text="GPA or Marks")
    degree_image = models.ImageField(upload_to='degrees/', blank=True, null=True)

    def __str__(self):
        return self.degree