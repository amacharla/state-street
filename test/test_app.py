#!/usr/bin/python3
"""Test Url Shortener Flask app"""
import unittest
import pep8
import inspect
from web_app import web_flask
from web_app.web_flask import app

class TestAPPDocs(unittest.TestCase):
    """Tests to check the documentation and style of Flask APP"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(web_flask, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that web_app/web_flask.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['web_app/web_flask.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_web_flask_module_docstring(self):
        """Test for the web_flask.py module docstring"""
        self.assertIsNot(web_flask.__doc__, None,
                         "web_flask.py needs a docstring")
        self.assertTrue(len(web_flask.__doc__) >= 1,
                        "web_flask.py needs a docstring")


    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in web_flask methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


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
