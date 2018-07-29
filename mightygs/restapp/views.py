from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Question, Subject, Section
#from .forms import QuestionForm, SubjectForm, SectionForms
from .serializers import SubjectSerializer, QuestionSerializer, SectionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.reverse import reverse
from rest_framework import pagination, status, mixins, generics

@api_view(['GET'])
def api_root(request, format=None):
    """
    This is `API` browser landing page. The following endpoints provide `questions`, `subjects`,
    `sections` and other `subject-specific` representations.
    """
    return Response({
        'dummyhome' : reverse('mgsapp:index', request=request, format=format),
        'questions': reverse('restapp_question_list', request=request, format=format),
        'subjects' : reverse('restapp_subject_list', request=request, format=format),
        'sections' : reverse('restapp_section_list', request=request, format=format),
        'subject specific questions': "http://localhost:8000/restapp/questions/?subname=history",
        'subject specific sections' : "http://localhost:8000/restapp/sections/?subname=history",

        })

class QuestionListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Returns a list of all `questions`, or filtered questions based on subject
    """

    # try using mixins
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAdminUser,)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # For more advanced control do following if you need to override the list
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        subname = request.query_params.get('subname', None)
        if subname is not None:
            queryset = self.get_queryset().filter(section__subject__title__iexact = subname)
            self.queryset = queryset
            serializer = QuestionSerializer(queryset, many = True)
            # the following call is needed in order not to lose the pagination by ovveriding
            return super(QuestionListView, self).list(request)
            # the following return can be used, but we loose pagination.
            #return Response(serializer.data)
        else:
            queryset = self.get_queryset()
            serializer = QuestionSerializer(queryset, many=True)
            return super(QuestionListView, self).list(request)
           # return Response(serializer.data)




#class QuestionCreateView(CreateView):
    """
    Creates a new question. This may not be implemented yet.
    """
#    model = Question
#    form_class = QuestionForm


class QuestionDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin, 
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    """
    Question Details, retrieve, update and destroy a question
    """

   # model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#class QuestionUpdateView(UpdateView):
#    model = Question
#    form_class = QuestionForm


class SubjectListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """

    Returns a list of subjects
    """
    
    # using Mixins
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#class SubjectCreateView(CreateView):
#    model = Subject
#    form_class = SubjectForm
#
#class SubjectDetailView(DetailView):
#    model = Subject

#
#class SubjectUpdateView(UpdateView):
#    model = Subject
#    form_class = SubjectForm


class SectionListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    """

    Returns a list of sections, and filtered sections based on subjects
    """

# Using Mixins
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # overiding list, we also want to get sections of particular subject
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        subname = request.query_params.get('subname', None)
        if subname is not None:
            queryset = self.get_queryset().filter(subject__title__iexact = subname)
            self.queryset = queryset
            serializer = SectionSerializer(queryset, many = True)
            # the following call is needed in order not to lose the pagination by ovveriding
            return super(SectionListView, self).list(request)
            # the following return can be used, but we loose pagination.
            #return Response(serializer.data)
        else:
            queryset = self.get_queryset()
            serializer = SectionSerializer(queryset, many=True)
            return super(SectionListView, self).list(request)
           # return Response(serializer.data)






#class SectionCreateView(CreateView):
#    model = Section
#    form_class = SectionForm
    


#class SectionDetailView(DetailView):
#    model = Section


#class SectionUpdateView(UpdateView):
#    model = Section
#    form_class = SectionForm



