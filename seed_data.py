# -*- coding: utf-8 -*-

from models import Character, Born, PB2, PPath, Path, Looper, KPath


def seed_data():
    kitty_key = Character(species= "Cat").put()
    panda_key = Character(species= "Panda").put()
    doggo_key = Character(species = "Dog").put()


    kitty_born = Born(born_1 = "You are a ratty streetcat born in a litter of four. Your mom abandoned you",
    born_2 = "You are a cute kitty cat born in a litter of six. You are super healthy!",
    born_3 = "You are a tiny teacup kitty born in a litter of nine. You are the runt of the bunch",
    owner = kitty_key).put()

    kitty_post_born = PB2(pb_1 = "Congrats! A streetboy found you and took you home. Do you stay with him or run away",
    pb_2 = "Congrats! A rich person saw you and just had to have you. Do you stay with this rich person or run",
    pb_3 = "An old man saw you and took you home with him. Do you stay with him or run",
    owner = kitty_key).put()

    kitty_loop = Looper(loop_1 = "Ouch! The kid was a sadist, and tortured you until you died.",
    loop_2 = "You have a new home! However, that rich person is cat obsessive and dresses you in tight clothing. Do you run or stay?",
    loop_3 = "Noice! The old man wanted  a support animal, so you now live your day to day life well fed and happy. However, the old man died of some unknown illness. The old man left you to his nephew. Do you stay with him or run away?",
    run = "You ran away.",
    owner = kitty_key).put()

    kitty_Path = KPath(p_2a = "You live your life miserably until you die from being strangled by an overly tight kitty outfit.",
    p_2b = "After you run away, you fell asleep in a damp alley. When you awaken, you are in a warm animal shelter. You are soon adopted by a nice person.",
    p_3a = "Awesomeness apparently runs in the family. The nephew is great and you live a long and happy life with him.",
    p_3b = "Because you have been domesticated, you do not know how to survive without human help. You come in contact with a dead mouse and begin to eat it. However, the mouse had leptospirosis, so you die of kidney failure.",
    owner = kitty_key).put()

    panda_born = Born(born_1 = "For your whole life you have been on the run from hunters. Your mother and father fell victim to the vicous fur trade in China",
    born_2 = "You were born in the San Diego Zoo where you spend your time posing for selfies with little kids and playing with your siblings",
    born_3 = "The circus means everything to you. It has been your home for the last ten years.",
    owner = panda_key).put()

    panda_post_born = PB2(pb_1 = "You become stuck in a trap! OH NO! Should you A) escape or B) stay?",
    pb_2 = "A little kid wanders into the zoo and manages to sneak into the cage. Do you A) call for attention or B) keep quiet?",
    pb_3 = "Oh no! Your circus has been disbanded by PETA! Do you A) start a new life or B) join a new circus?",
    owner = panda_key).put()

    panda_path = Path(p_1a = ["Your attempt to escape fails and you end up cutting your foot off. You lose too much blood and your vision is dimming fast. You panic because you do not want your life to end so soon! But your eyes close anyway as you slowly bleed out painfully.", ""],
    p_1b = ["Luckily, you were found by a group of tourists who help free you.", ""],
    p_2a = ["Your brother suddenly comes out of nowhere and is inches from trampling the kid. But since the zookeeper heard your cries, he shows up and saves the kid. Your good behavior is rewarded and the zookeeper buys you new toys! Yay!",""],
    p_2b = ["You end up playing with the kid and have a lot of fun. However, the kid’s mother spots you both playing and threatens to sue the zoo. The zoo decides to free you into the wild and you become separated from your family. You slowly grow apart from them, and after 2 years you have totally forgotten about them. Sad.",""],
    p_3a = ["You are unable to cope with the stress of living by yourself and end up joining a new circus.",""],
    p_3b = ["You are doing great at the new circus and were even offered a new job from Larry the Lion. Should you A) take the job or B) don't take the job?",""],
    owner = panda_key).put()

    panda_post_path = PPath(PP_1 = "Unfortunately your new job requires for you to jump into a pool of sharks. Your attempt to jump fails and you end up getting eaten by the sharks.",
    PP_2 = "You realize that you like your current job. In fact, the tricks that you partake in end up making you rich and famous. You live out the rest of your life swimming in your own fortune and enjoying your life. Yay.",
    owner = panda_key).put()


    doggo_born = Born(born_1 = "You wake up in a dark ravine without any family. You are starving. You scavenge for food but cannot find anything.",
    born_2 = "You were born into a rich family, but they are never home. Your food is overflowing because your owners do not know how much to feed you. The food looks old now.",
    born_3 = "Your owner pats your head with affection. He gazes into your eyes and rubs you behind your ears, just the way you like. Your tail wags. You almost forget you both have no house to live in",
    owner = doggo_key).put()

    doggo_post_born = PB2(pb_1 = "You see food on the dirty floor. One is a seemingly moldy dog buscuit and a dead mouse lies next to it. Which do you eat? Press A for the mouse and B for the buiscuit ",
    pb_2 = "You do not want to have such a boring, empty life. You want more, so you run away. DO you A) follow the music playing from a dirty car or B) run aimlessly?",
    pb_3 = "You see that there is no food for you both tonight. There is only enough for one of you. Do you A) take the food, or B) let the human have it?",
    owner = doggo_key).put()

    doggo_pre_path = PPath(PP_1 = "You regain your strength and decide to take a chance. You go beyond your ravine and ...",
    PP_2 = "The dog buiscuit had salmonella and you become extremely sick.",
    owner = doggo_key).put()

    doggo_path = Path(p_1a = ["You get run over by a car. You are dead.", "You find a pack of dogs. You are happy with your newfound life."],
    p_1b = ["A child finds you and takes you home. The child's family treats you and you feel better", "You die from being sick."],
    p_2a = ["The owner of the car is a travelling musician. He wants a companion for the road so he takes you. You ride off into the sunset excited for what lies ahead.", "The driver doe not stop. You chase on for hours and get tired. You die of exhaustion in an unknown place"],
    p_2b = ["Your owner sees you running away and catches you. You are taken back to your life of solitude."],
    p_3a = ["He yells and tries to grab the bread but you eat it. You run away and the man dies.", "You nudge the bread with your nose toward the man. He places the bread infront of you and finds another piece of bread. You go to bed happy"],
    p_3b = ["He breaks the bread in half and shares it. You rest you muzzle on him and dze off somewhat hungry.", "He kicks you and runs off. You bite his finger off and run away with the bread. The man's finger becomes infected and he dies. You  eat the bread and live for another day."],
    owner = doggo_key).put()
