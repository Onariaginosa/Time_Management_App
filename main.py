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

class Story(webapp2.RequestHandler):
    def get(self):
        story_template = jinja_env.get_template("templates/story.html")
        self.response.write(story_template.render())

app = webapp2.WSGIApplication([
   ('/', MainPage),
   ('/character',Character),
   ('/story',Story)
], debug=True)
