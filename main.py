 #this is a test
import webapp2
from random import shuffle
import os
import jinja2
from cat import kat_born, kat_post_born, kitty_loop, number

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
        kitten = kat_born()
        cat_template = jinja_env.get_template("templates/cat.html")
        self.response.write(cat_template.render({"kitten" :kitten }))

class Cat1(webapp2.RequestHandler):
    def get(self):
        kittten = kat_post_born()
        cat1_template = jinja_env.get_template("templates/cat1.html")
        self.response.write(cat1_template.render({"kittten" :kittten }))

class Cat2(webapp2.RequestHandler):
    def get(self):
        Katt = kitty_loop()
        numb = number()
        cat2_template = jinja_env.get_template("templates/cat2.html")
        self.response.write(cat2_template.render({"Katt" :Katt, "numb":numb}))

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
        self.response.write(seed_data_template.render())

app = webapp2.WSGIApplication([
   ('/', MainPage),
   ('/character',Character),
   ('/cat',CatStory),
   ('/panda',PandaStory),
   ('/dog',DogStory),
   ('/seed_data', LoadDataHandler ),
   ('/cat1',Cat1),
   ('/cat2',Cat2),
   ('/catB', CatB),
   ('/catA', CatA),




], debug=True)
