from models import Character, Born, PB2, PPath, Path, Looper, KPath
from seed_data import seed_data
from random import randrange
import jinja2
import os

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

seed_data()

born_opt = 0

def doggo_born():
    global born_opt
    doggo_key = Character.query(Character.species == "Dog").get()
    doggo_born = Born.query(Born.owner == doggo_key.key).get()
    born_opt = randrange(1,4)
    if born_opt == 1:
        return doggo_born.born_1
    elif born_opt == 2:
        return doggo_born.born_2
    elif born_opt == 3:
        return doggo_born.born_3

def doggo_post_born():
    global post_born_opt
    doggo_key = Character.query(Character.species == "Dog").get()
    doggo_post_born = PB2.query(PB2.owner == doggo_key.key).get()
    if born_opt == 1:
        return doggo_post_born.pb_1
    elif born_opt == 2:
        return doggo_post_born.pb_2
    elif born_opt == 3:
        return doggo_post_born.pb_3
