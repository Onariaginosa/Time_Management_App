from models import Character, Born, PB2, PPath, Path, Looper, KPath
from seed_data import seed_data
from random import randrange
import jinja2
import os

born_opt = 0

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)
   
seed_data()

def panda_born():
    panda_key = Character.query(Character.species == "Panda").get()
    panda_born = Born.query(Born.owner == panda_key.key).get()
    global born_opt
    born_opt = randrange(1,4)
    if born_opt == 1:
        return panda_born.born_1
    elif born_opt == 2:
        return panda_born.born_2
    elif born_opt == 3:
        return panda_born.born_3


def panda_post_born():
    global born_opt
    panda_key = Character.query(Character.species == "Panda").get()
    panda_post_born = PB2.query(PB2.owner == panda_key.key).get()
    if born_opt == 1:
        return panda_post_born.pb_1
    elif born_opt == 2:
        return panda_post_born.pb_2
    elif born_opt == 3:
        return panda_post_born.pb_3

def panda_pathA():
    global born_opt
    panda_key = Character.query(Character.species == "Panda").get()
    panda_path = Path.query(Path.owner == panda_key.key).get()
    if born_opt == 1:
        return panda_path.p_1a
    elif born_opt == 2:
        return panda_path.p_2a
    elif born_opt == 3:
        return panda_path.p_3a

def panda_pathB():
    global born_opt
    panda_key = Character.query(Character.species == "Panda").get()
    panda_path = Path.query(Path.owner == panda_key.key).get()
    if born_opt == 1:
        return panda_path.p_1b
    elif born_opt == 2:
        return panda_path.p_2b
    elif born_opt == 3:
        return panda_path.p_3b


def panda_post_pathA():
    panda_key = Character.query(Character.species == "Panda").get()
    panda_post_path = PPath.query(PPath.owner == panda_key.key).get()
    return panda_post_path.PP_1

def panda_post_pathB():
    panda_key = Character.query(Character.species == "Panda").get()
    panda_post_path = PPath.query(PPath.owner == panda_key.key).get()
    return panda_post_path.PP_2

def number():
    global born_opt
    return born_opt
