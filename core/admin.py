# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-02-13T22:01:36+05:30
# @Email:  tamyworld@gmail.com
# @Filename: admin.py
# @Last modified by:   tushar
# @Last modified time: 2017-02-13T22:06:15+05:30



from django.contrib import admin
from .models import University, Course, Student
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Student)
