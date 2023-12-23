def p27():
    test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]

    print(list(filter(lambda x: 50 <= x['result'] <= 70, test_results)))

def p28():
    og = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
          {"country":"Finland","gold":5,"silver":0,"bronze":4},
          {"country":"USA","gold":12,"silver":5,"bronze":11},
          {"country":"Peru","gold":0,"silver":1,"bronze":7}]
    tens = filter(lambda x: x['gold'] + x['silver'] + x['bronze'] >= 10, og)
    print('COUNTRIES WITH AT LEAST 10 MEDALS')
    for country in tens:
        print(f'{country["country"]}: {country["gold"]},{country["silver"]},{country["bronze"]}')

def p29():
    og = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
          {"country":"Finland","gold":5,"silver":0,"bronze":4},
          {"country":"USA","gold":12,"silver":5,"bronze":11},
          {"country":"Peru","gold":0,"silver":1,"bronze":7}]
    
    results = list(map(lambda x: x['gold'] + x['silver'] + x['bronze'], og))
    countries = list(map(lambda x: x['country'], og))
    # for i in results:
    #     for j in range(0, i+1):
    #         print(j)

    print(countries, results)




if __name__ == '__main__':
    # print(list(map(lambda x: pow(x, 3), range(1, 20+1))))
    # print(dict((i, pow(i, 3)) for i in range(1, 20+1)))
    
    p29()