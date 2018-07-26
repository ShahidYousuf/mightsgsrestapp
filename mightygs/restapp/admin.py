from django.contrib import admin
from django import forms
from .models import Question, Subject, Section

class QuestionAdminForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = '__all__'


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ['question_text', 'created', 'optiona', 'optionb', 'optionc', 'optiond', 'option_correct']
    #readonly_fields = ['question_text', 'created', 'optiona', 'optionb', 'optionc', 'optiond', 'option_correct']

admin.site.register(Question, QuestionAdmin)


class SubjectAdminForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectAdmin(admin.ModelAdmin):
    form = SubjectAdminForm
    list_display = ['title', 'description']
   # readonly_fields = ['title', 'description', 'number_of_questions']

admin.site.register(Subject, SubjectAdmin)


class SectionAdminForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = '__all__'


class SectionAdmin(admin.ModelAdmin):
    form = SectionAdminForm
    list_display = ['title', 'description']
    #readonly_fields = ['title', 'description', 'number_of_questions']

admin.site.register(Section, SectionAdmin)


