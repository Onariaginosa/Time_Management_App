 #this is a test
import webapp2
from random import shuffle
import os
import jinja2
from models import Character, Born, PB2, PPath, Path, Looper, KPath
from seed_data import seed_data

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
        kat_born = Born.query().order().fetch()
        cat_template = jinja_env.get_template("templates/cat.html")
        self.response.write(cat_template.render())
class PandaStory(webapp2.RequestHandler):
    def get(self):
        panda_template = jinja_env.get_template("templates/panda.html")
        self.response.write(panda_template.render())
class DogStory(webapp2.RequestHandler):
    def get(self):
        dog_template = jinja_env.get_template("templates/dog.html")
        self.response.write(dog_template.render())

class LoadDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()
        self.response.write("Seed_Data added to database")

app = webapp2.WSGIApplication([
   ('/', MainPage),
   ('/character',Character),
   ('/cat',CatStory),
   ('/panda',PandaStory),
   ('/dog',DogStory),
   ('/seed_data', LoadDataHandler ),


], debug=True)
