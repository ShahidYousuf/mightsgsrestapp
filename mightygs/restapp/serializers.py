from . import models

from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    #sections = SectionSerializer(read_only=True)
    
    class Meta:
        model = models.Subject
        fields = (
               'title',
               'description',

              )

class SectionSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True) # remove read-only to view this in subject list post form
    class Meta:
        model = models.Section
        fields = (
            'pk', 
            'title', 
            'description',  
            'subject',
            
        )


class QuestionSerializer(serializers.ModelSerializer):
    section = SectionSerializer(read_only= True)
    class Meta:
        model = models.Question
        fields = (
            'pk', 
            'question_text', 
            'created', 
            'optiona', 
            'optionb', 
            'optionc', 
            'optiond', 
            'option_correct',
            'section', 
        )


