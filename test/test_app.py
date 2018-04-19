#!/usr/bin/python3
"""Test Url Shortener Flask app"""
import unittest
from web_app.web_flask import app

class TestUrlShortener(unittest.TestCase):
    """Class to test Url Shortener functionality"""
    @classmethod
    def setupClass(self):
       """Creating test client for all calls"""
       app.testing = True
       self.client = app.test_client()

    def test_404(self):
        """Test the result of querying a website that does not exist"""
        rv = self.client.get('/1234')
        self.assertEqual(rv.status_code, 404)

    def test_add(self):
        """Test adding url"""
        res = self.client.post('/', data={'ogUrl': 'statestreet.com'})
        self.assertEqual(res.status_code, 201)

        res = self.client.post('/', data={'ogUrl': 'statestreet.com'})
        self.assertEqual(res.status_code, 200)

    def test_retrival(self):
        """Test Retrival of original url"""
        res = self.client.post('/', data={'ogUrl': 'google.com'})
        shortUrl = res.form.get('shortUrl')

        res2 = self.client.get('/'+ shortUrl)
        self.assertEqual(res.url, 'http://www.google.com')
