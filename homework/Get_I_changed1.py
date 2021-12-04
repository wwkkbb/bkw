from function.func1 import First, Follow, Select, Vt_Vn,Closure
from collections import OrderedDict

#
# def VT():
#     return list('abcde')
#
# 
# def VN():
#     return list('BCS')
#
#
# def VT1():
#     return list('abcde')
#
#
# def VN1():
#     return list('SUT')


def get_i(grammar, vt, vn):
    vt_vn = vt | vn
    grammar = sorted(grammar)
    I_all = OrderedDict()
    I_all[0] = Closure([grammar[0]],vn,grammar)

    I_index = 0



    len_I_all = len(I_all)
    while I_index < len_I_all:
        I = I_all[I_index]
        for t_n in vt_vn:

            I_add = []
            for project in I:
                if project[2] < project[3] and project[1][project[2]] == t_n:
                    I_add.append((project[0], project[1], project[2] + 1, project[3]))
            if len(I_add) != 0:
                I_add = Closure(I_add,vn,grammar)
                values=I_all.values()
                if I_add not in values:
                    x = list(I_all.keys())[-1] + 1
                    I_all[x] = I_add
                else:
                    x=list(values).index(I_add)
                print("I{}=Go(I{},{})".format(x,I_index,t_n))
                # print(x , I_add)
        len_I_all = len(I_all)
        I_index += 1
    for x in list(I_all):
        print("I{}={}".format(x,I_all[x]))


# I_start = (('S', 'aSe', 0, 3), ('S', 'B', 0,1), ('B', 'bBe', 0,3), ('B', 'C', 0,1), ('C', 'cCc', 0,3),
#   ('C', 'd', 0,1))
# ('#', 'S', 0, 1)意思： '#'：文法左侧，‘S':文法右侧，0:点所在的位置 1：右侧文法长度
grammars = {'#': ['S'], 'S': ['UTa','Tb'],'U': ['US','e'],
           'T': ['S','Sc','d']}
vt,vn=Vt_Vn(grammars)
I_start=[]
for grammar in grammars:
    grammar_opens=grammars[grammar]
    for grammar_open in grammar_opens:
        I_start.append((grammar,grammar_open,0,len(grammar_open)))

get_i(I_start, vt, vn)
