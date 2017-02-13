# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-02-13T22:02:55+05:30
# @Email:  tamyworld@gmail.com
# @Filename: models.py
# @Last modified by:   tushar
# @Last modified time: 2017-02-14T02:51:31+05:30



from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import django.db.models.options as options
options.DEFAULT_NAMES=options.DEFAULT_NAMES+('es_index_name','es_type_name','es_mapping')
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
    class Meta:
        es_index_name='django'
        es_type_name='student'
        es_mapping={
        'properties':{
            'university':{
                "type":'object',
                "properties":{
                    "name":{'type':'string','index':'not_analyzed'},
                    }
                },
                'first_name':{'type':'string','index':'not_analyzed'},
                'last_name':{'type':'string','index':'not_analyzed'},
                'age':{'type':'short'},
                'year_in_school':{'type':'string'},
                'name_complete':{
                "type":"completion",
                "analyzer":"simple",
                'payloads':True,
                'preserve_separators':True,
                'preserve_position_increments':True,
                'max_input_length':50
                },
                "course_names":{
                    "type":"string","store":"yes","index":"not_analyzed"
                }

            }
        }
