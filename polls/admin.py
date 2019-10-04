from django.contrib import admin

from .models import Choice, Question

# admin.site.register(Question)
# admin.site.register(Choice)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'question', 'votes')
    ordering = ('question', 'pk')


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'pub_date', 'num_choices')
    list_filter = ('pub_date',)
    ordering = ('pub_date', 'pk')
    inlines = [ChoiceInline]
