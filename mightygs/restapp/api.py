from . import models
from . import serializers
from rest_framework import viewsets, permissions
from rest_framework.response import Response


class QuestionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Question class
    This endpoint returns all `questions` in reverse tree format.

    """

    queryset = models.Question.objects.all()
    print("Inside QuestionViewSet")
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class SectionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Section class"""

    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionSubjectViewSet(viewsets.ViewSet):
    print("Inside the QuestionSubjectViewSet")
    def list(self, request):
        subname = request.query_params.get('subname', None)
        queryset = models.Questions.objects.filter(section__subject__title__iexact=subname)
        serializer = serializers.QuestionSerializer(queryset, many=True)
        return Response(serializer.data)