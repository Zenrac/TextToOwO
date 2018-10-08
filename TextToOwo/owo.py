import re
import random

def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU']
    if '`' not in text:
        smileys.append("(・`ω´・)")
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')
    
    while '!!' in text:
        text = text.replace('!!', '!')
    while '??' in text:
        text = text.replace('??', '?')
        
    text = last_replace(text, '!', ' {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '...', ' UwU')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))
    text = re.sub('\s\s+' , ' ', text)
    
    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))
            
    return text