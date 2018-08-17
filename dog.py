from models import Character, Born, PB2, PPath, Path, Looper, KPath
from seed_data import seed_data
from random import randrange
import jinja2
import os

jinja_env = jinja2.Environment(
   loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
   extensions=['jinja2.ext.autoescape'],
   autoescape=True)


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
        return [doggo_post_born.pb_1, 1]
    elif born_opt == 2:
        return [doggo_post_born.pb_2, 2]
    elif born_opt == 3:
        return [doggo_post_born.pb_3, 3]

def doggo_pre_pathA():
    doggo_key = Character.query(Character.species == "Dog").get()
    doggo_pre_path = PPath.query(PPath.owner == doggo_key.key).get()
    return doggo_pre_path.PP_1

def doggo_pre_pathB():
    doggo_key = Character.query(Character.species == "Dog").get()
    doggo_pre_path = PPath.query(PPath.owner == doggo_key.key).get()
    return doggo_pre_path.PP_2

def doggo_pathA():
    global post_born_opt
    doggo_key = Character.query(Character.species == "Dog").get()
    doggo_pathA = Path.query(Path.owner == doggo_key.key).get()
    why = randrange(1,3)
    if born_opt == 1:
        if why == 1:
            return doggo_pathA.p_1a[0]
        elif why == 2:
            return doggo_pathA.p_1a[1]
    elif born_opt == 2:
        if why == 1:
            return doggo_pathA.p_2a[0]
        elif why == 2:
            return doggo_pathA.p_2a[1]
    elif born_opt == 3:
        if why == 1:
            return doggo_pathA.p_3a[0]
        elif why == 2:
            return doggo_pathA.p_3a[1]

def doggo_pathB():
    global post_born_opt
    doggo_key = Character.query(Character.species == "Dog").get()
    doggo_pathB = Path.query(Path.owner == doggo_key.key).get()
    why = randrange(1,3)
    if born_opt == 1:
        if why == 1:
            return doggo_pathB.p_1b[0]
        elif why == 2:
            return doggo_pathB.p_1b[1]
    elif born_opt == 2:
        if why == 1:
            return doggo_pathB.p_2b[0]
        elif why == 2:
            return doggo_pathB.p_2b[1]
    elif born_opt == 3:
        if why == 1:
            return doggo_pathB.p_3b[0]
        elif why == 2:
            return doggo_pathB.p_3b[1]
