from function.func import First, Follow, Select
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
    I_all = OrderedDict()
    I_all[0] = grammar

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
                # set_vn=set()
                I_add_index = 0
                while I_add_index < len(I_add):
                    I_add_project = I_add[I_add_index]
                    if I_add_project[2] < I_add_project[3] and I_add_project[1][I_add_project[2]] in vn:
                        for I0 in I_all[0]:
                            if I0[0] == I_add_project[1][I_add_project[2]] and I0 not in I_add:
                                I_add.append(I0)
                    I_add_index += 1
                I_add = sorted(I_add)
                if I_add not in I_all.values():
                    x = list(I_all.keys())[-1] + 1
                    I_all[x] = I_add
                # print(x , I_add)
        len_I_all = len(I_all)
        I_index += 1
    for x in list(I_all):
        print(I_all[x])


# I_start = (('S', 'aSe', 0, 3), ('S', 'B', 0,1), ('B', 'bBe', 0,3), ('B', 'C', 0,1), ('C', 'cCc', 0,3),
#   ('C', 'd', 0,1))
# ('#', 'S', 0, 1)意思： '#'：文法左侧，‘S':文法右侧，0:点所在的位置 1：右侧文法长度
I_start = (('#', 'S', 0, 1), ('S', 'UTa', 0, 3), ('S', 'Tb', 0, 2), ('U', 'US', 0, 2), ('U', 'e', 0, 1),
           ('T', 'S', 0, 1), ('T', 'Sc', 0, 2), ('T', 'd', 0, 1))

get_i(I_start, VT1, VN1)
