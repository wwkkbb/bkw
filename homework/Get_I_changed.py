from function.func1 import First, Follow, Select
from collections import OrderedDict


def VT():
    return list('abcde')


def VN():
    return list('BCS')


def VT1():
    return list('abcde')


def VN1():
    return list('SUT')


def get_i(grammar, vtfun, vnfun):
    vt = vtfun()
    vn = vnfun()
    vt_vn = vt + vn
    grammar = sorted(grammar)
    I_all = [grammar[0]]
    I_all_I=[[grammar[0]]]
    I_index = 0
    I_add=[grammer[0]]
    while True:
        I_add_index = 0
        while I_add_index < len(I_add):
            I_add_project = I_add[I_add_index]
            if I_add_project[2] < I_add_project[3] and I_add_project[1][I_add_project[2]] in vn:
                for I0 in grammar:
                    if I0[0] == I_add_project[1][I_add_project[2]] and I0 not in I_add:
                        I_add.append(I0)
            I_add_index += 1
        I_add=sorted(I_add)
        if I_add in I_all[:I_index]:
            del I_all_I[I_index]
            del I_all[I_index]
            if I_index < len(I_all):
                I_add = I_all[I_index]
            else:
                break
            continue
        else:
            I_all[I_index]=I_add

        print(I_index,I_add)
        for t_n in vt_vn:
            I_add=[]
            for project in I_all[I_index]:
                if project[2] < project[3] and project[1][project[2]] == t_n:
                    I_add.append((project[0], project[1], project[2] + 1, project[3]))
            if len(I_add) != 0 and I_add not in I_all_I:
                I_all.append(I_add)
                I_all_I.append(I_add)

        I_index += 1
        if I_index < len(I_all):
            I_add = I_all[I_index]
        else:
            break
    for x in I_all:
        print(x)


# I_start = (('S', 'aSe', 0, 3), ('S', 'B', 0,1), ('B', 'bBe', 0,3), ('B', 'C', 0,1), ('C', 'cCc', 0,3),
#   ('C', 'd', 0,1))
# ('#', 'S', 0, 1)意思： '#'：文法左侧，‘S':文法右侧，0:点所在的位置 1：右侧文法长度

# grammer={'#':['S'],}
grammer = (('#', 'S', 0, 1), ('S', 'UTa', 0, 3), ('S', 'Tb', 0, 2), ('U', 'US', 0, 2), ('U', 'e', 0, 1),
           ('T', 'S', 0, 1), ('T', 'Sc', 0, 2), ('T', 'd', 0, 1))

get_i(grammer, VT1, VN1)
