KESI = '$'
TERMINATOR = '@'

def Vt_Vn(grammers):
    vn = set()
    vt = set()
    for left in grammers:
        vn.add(left)
        for right in grammers[left]:
            vt.update(right)
    for i in vt.copy():
        if i in vn:
            vt.remove(i)
    print(vt, vn)
    return vt, vn


def First(st, rules, VT, VN, ls):
    st = st + TERMINATOR
    set_first = set()
    for s in st:
        if s in VT or s == KESI:
            return {s}
        elif s in VN:
            num = ls.count(s)
            if num > 1:
                return set()
            ls.append(s)
            s_opens = rules[s]
            if type(s_opens) != list:
                s_opens = [s_opens]
            for s_open in s_opens:
                first = First(s_open, rules, VT, VN, ls)
                ls=ls[:-1]
                set_first = set_first | first
            if KESI in set_first:
                set_first.remove(KESI)
                continue
            else:
                return set_first
        else:  # 最后一个字符情况
            set_first.add(KESI)
            return set_first


def Follow(st, rules, VT, VN, list_a=[]):
    set_follow = set()
    flag = 0
    lefts = rules.keys()
    for left in lefts:
        num = list_a.count(st)
        if num > 1:
            continue
        rights = rules[left]
        if type(rights) != list:
            rights = [rights]
        for right in rights:
            for dir in range(len(right)):
                if right[dir] == st:
                    flag = 1
                    if dir == len(right) - 1:
                        set_follow.add(TERMINATOR)
                        # num_before=len(set_follow)
                        list_a.append(left)
                        set_follow = set_follow | Follow(left, rules, VT, VN, list_a)
                        list_a = list_a[:-1]
                        # if (num_before==len(set_follow)):
                        #

                    else:
                        ls=[]
                        fir = First(right[dir + 1:], rules, VT, VN,ls)
                        if KESI in fir:
                            fir.remove(KESI)
                            fir.add(TERMINATOR)
                            set_follow = fir | set_follow | Follow(left, rules, VT, VN, list_a)
                            pass
                        else:
                            set_follow = fir | set_follow
    if not flag:
        set_follow.add(TERMINATOR)
    return set_follow


def Select(st, rules, VT, VN):
    ls=[]
    first_1 = First(st[1], rules, VT, VN,ls)
    if KESI in first_1:
        first_1.remove(KESI)
        s = Follow(st[0], rules, VT, VN, [])
        return (first_1 | Follow(st[0], rules, VT, VN, []))
    else:
        return first_1

def Closure(I_add,vn,grammar):
    I_add_index = 0
    while I_add_index < len(I_add):
        I_add_project = I_add[I_add_index]
        if I_add_project[2] < I_add_project[3] and I_add_project[1][I_add_project[2]] in vn:
            for I0 in grammar:
                if I0[0] == I_add_project[1][I_add_project[2]] and I0 not in I_add:
                    I_add.append(I0)
        I_add_index += 1
    return sorted(I_add)

def Get_first(First, ls, rules1, VT0, VN0):
    ls_set = []
    ls = list(ls)
    first_set = dict()
    for i in ls:
        kong = []
        first_i = First(i, rules1, VT0, VN0, kong)
        ls_set.append(first_i)
        first_set[i] = first_i
        print('First({0})={1}'.format(i, first_i))
    return first_set


def Get_follow(Follow, ls, rules1, VT0, VN0):
    ls_set = []
    for i in ls:
        lss = []
        follow_i=Follow(i, rules1, VT0, VN0, lss)
        ls_set.append(follow_i)
        print('Follow({0})={1}'.format(i, follow_i))
    return ls_set


def Get_select(Select, ls, rules1, VT0, VN0):
    ls_set = dict()
    for i in ls:
        sels = Select(i, rules1, VT0, VN0)
        for sel in sels:
            ls_set[(i[0], sel)] = i[1]
    return ls_set

#
# rules0 = {'S': ['AB', 'bC'], 'A': ['b', KESI], 'B': ['aD', KESI], 'C': ['AD', 'b'], 'D': ['aS', 'c']}#page72
# rules1 = {'E': 'Te', 'e': ['+E', KESI], 'T': 'Ft', 't': ['T', KESI], 'F': 'Pf', 'f': ['*f', KESI],
#           'P': ['(E)', 'a', 'b', '^']}#page100第二题
# rules2 = {"Z": ["bMb"], "M": ["a", "(L"], "L": ["Ma)"]}
#
# rules3={"E":["E+T","T"],"T":['T*F','F'],'F':['i','(E)']}
# rules4={"E":["Te"],"e":["+Te",KESI],"T":["Ft"],'t':['*Ft',KESI],'F':['i','(E)']}


# vt, vn = Vt_Vn(rules0)
# follow_set = Get_follow(Follow, vn, rules0, vt, vn)
# vt, vn = Vt_Vn(rules1)
# follow_set = Get_follow(Follow, vn, rules1, vt, vn)
# vt, vn = Vt_Vn(rules2)
# follow_set = Get_follow(Follow, vn, rules2, vt, vn)
# vt, vn = Vt_Vn(rules3)
# follow_set = Get_follow(Follow, vn, rules3, vt, vn)
# vt, vn = Vt_Vn(rules4)

# Follow(t)={'@', '+'}
# Follow(F)={'@', '*'}
# Follow(E)={'@', ')'}
# Follow(T)={'@', '+'}
# Follow(e)={'@', ')'}


# follow_set = Get_follow(Follow, vn, rules4, vt, vn)

# rules0 = {'S': ['AB', 'bC'], 'A': ['b', KESI], 'B': ['aD', KESI], 'C': ['AD', 'b'], 'D': ['aS', 'c']}#page72
# rules1 = {'E': 'Te', 'e': ['+E', KESI], 'T': 'Ft', 't': ['T', KESI], 'F': 'Pf', 'f': ['*f', KESI],
#           'P': ['(E)', 'a', 'b', '^']}#page100第二题
# rules2 = {"Z": ["bMb"], "M": ["a", "(L"], "L": ["Ma)"]}
#
# rules3={"E":["E+T","T"],"T":['T*F','F'],'F':['i','(E)']}
# vt, vn = Vt_Vn(rules0)
# first_set = Get_first(First, vn, rules0, vt, vn)
# vt, vn = Vt_Vn(rules1)
# first_set = Get_first(First, vn, rules1, vt, vn)
# vt, vn = Vt_Vn(rules2)
# first_set = Get_first(First, vn, rules2, vt, vn)
# vt, vn = Vt_Vn(rules3)
# first_set = Get_first(First, vn, rules3, vt, vn)

# def Closure()

