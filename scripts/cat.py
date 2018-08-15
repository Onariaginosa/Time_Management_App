from models import Character, Born, PB2, PPath, Path, Looper, KPath
from seed_data import seed_data
import random



def kat_born():
    kitty_born = Born.query().fetch()
    born_opt = random.randint(range(1,4))
    if born_opt == 1:
        return kitty_born.
