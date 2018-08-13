 #this is a test
import webapp2
from random import shuffle
import os
import jinja2

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)


   app = webapp2.WSGIApplication([
   ('/', MainPage),
], debug=True)
