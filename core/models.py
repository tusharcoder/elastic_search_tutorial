# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-02-13T22:02:55+05:30
# @Email:  tamyworld@gmail.com
# @Filename: models.py
# @Last modified by:   tushar
# @Last modified time: 2017-02-14T00:27:25+05:30



from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class University(models.Model):
        name = models.CharField(max_length=255, unique=True)
class Course(models.Model):
        name = models.CharField(max_length=255, unique=True)
class Student(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
                ('FR', 'Freshman'),
                ('SO', 'Sophomore'),
                ('JR', 'Junior'),
                ('SR', 'Senior'),

    )
        # note: incorrect choice in MyModel.create leads to
        # creation of incorrect record
    year_in_school = models.CharField(
                max_length=2, choices=YEAR_IN_SCHOOL_CHOICES
    )
    age = models.SmallIntegerField(
                validators=[MinValueValidator(1), MaxValueValidator(100)]

    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
        # various relationships models
    university = models.ForeignKey(University, null=True, blank=True)
    courses = models.ManyToManyField(Course, null=True, blank=True)
    def __unicode__(self):
        return self.first_name+" "+self.last_name
