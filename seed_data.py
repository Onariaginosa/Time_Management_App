from models import Character, KBorn, PB2


def seed_data():
    kitty_key = Character(species= "Cat").put()
    panda_key = Character(species= "Panda").put()
    doggo_key = Character(species = "Dog").put()



    kitty_born = Born(born_1 = "You are a ratty streetcat born in a litter of four. Your mom abandoned you",
    born_2 = "You are a cute kitty cat born in a litter of six. You are super healthy!",
    born_3 = "You are a tiny teacup kitty born in a litter of nine. You are the runt of the bunch",
    owner = kitty_key).put()

    panda_born = Born(born_1 = "For your whole life you've been on the run from hunters. Your mother and father fell victim to the vicous fur trade in China",
    born_2 = "You were born in the San Diego Zoo where you spend your time posing for selfies with little kids and playing with your siblings",
    born_3 = "The circus means everything to you. It has been your home for the last ten years.",
    owner = panda_key).put()

    panda_post_born = PB2(pb_1 = "You become stuck in a trap! OH NO! Should you"

    doggo_born = Born()
