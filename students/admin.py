from django.contrib import admin
# 해당 모델에서 클래스 이름을 임포트
from students.models import Student
# Register your models here.
# 어드민에 등록
admin.site.register(Student)