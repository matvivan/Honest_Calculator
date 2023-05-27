msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def is_one(v):
    return -10 < v < 10 and v.is_integer()

def check(v1, v2, v3):
    msg = ''
    if is_one(v1) and is_one(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and v3 != '/':
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
    print(msg) 

# enter your code here

memory = 0.0

def prompt(msg):
    try:
        return {'y' : True, 'n' : False}[input(msg + '\n')]
    except KeyError:
        return prompt(msg)

while True:
    calc = input(msg_0).split()
    try:
        x = float(calc[0]) if calc[0] != 'M' else memory
        y = float(calc[2]) if calc[2] != 'M' else memory

        # check laziness
        check(x, y, calc[1])
        #
        
        result = {'+' : lambda x, y : x + y,
                  '-' : lambda x, y : x - y,
                  '*' : lambda x, y : x * y,
                  '/' : lambda x, y : x / y}[calc[1]](x, y)
        print(result)

        # memory prompt
        if prompt(msg_4):
            if not is_one(result) or (prompt(msg_10) and prompt(msg_11) and prompt(msg_12)):
                memory = result
        #
                
        # exit prompt
        if not prompt(msg_5):
            break
        #
    except ValueError:
        print(msg_1)
    except KeyError:
        print(msg_2)
    except ZeroDivisionError:
        print(msg_3)