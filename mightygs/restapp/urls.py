from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

#router = routers.DefaultRouter()
#router.register(r'question', api.QuestionViewSet)
#router.register(r'subject', api.SubjectViewSet)
#router.register(r'section', api.SectionViewSet)


#urlpatterns = (
    # urls for Django Rest Framework API
#    url(r'^$', views.api_root),
#)

urlpatterns = (
    url(r'^$', views.api_root),
    # urls for Question
    url(r'^questions/$', views.QuestionListView.as_view(), name='restapp_question_list'),
    url(r'^questions/(?P<subname>)/$', views.QuestionListView.as_view(), name='restapp_question_list'),
    #url(r'^questions/create/$', views.QuestionCreateView.as_view(), name='restapp_question_create'),
    url(r'^questions/detail/(?P<pk>\S+)/$', views.QuestionDetailView.as_view(), name='restapp_question_detail'),
    #url(r'^questions/update/(?P<pk>\S+)/$', views.QuestionUpdateView.as_view(), name='restapp_question_update'),
)

urlpatterns += (
    # urls for Subject
    url(r'^subjects/$', views.SubjectListView.as_view(), name='restapp_subject_list'),
    #url(r'^subjects/create/$', views.SubjectCreateView.as_view(), name='restapp_subject_create'),
    #url(r'^subject/detail/(?P<pk>\S+)/$', views.SubjectDetailView.as_view(), name='restapp_subject_detail'),
    #url(r'^subject/update/(?P<pk>\S+)/$', views.SubjectUpdateView.as_view(), name='restapp_subject_update'),
)

urlpatterns += (
    # urls for Section
    url(r'^sections/$', views.SectionListView.as_view(), name='restapp_section_list'),
    url(r'^sections/(?P<subname>)/$', views.SectionListView.as_view(), name='restapp_section_list'),
    #url(r'^sections/create/$', views.SectionCreateView.as_view(), name='restapp_section_create'),
    #url(r'^section/detail/(?P<pk>\S+)/$', views.SectionDetailView.as_view(), name='restapp_section_detail'),
    #url(r'^section/update/(?P<pk>\S+)/$', views.SectionUpdateView.as_view(), name='restapp_section_update'),
)

