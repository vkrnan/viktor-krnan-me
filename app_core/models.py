from django.db import models

# Create your models here.

# Home
class About(models.Model):
    name = models.CharField(max_length=120)
    mail = models.EmailField()
    image = models.ImageField(null=True, upload_to="images/foto/")

class Introduction(models.Model):
    text = models.TextField()

# Skillset

class Skill_Set(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    set = models.ForeignKey(Skill_Set, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Skill_Desc(models.Model):
    shortdesc = models.TextField()
    longdesc = models.TextField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    def __str__(self):
        return self.shortdesc

# Certifications
class Certification(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    file = models.FileField(null=True, blank=True, upload_to="files/certifications/")
    image = models.ImageField(null=True, upload_to="images/certifications/")
    def __str__(self):
        return self.name

# Employments
class Employment(models.Model):
    name = models.CharField(max_length=60)
    adress = models.CharField(max_length=120)
    desc = models.TextField(blank=True)
    start = models.DateField(auto_now=False, null=True)
    end = models.DateField(auto_now=False, null=True)
    def __str__(self):
        return self.name+"("+self.start.year.__str__()+"-"+self.end.year.__str__()+")"

class EmploymentPosition(models.Model):
    position = models.CharField(max_length=60)
    desc = models.TextField()
    start = models.DateField(auto_now=False, null=True)
    end = models.DateField(auto_now=False, null=True)
    employer = models.ForeignKey(Employment, on_delete=models.CASCADE)
    def __str__(self):
        return self.name+"("+self.start.year.__str__()+"-"+self.end.year.__str__()+")"

# Educations
class Education(models.Model):
    name = models.CharField(max_length=60)
    adress = models.CharField(max_length=120)
    desc = models.TextField()
    start = models.DateField(auto_now=False, null=True)
    end = models.DateField(auto_now=False, null=True)
    def __str__(self):
        return self.name+"("+self.start.year.__str__()+"-"+self.end.year.__str__()+")"

# Testimonials
class Testimonial(models.Model):
    quote = models.TextField()
    autor = models.CharField(max_length=60)
    link = models.TextField()
    logo = models.ImageField(null=True, upload_to="images/testimonials/")

# Adverts
class Advert(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    link = models.TextField()
    banner = models.ImageField(null=True, upload_to="images/adverts/")
    def __str__(self):
        return self.name

# Quotes
class Quote(models.Model):
    quote = models.TextField()