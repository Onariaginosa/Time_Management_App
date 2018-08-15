from models import Character, Born, PB2, PPath, Path, Looper, KPath
from seed_data import seed_data
from random import randrange
import jinja2
import os

post_born_opt = 0


jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)
seed_data()
def kat_born():
    kitty_key = Character.query(Character.species == "Cat").get()
    kitty_born = Born.query(Born.owner == kitty_key.key).get()
    born_opt = randrange(1,4)
    if born_opt == 1:
        return kitty_born.born_1
    elif born_opt == 2:
        return kitty_born.born_2
    elif born_opt == 3:
        return kitty_born.born_3
def kat_post_born():
    kitty_key = Character.query(Character.species == "Cat").get()
    kitty_post_born = PB2.query(PB2.owner == kitty_key.key).get()
    post_born_opt = randrange(1,4)
    if post_born_opt == 1:
        return kitty_post_born.pb_1
    elif post_born_opt == 2:
        return kitty_post_born.pb_2
    elif post_born_opt == 3:
        return kitty_post_born.pb_3