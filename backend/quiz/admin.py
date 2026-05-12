
from django.contrib import admin
from .models import Question, Option,Student

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4 
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ['id', 'text', 'created_at']

admin.site.register(Student) 