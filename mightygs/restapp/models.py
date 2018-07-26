from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields

class Subject(models.Model):
    SUBJECT_CHOICES = (
           ('History', 'History'),
           ('Geography', 'Geography'),
           ('Indian Polity', 'Indian Polity'),
           ('Economics','Economics'),
           ('Ecology','Ecology'),
           ('Science', 'Science'),
           ('General Knowledeg', 'GK'),
           ('Aptitude', 'Aptitude'),
        )

    # Fields
    title = models.CharField(max_length=50, choices = SUBJECT_CHOICES)
    description = models.TextField(max_length=100)

    #Relationship Fields
    #sections = models.ForeignKey(Section, on_delete=models.CASCADE)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('restapp_subject_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('restapp_subject_update', args=(self.pk,))

class Section(models.Model):

    # Fields
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=100)

    # Relationship Fields
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
   # questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('restapp_section_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('restapp_section_update', args=(self.pk,))


class Question(models.Model):
    CORRECT_OPTIONS = (
               ('optiona', 'optiona'),
               ('optionb', 'optionb'),
               ('optionc', 'optionc'),
               ('optiond', 'optiond'),
        )

    # Fields
    question_text = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    optiona = models.CharField(max_length=30)
    optionb = models.CharField(max_length=30)
    optionc = models.CharField(max_length=30)
    optiond = models.CharField(max_length=30)
    option_correct = models.CharField(max_length=30, choices = CORRECT_OPTIONS)

    # Relationship Fields
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.question_text

    def get_absolute_url(self):
        return reverse('restapp_question_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('restapp_question_update', args=(self.pk,))




