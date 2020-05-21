import re


# pattern: pat
# replacement: rep
# terminal: term

# extend a string to a list constrain tuples
# tuple = (pat, rep, term)
def extract_replacements(grammar):
    return [(matchObj.group('pat'), matchObj.group('rep'), bool(matchObj.group('term')))
            for matchObj in re.finditer(syntax_re, grammar)
            if matchObj.group('rule')]


def replace(text, replacements):
    while True:
        for pat, rep, term in replacements:
            if pat in text:
                text = text.replace(pat, rep, 1)
                if term:
                    return text
                break
            else:
                return text


# \	Signals a special sequence (can also be used to escape special characters)
# \s	Returns a match where the string contains a white space character
# .	Any character (except newline character)
# ^	Starts with
# $	Ends with
# *	Zero or more occurrences
# +	One or more occurrences
# ()	Capture and group
# |	Either or

syntax_re = r"""
(?mx)
    ^(?: 
        (?: (?P<comment> \# .* ) ) | 
        (?: (?P<blank>   \s*  ) (?: \n | $ )  ) | 
        (?: (?P<rule>    (?P<pat> .+? ) \s+ -> \s+ (?P<term> \.)? (?P<rep> .+) ) )
    )$
"""

grammar1 = """\
A -> apple
B -> bag
S -> shop
T -> the
the shop -> my brother
a never used -> .terminating rule
"""

text1 = "I bought a B of As from T S."

grammar2 = '''\
# Slightly modified from the rules on Wikipedia
A -> apple
B -> bag
S -> .shop
T -> the
the shop -> my brother
a never used -> .terminating rule
'''

grammar3 = '''\
# BNF Syntax testing rules
A -> apple
WWWW -> with
Bgage -> ->.*
B -> bag
->.* -> money
W -> WW
S -> .shop
T -> the
the shop -> my brother
a never used -> .terminating rule
'''

grammar4 = '''\
### Unary Multiplication Engine, for testing Markov Algorithm implementations
### By Donal Fellows.
# Unary addition engine
_+1 -> _1+
1+1 -> 11+
# Pass for converting from the splitting of multiplication into ordinary
# addition
1! -> !1
,! -> !+
_! -> _
# Unary multiplication by duplicating left side, right side times
1*1 -> x,@y
1x -> xX
X, -> 1,1
X1 -> 1X
_x -> _X
,x -> ,X
y1 -> 1y
y_ -> _
# Next phase of applying
1@1 -> x,@y
1@_ -> @_
,@_ -> !_
++ -> +
# Termination cleanup for addition
_1 -> 1
1+_ -> 1
_+_ -> 
'''

grammar5 = '''\
# Turing machine: three-state busy beaver
#
# state A, symbol 0 => write 1, move right, new state B
A0 -> 1B
# state A, symbol 1 => write 1, move left, new state C
0A1 -> C01
1A1 -> C11
# state B, symbol 0 => write 1, move left, new state A
0B0 -> A01
1B0 -> A11
# state B, symbol 1 => write 1, move right, new state B
B1 -> 1B
# state C, symbol 0 => write 1, move left, new state B
0C0 -> B01
1C0 -> B11
# state C, symbol 1 => write 1, move left, halt
0C1 -> H01
1C1 -> H11
'''

grammar6 = [('A', 'apple', False),
            ('B', 'bag', False),
            ('S', 'shop', False),
            ('T', 'the', False),
            ('the shop', 'my brother', False),
            ('a never used', 'terminating rule', True)]

text2 = "I bought a B of As W my Bgage from T S."

text3 = '_1111*11111_'

text4 = '000000A000000'

if __name__ == '__main__':

    print(extract_replacements(grammar1))
    print(extract_replacements(grammar2))

    for match in re.finditer(syntax_re, grammar1):
        print(match.group('term'))

    '''print(replace(text1, grammar6))
    print(replace(text1, extract_replacements(grammar2)))
    print(replace(text2, extract_replacements(grammar3)))
    print(replace(text3, extract_replacements(grammar4)))
    print(replace(text4, extract_replacements(grammar5)))'''
