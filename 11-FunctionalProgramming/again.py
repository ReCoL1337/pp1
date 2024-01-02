def p20():
    arr = list(range(1,21))
    
    print(list(map(lambda x:pow(x, 3), arr)))

def p21():
    arr = list(range(1,21))

    print(list(filter(lambda x:x%2 == 0 or x%3 == 0, arr)))

def p22():
    names = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
            ("Jackson","Peter"),("Johnson","Rick"),
            ("Lewis","Terry"),("Clarke","Robin")]

    for i in names:
        print(i[0].upper() + ', ' + i[1])

def p23():
    points = [(17,15,16,17,15),
              (16,18,19,17,19),
              (19,15,15,19,18),
              (18,17,19,15,16)]
    print(list(map(lambda x:sum(x) - min(x) - max(x), points)))

def p24():
    def min_pts(limit):
        return lambda pts: pts>=limit
            

    limit = [30,40,70]
    scores = [37,51,44,23,78,92,39,84,83,51]
    for i in limit:
        passed_students = list(filter(min_pts(i), scores))
        print(f"Min {i} pts: {passed_students}")

def p25():
    cities = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
    filtered = list(filter(lambda x:cities[x] > 0, cities.keys()))
    print('Cities with positive temperatures:', " ".join(filtered))

def p26():
    cities = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
    arr = []
    for i in list(map(lambda x:x, cities)):
        data = {'City': i, 'Temp': cities[i]}
        arr.append(data)
    print(arr)


if __name__ == '__main__':
    p26()