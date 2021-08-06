# Silly sentences.

import random

nouns = ['apple', 'ball', 'cat', 'dog', 'elephant',
         'fish', 'goat', 'house', 'iceberg', 'jackal',
         'king', 'llama', 'monkey', 'nurse', 'octopus',
         'pie', 'queen', 'robot', 'snake', 'tofu',
         'unicorn', 'vampire', 'wumpus', 'x-ray', 'yak',
         'zebra']

verbs = ['ate', 'bit', 'caught', 'dropped', 'explained',
         'fed', 'grabbed', 'hacked', 'inked', 'jumped',
         'knitted', 'loved', 'made', 'nosed', 'oiled',
         'puffed', 'quit', 'rushed', 'stung', 'trapped',
         'uplifted', 'valued', 'wanted']

templates = [
    'Waiter! I found a {{noun}} in my {{noun}}!',
    'The {{noun}} {{verb}} the {{noun}}.',
    'If you {{verb}} the {{noun}}, '
    'the {{noun}} will get you.',
    "Let's go: the {{noun}} is {{verb}}.",
    'Colorless green {{noun}}s {{verb}} furiously.'
]


def breaklines(string):
    return "<br>".join(string)


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.
    while index < len(template):
        if template[index: index + 8] == '{{noun}}':
            text = random.choice(nouns)
            output.append(text)
            index += 8
        elif template[index: index + 8] == '{{verb}}':
            text = random.choice(verbs)
            output.append(text)
            index += 8
        else:
            output.append(template[index])
            index += 1

    # After the loop has finished, join the output and return it.
    return "".join(output)


if __name__ == '__main__':
    print(silly_string(nouns, verbs,
                       templates))
