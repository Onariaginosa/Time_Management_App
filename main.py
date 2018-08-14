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
        welcome_template = jinja_env.get_template("templates/welcome.html")
        self.response.write(welcome_template.render())

class Character(webapp2.RequestHandler):
    def get(self):
        char_template = jinja_env.get_template("templates/character.html")
        self.response.write(char_template.render())

class CatStory(webapp2.RequestHandler):
    def get(self):
        cat_template = jinja_env.get_template("templates/story.html")
        self.response.write(cat_template.render())
class PandaStory(webapp2.RequestHandler):
    def get(self):
        panda_template = jinja_env.get_template("templates/story.html")
        self.response.write(panda_template.render())
class DogStory(webapp2.RequestHandler):
    def get(self):
        dog_template = jinja_env.get_template("templates/story.html")
        self.response.write(dog_template.render())

app = webapp2.WSGIApplication([
   ('/', MainPage),
   ('/character',Character),
   ('/cat_story',CatStory),
   ('/panda_story',PandaStory),
   ('/dog_story',DogStory)


], debug=True)
