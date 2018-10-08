import re
import random

vowels = ['a','e','i','o','u','A','E','I','O','U']

def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU']
    if '`' not in text:
        smileys.append("(・`ω´・)")   
    
    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')
    
    while '!!' in text:
        text = text.replace('!!', '!')
    while '??' in text:
        text = text.replace('??', '?')
        
    choosen = random.choice(smileys) # Don't want the same smiley twice in the same text.
    smileys.remove(choosen)
    
    text = last_replace(text, '!', ' {}'.format(choosen))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '...', ' UwU')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))
    
    text = re.sub('\s\s+' , ' ', text) # remove useless space
    
    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format('Y' if v.isupper() else 'y', v))
            
    return text