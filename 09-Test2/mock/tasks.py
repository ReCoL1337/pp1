def f(n):
    import csv
    with open('09-Test2\mock\data.csv', encoding='utf8') as file:
        lines = csv.reader(file)
        for line in lines:
            print(', '.join(line))

def p7():
    person = {
        "name": "Marek",
        "surname": "Banach",
        "age": 25,
        "hobby": ["swimming","excursions"],
        "married": True,
        "phone":{"landline":"123444321","mobile":"777888999"}
    }

    print(person)
    print(person.get('name'))
    print(person.get('hobby'))
    person.update({'surname': 'Nowak'})
    print(person.get('surname'))
    person.update({'married': 'False'})
    person.update({'gender': 'male'})
    hobby = person.get('hobby')
    hobby.append('bicycle')
    person.update({'hobby': hobby})
    phone = person.get('phone')
    phone.update({'work': '313131444'})
    print(person)


def p17():
    import os
    icao = {
        'A':'Alfa',
        'B':'Bravo',
        'C':'Charlie',
        'D':'Delta',
        'E':'Echo',
        'F':'Foxtrot',
        'G':'Golf',
        'H':'Hotel',
        'I':'India',
        'J':'Juliett',
        'K':'Kilo',
        'L':'Lima',
        'M':'Mike',
        'N':'November',
        'O':'Oscar',
        'P':'Papa',
        'Q':'Quebec',
        'R':'Romeo',
        'S':'Sierra',
        'T':'Tango',
        'U':'Uniform',
        'V':'Victor',
        'W':'Whiskey',
        'X':'Xray',
        'Y':'Yankee',
        'Z':'Zulu',
    }
    if os.path.exists('09-Test2\mock\ICAO.txt'):
        with open('09-Test2\mock\ICAO.txt', 'w') as file:
            for i in icao:
                file.write(f'{i} {icao.get(i)}\n')
    else:
        with open('09-Test2\mock\ICAO.txt', 'x') as file:
            for i in icao:
                file.write(f'{i} {icao.get(i)}\n')


def p24(n):
    r = []
    b = ''
    while n != 0:
        r.append(n % 2)
        n //= 2
    while len(r) != 0:
        b += str(r.pop())
    return b

def p25(exp: str) -> str:
    s = []
    n1 = 0
    n2 = 0
    for i in exp:
        if i.isdigit():
            s.append(i)
        if i == '+' or i == '-' or i == '*' or i == '/':
            n2 = int(s.pop())
            n1 = int(s.pop())
            if i == '+':
                s.append(n1+n2)
            elif i == '-':
                s.append(n1-n2)
            elif i == '*':
                s.append(n1*n2)
            elif i == '/':
                s.append(n1/n2)
        if i == '=':
            return s.pop()
        
#print(p25('8 3 1 + / 3 2 - 4 + * ='))


def p222():
    import random
    import os

    def rwrite(file):

        count = 0
        while count < 50:
            rand = random.randint(100, 999)
            count += 1
            file.write(f'{rand}\n')


    p = '09-Test2\mock\\rand.txt'
    if os.path.exists(p):
        with open(p, 'w') as file:
            rwrite(file)
    else:
        with open(p, 'x') as file:
            rwrite(file)


def p223():
    import os
    p = '09-Test2\mock\power.txt'
    if os.path.exists(p):
        with open(p, 'w') as file:
            for i in range(1,10+1):
                file.write(f'{i},{pow(i,2)},{pow(i,3)}\n')
    else:
        with open(p, 'x') as file:
            for i in range(1,10+1):
                file.write(f'{i},{pow(i,2)},{pow(i,3)}\n')

def p224():
    import csv
    p = '09-Test2\mock\studentslist.txt'
    try:
        with open(p) as file:
            lines = csv.DictReader(file)
            for line in lines:
                if int(line.get('age')) < 30:
                    data = f'{line.get("first_name")}\t{line.get("last_name")}\t {line.get("email")}'
                    print(data)
    except(FileNotFoundError):
        print('File not found :(')
    except(TypeError):
        print('Ya fucked somethin up m8')
        
p224()