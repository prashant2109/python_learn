import re



'''
rs = re.compile('hello', re.X)
print(rs)
'''

'''
sent = 'we are humans'
matched = re.match(r'(.+)\s(.*?)\s(.*)', sent)
print(dir(matched))
print(matched.span())
'''

'''
sent = 'horses are fast'
pattern = re.compile(r'(?P<animal>\w+) (?P<verb>\w+) (?P<adjective>\w+)')
matched = re.search(pattern, sent)
matched = re.match(pattern, sent)
print(matched.groupdict())
'''
'''
st = "an example word:cat!!"
res = re.search(r'word:\w\w\w', st)
print(res.group())
'''

"""
st = ''' Subject has Uber booked already mewlw
        ;efrwerw uber dka;s '''
op = re.sub('ub', '*~', st, flags=re.IGNORECASE)
op = ' '.join(re.split('\s', st, flags=re.IGNORECASE))
print(op)

st = '9109kumar@gmail.com'
op = re.sub('[0-9a-z]+@', '2109jpk@', st)
print(op)
"""
'''
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    print(string.start())
    print(dir(string))
    return not bool(string)

print(is_allowed_specific_char('qwqqw242 34'))
'''

def check_m_ab(strng):
    charRe = re.compile(r'ab+')
    sch  = charRe.search(strng)
    print(dir(sch))
    print(sch.lastindex)
    return bool(sch)
print(check_m_ab('wdqweab'))


