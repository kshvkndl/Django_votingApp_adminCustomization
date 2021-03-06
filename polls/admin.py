from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# class ChoiceInline(admin.StackedInline):


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # rearranging the display order.
    # fields = ['pub_date', 'question_text']

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date',
                    'was_published_recently', 'days_since_active')

    list_filter = ['pub_date']

    search_fields = ['question_text']

    list_per_page = 25


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
