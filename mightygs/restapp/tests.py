import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Question, Subject, Section
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_question(**kwargs):
    defaults = {}
    defaults["question_text"] = "question_text"
    defaults["optiona"] = "optiona"
    defaults["optionb"] = "optionb"
    defaults["optionc"] = "optionc"
    defaults["optiond"] = "optiond"
    defaults["option_correct"] = "option_correct"
    defaults.update(**kwargs)
    if "section" not in defaults:
        defaults["section"] = create_section()
    return Question.objects.create(**defaults)


def create_subject(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["description"] = "description"
    defaults["number_of_questions"] = "number_of_questions"
    defaults.update(**kwargs)
    return Subject.objects.create(**defaults)


def create_section(**kwargs):
    defaults = {}
    defaults["title"] = "title"
    defaults["description"] = "description"
    defaults["number_of_questions"] = "number_of_questions"
    defaults.update(**kwargs)
    if "subject" not in defaults:
        defaults["subject"] = create_subject()
    return Section.objects.create(**defaults)


class QuestionViewTest(unittest.TestCase):
    '''
    Tests for Question
    '''
    def setUp(self):
        self.client = Client()

    def test_list_question(self):
        url = reverse('restapp_question_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_question(self):
        url = reverse('restapp_question_create')
        data = {
            "question_text": "question_text",
            "optiona": "optiona",
            "optionb": "optionb",
            "optionc": "optionc",
            "optiond": "optiond",
            "option_correct": "option_correct",
            "section": create_section().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_question(self):
        question = create_question()
        url = reverse('restapp_question_detail', args=[question.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_question(self):
        question = create_question()
        data = {
            "question_text": "question_text",
            "optiona": "optiona",
            "optionb": "optionb",
            "optionc": "optionc",
            "optiond": "optiond",
            "option_correct": "option_correct",
            "section": create_section().pk,
        }
        url = reverse('restapp_question_update', args=[question.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SubjectViewTest(unittest.TestCase):
    '''
    Tests for Subject
    '''
    def setUp(self):
        self.client = Client()

    def test_list_subject(self):
        url = reverse('restapp_subject_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_subject(self):
        url = reverse('restapp_subject_create')
        data = {
            "title": "title",
            "description": "description",
            "number_of_questions": "number_of_questions",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_subject(self):
        subject = create_subject()
        url = reverse('restapp_subject_detail', args=[subject.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_subject(self):
        subject = create_subject()
        data = {
            "title": "title",
            "description": "description",
            "number_of_questions": "number_of_questions",
        }
        url = reverse('restapp_subject_update', args=[subject.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SectionViewTest(unittest.TestCase):
    '''
    Tests for Section
    '''
    def setUp(self):
        self.client = Client()

    def test_list_section(self):
        url = reverse('restapp_section_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_section(self):
        url = reverse('restapp_section_create')
        data = {
            "title": "title",
            "description": "description",
            "number_of_questions": "number_of_questions",
            "subject": create_subject().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_section(self):
        section = create_section()
        url = reverse('restapp_section_detail', args=[section.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_section(self):
        section = create_section()
        data = {
            "title": "title",
            "description": "description",
            "number_of_questions": "number_of_questions",
            "subject": create_subject().pk,
        }
        url = reverse('restapp_section_update', args=[section.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


