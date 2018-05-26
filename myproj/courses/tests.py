
from django.urls import resolve
from django.urls import reverse
from django.test import TestCase
from .views import home
from django.urls import resolve
from django.test import TestCase
from .views import home, courses_page
from .models import Course


class HomeTests(TestCase):

    def setUp(self):
        self.course = Course.objects.create(course_name='Django', course_code='Django Course.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        courses_page_url = reverse('courses_page', kwargs={'pk': self.course.pk})
        self.assertContains(self.response, 'href="{0}"'.format(courses_page_url))


class CourseTopicsTests(TestCase):
    def setUp(self):
        Course.objects.create(course_name='Django', course_code='Django Course.')

    def test_courses_page_view_success_status_code(self):
        url = reverse('courses_page', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_courses_page_view_not_found_status_code(self):
        url = reverse('courses_page', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_courses_page_url_resolves_Course_topics_view(self):
        view = resolve('/courses/1/')
        self.assertEquals(view.func, courses_page)
