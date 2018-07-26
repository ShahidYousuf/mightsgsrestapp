from django import forms
from .models import Question, Subject, Section


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'optiona', 'optionb', 'optionc', 'optiond', 'option_correct', 'section']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'description']


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'description', 'subject']


