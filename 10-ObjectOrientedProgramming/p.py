# class C():
#     def __init__(self, name, surname, age, seniority) -> None:
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.seniority = seniority

#     def __str__(self) -> str:
#         s = self.surname + self.name[0] + str(self.seniority)
#         if self.age >= 18:
#             return s.upper()
#         else:
#             return s.lower()



# class C():
#     def __init__(self, arr: list) -> None:
#         self.arr = arr

#     def m(self, n):
#         if sum(1 for i in self.arr if all(x > 0 for x in i)) >= n:
#             return True
#         else:
#             return False


class C():
    def __init__(self, sectors: dict):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        return sum(self.sectors.get(sector, 0) for sector in s)

if __name__ == '__main__':
#    print(C("Anna","May",17,7))
#    print(C("George","Brown",21,4))
    


    # c = C([[2,3],[1,8],[-6,4],[3,-7]])
    # print(c.m(3))
    

    c = C({"A":120,"D":150,"G":90,"K":110})
    c.m1("G",130)
    print(c.m2("GD"))
    print(c.m2("KEJ"))
