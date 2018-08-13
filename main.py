 #this is a test
import webapp2
from random import shuffle
import os
import jinja2

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to Toki Adventure")

class Character(webapp2.RequestHandler):
    def get(self):
        self.response.write("Choose Your character party ppl")

class DogStory(webapp2.RequestHandler):
    def get(self):
        self.response.write("Story goes here for Dog")

class PandaStory(webapp2.RequestHandler):
    def get(self):
        self.response.write("Story goes here for Panda")
class CatStory(webapp2.RequestHandler):
    def get(self):
        self.response.write("Story goes here for Cat")


app = webapp2.WSGIApplication([
   ('/', MainPage),
   ('/character',Character),
   ('/dog',DogStory),
   ('/panda',PandaStory),
   ('/cat',CatStory)
], debug=True)
