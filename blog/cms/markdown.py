# This is a heavily modified and simplified markdown interpreter
#     # heading $
#     ( italic )
#     [ bold ]
#     =
#     { unordered list item }
#     =

def parse(text):
    lookup = {'#':'<h1>',
              '$':'</h1>',
              '(':'<em>',
              ')':'</em>',
              '[':'<strong>',
              ']':'</strong>',
              '{':'<li>',
              '}':'</li>',
              '@':'<br />',
              '^':'<br /><br />',
              }
    if confirm_format(text):
        position = 0
        running_list = False
        while position < len(text):
            char = text[position]
            if char == '=':
                if running_list:
                    text = text[:position]+'</ul>'+text[position+1:]
                    running_list = False
                    position += 5
                else:
                    text = text[:position]+'<ul>'+text[position+1:]
                    running_list = True
                    position += 4
            elif char in lookup:
                text = text[:position]+lookup[char]+text[position+1:]
                position += len(lookup[char])
            else:
                position += 1
        return text
    else:
        return 'Text is improperly formated'

def confirm_format(text):
    mark_open = ('#','{','[','(',)
    mark_close = ('$','}',']',')',)
    pairs = {'$':'#',
             ')':'(',
             ']':'[',
             '}':'{',
            }
    stack = []
    for char in range(0,len(text)):
        if text[char] in mark_open:
            stack.append(text[char])
        else:
            if text[char] in mark_close and pairs[text[char]] == stack[-1]:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
