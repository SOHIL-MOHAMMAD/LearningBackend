from django.contrib import admin
from .models import Member
# Register your models here.

class MemberModel(admin.ModelAdmin):
  list1_display = ('firstname','lastname', 'age')


admin.site.register(Member , MemberModel)