token = "571274483:AAFhPoNeivu8cE_C9hH7z72b4U74M2dY5rQ"

words = [ 'Every spectator is a plotter, if he tries to explain a word (to know!) (Hugo Ball)',
         'Lacking aura,  at least scatter its emanations.(Henri Michaux)',
         '...the vicinity of the twentieth year, generally prefers to abandon man to his lusterless fate. (Andre Breton)',
         'Beloved imagination, what I most like in you is your unsparing quality. (Andre Breton)',
         'The genome is only a mirror for the breadth or narrowness of human imagination. (Siddhartha Mukherjee)'
         ]

import random
random_message = lambda: random.choice(words)
