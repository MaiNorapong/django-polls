from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
# I don't know why django didn't say to include this but I did anyway
