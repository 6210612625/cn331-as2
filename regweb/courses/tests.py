from django.test import TestCase, Client
from .models import Course
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your tests here.

class CourseTestCase(TestCase):
    def setUp(self):
        course1 = Course.objects.create(code = "JA111" , name  = "A", semester =1,year = 2020 ,quota = 2,status = True)
        course2 = Course.objects.create(code = "JA222" , name  = "B", semester =1,year = 2020 ,quota = 2,status = False)

    def test_seat_available(self):
        """ is_seat_available should be True """

        course =  Course.objects.first()

        self.assertTrue(course.is_seat_available())
        
    def test_seat_not_available(self):
        """ is_seat_available should be False"""

        user1 = User.objects.create(username="user1", password="", email="user1@example.com")
        user2 = User.objects.create(username="user2", password="", email="user2@example.com")

        course = Course.objects.first()
        course.student.add(user1)
        course.student.add(user2)

        self.assertFalse(course.is_seat_available())
    
    def test_index(self):
        c = Client()
        response = c.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)
        
    def test_course(self):
        c = Client()
        course = Course.objects.first()
        response = c.get(reverse('courses:course',args=(course.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_book_successful(self):
        c = Client()
        user3 = User.objects.create(username="user3", password="", email="user3@example.com")
        course = Course.objects.first()
        c.force_login(user3)
        response = c.get(reverse('courses:book',args=(course.id,)))        
        self.assertEqual(course.student.count(),1)
        
    def test_book_unsuccessful(self):
        c = Client()
        course = Course.objects.first()
        response = c.get(reverse('courses:book',args=(course.id,)))        
        self.assertEqual(course.student.count(),0)
        
    def test_remove_successful(self):
        c = Client()
        user3 = User.objects.create(username="user3", password="", email="user3@example.com")
        course = Course.objects.first()
        c.force_login(user3)
        course.student.add(user3)
        response = c.get(reverse('courses:remove',args=(course.id,)))        
        self.assertEqual(course.student.count(),0)
        
    def test_remove_unsuccessful(self):
        c = Client()
        course = Course.objects.first()
        response = c.get(reverse('courses:remove',args=(course.id,)))        
        self.assertEqual(course.student.count(),0)
         

    


    


