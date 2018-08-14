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

    doggo_born = Born(born_1 = "You wake up in a dark ravine without any family. You are starving. You scavenge for food but cannot find anything.",
    born_2 = "You were born into a rich family, but they are never home. Your food is overflowing because your owners do not know how much to feed you. The food looks old now.",
    born_3 = "Your owner pats your head with affection. He gazes into your eyes and rubs you behind your ears, just the way you like. Your tail wags. You almost forget you both have no house to live in",
    owner = doggo_key).put()
    )


    kitty_post_born = PB2(pb_1 = "Congrats! A streetboy found you and took you home. Do you stay with him or run away",
    pb_2 = "Congrats! A rich person saw you and just had to have you. Do you stay with this rich person or run",
    pb_3 = "An old man saw you and took you home with him. Do you stay with him or run",
    owner = kitty_key).put()
    )

    panda_post_born = PB2(pb_1 = "You become stuck in a trap! OH NO! Should you stay or escape?",
    pb_2 = "A little kid wanders into the zoo and manages to sneak into the cage. Do you call for attention or keep quiet?",
    pb_3 = "Oh no! Your circus has been disbanded by PETA! Do you join a new circus or start a new life?",
    owner = panda_key).put()

    doggo_post_born = PB2(pb_1 = "You see food on the dirty floor. One is a seemingly moldy dog buscuit and a dead muse lies next to it. Which do you eat?",
    pb_2 = "You don't want to have such a boring, empty life. You want more, so you run away. DO you follow the music playing from a dirty car or run aimlessly?"
    pb_3 = "You see that there is no food for you both tonight. There is only enough for one of you. Do you take the food, or let the hooman have it?",
    owner = doggo_key).put()
