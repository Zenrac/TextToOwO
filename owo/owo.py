import re
import random

def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = ['(・`ω´・)', ';;w;;', '^w^', '>w<', 'UwU']
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')
    
    while '!!' in text:
        text = text.replace('!!', '!')
    while '??' in text:
        text = text.replace('??', '?')
        
    text = text.replace('!', ' {}'.format(random.choice(smileys)))
    text = text.replace('?', '? owo')
    text = re.sub('\s\s+' , ' ', text)
    
    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))
            
    return text