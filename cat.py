from models import Character, Born, PB2, PPath, Path, Looper, KPath
from seed_data import seed_data
from random import randrange
import jinja2
import os

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)

def kat_born():
    kitty_born = Born.query().fetch()
    born_opt = randrange(1,4)
    if born_opt == 1:
        return kitty_born
    elif born_opt == 2:
        return kitty_born
    elif born_opt == 3:
        return kitty_born
