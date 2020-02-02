from django.contrib import admin
from . import models

class ChoicInLine(admin.TabularInline):
    model=models.Choice
    extera=1


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    # model=models.Question
    inlines =[ChoicInLine]