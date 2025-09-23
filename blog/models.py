from django.db import models

class About(models.Model):
    first_name = models.CharField(max_length=50, default="Unknown")
    last_name = models.CharField(max_length=50, default="Unknown")
    address = models.CharField(max_length=255, default="Unknown")
    phone = models.CharField(max_length=50, default="Unknown")
    email = models.EmailField(default="unknown@example.com")
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    about_text = models.TextField(default="No description")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Experience(models.Model):
    title = models.CharField(max_length=100, default="Unknown")
    company = models.CharField(max_length=100, default="Unknown")
    location = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=100, default="Unknown")
    description = models.TextField(default="No description")

    def __str__(self):
        return f"{self.title} - {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=100, default="Unknown")
    school = models.CharField(max_length=200, default="Unknown")
    field = models.CharField(max_length=200, default="Unknown")
    gpa = models.CharField(max_length=20, blank=True)
    date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.degree} - {self.school}"


class Certificate(models.Model):
    name = models.CharField(max_length=200, default="Unknown")

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.name


class Interest(models.Model):
    description = models.TextField(default="No description")

    def __str__(self):
        return self.description[:100]

