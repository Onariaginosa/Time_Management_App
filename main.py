 #this is a test
import webapp2
from random import shuffle
import os
import jinja2
from seed_data import seed_data
from cat import kat_born, kat_post_born, kitty_loop, kitty_pathB, kitty_pathA
from panda import panda_born, panda_post_born, panda_pathB, panda_pathA, panda_post_pathA, panda_post_pathB, number
from dog import doggo_born, doggo_post_born, doggo_pre_pathA, doggo_pre_pathB, doggo_pathA, doggo_pathB

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

class MainPage(webapp2.RequestHandler):
    # seed_data()
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
        katt = kitty_loop()
        kkatt = katt[0]
        numbr = katt[1]
        cat2_template = jinja_env.get_template("templates/cat2.html")
        self.response.write(cat2_template.render({"kkatt" :kkatt, "numbr":numbr}))

class CatA(webapp2.RequestHandler):
    def get(self):
        Acat = kitty_pathA()
        catA_template = jinja_env.get_template("templates/catA.html")
        self.response.write(catA_template.render({"Acat" :Acat}))

class CatB(webapp2.RequestHandler):
    def get(self):
        Bcat = kitty_pathB()
        catB_template = jinja_env.get_template("templates/catB.html")
        self.response.write(catB_template.render({"Bcat" :Bcat}))

class PandaStory(webapp2.RequestHandler):
    def get(self):
        Pannda = panda_born()
        panda_template = jinja_env.get_template("templates/panda.html")
        self.response.write(panda_template.render({"Pannda": Pannda}))

class Panda1(webapp2.RequestHandler):
    def get(self):
        PPanda = panda_post_born()
        panda1_template = jinja_env.get_template("templates/panda1.html")
        self.response.write(panda1_template.render({"PPanda" :PPanda }))

class PandaA(webapp2.RequestHandler):
    def get(self):
        nnumber = number()
        ppPanda = panda_pathA()
        pPanda = "".join(ppPanda)
        pandaA_template = jinja_env.get_template("templates/pandaA.html")
        self.response.write(pandaA_template.render({"pPanda" :pPanda, "nnumber":nnumber }))

class PandaB(webapp2.RequestHandler):
    def get(self):
        numbber = number()
        PPpanda = panda_pathB()
        Ppanda = "".join(PPpanda)
        pandaB_template = jinja_env.get_template("templates/pandaB.html")
        self.response.write(pandaB_template.render({"Ppanda" :Ppanda, "numbber":numbber }))

class PandaPostA(webapp2.RequestHandler):
    def get(self):
        posttA = panda_post_pathA()
        pandapostA_template = jinja_env.get_template("templates/pandapostA.html")
        self.response.write(pandapostA_template.render({"posttA" :posttA }))

class PandaPostB(webapp2.RequestHandler):
    def get(self):
        posttB = panda_post_pathB()
        pandapostB_template = jinja_env.get_template("templates/pandapostB.html")
        self.response.write(pandapostB_template.render({"posttB" :posttB }))

class DogStory(webapp2.RequestHandler):
    def get(self):
        dborn = doggo_born()
        dog_template = jinja_env.get_template("templates/dog.html")
        self.response.write(dog_template.render({"dborn":dborn}))

class Dog1(webapp2.RequestHandler):
    def get(self):
        doggyb = doggo_post_born()
        dog_pb = doggyb[0]
        nums = doggyb[1]
        dog1_template = jinja_env.get_template("templates/dog1.html")
        self.response.write(dog1_template.render({"dog_pb": dog_pb, "nums":nums}))

class DogpreA(webapp2.RequestHandler):
    def get(self):
        dogpreA = doggo_pre_pathA()
        dogpreA_template = jinja_env.get_template("templates/dogpreA.html")
        self.response.write(dogpreA_template.render({"dogpreA": dogpreA}))

class DogpreB(webapp2.RequestHandler):
    def get(self):
        dogpreB = doggo_pre_pathB()
        dogpreB_template = jinja_env.get_template("templates/dogpreB.html")
        self.response.write(dogpreB_template.render({"dogpreB": dogpreB}))

class Dog2A(webapp2.RequestHandler):
    def get(self):
        dogA = doggo_pathA()
        dog2A_template = jinja_env.get_template("templates/dog2A.html")
        self.response.write(dog2A_template.render({"dogA": dogA}))

class Dog2B(webapp2.RequestHandler):
    def get(self):
        dogB = doggo_pathB()
        dog2B_template = jinja_env.get_template("templates/dog2B.html")
        self.response.write(dog2B_template.render({"dogB": dogB}))







app = webapp2.WSGIApplication([
   ('/', MainPage),
   ('/character',Character),
   ('/cat',CatStory),
   ('/cat1',Cat1),
   ('/cat2',Cat2),
   ('/catB', CatB),
   ('/catA', CatA),
   ('/panda',PandaStory),
   ('/panda1', Panda1),
   ('/pandaA', PandaA),
   ('/pandaB', PandaB),
   ('/pandapostA', PandaPostA),
   ('/pandapostB', PandaPostB),
   ('/dog',DogStory),
   ('/dog1', Dog1),
   ('/dogpreA', DogpreA),
   ('/dogpreB', DogpreB),
   ('/dog2A', Dog2A),
   ('/dog2B', Dog2B),


], debug=True)
