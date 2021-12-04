KESI=''
TERMINATOR=''
rules2={"Z":["bMb"],"M":["a","(L"],"L":["Ma)"]}
vn=set()
vt=set()


def First(st, rules, VT, VN):
    st = st + TERMINATOR
    set_first = set()
    for s in st:
        if VT(s) or s == KESI:
            return {s}
        elif VN(s):
            s_opens = rules[s]
            if type(s_opens) != list:
                s_opens = [s_opens]
            for s_open in s_opens:
                first = First(s_open, rules, VT, VN)
                set_first = set_first | first
            if KESI in set_first:
                set_first.remove(KESI)
                continue
            else:
                return set_first
        else:  # 最后一个字符情况
            set_first.add(KESI)
            return set_first
def Follow(st, rules, VT, VN, list_a):
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
                        fir = First(right[dir + 1:], rules, VT, VN)
                        if KESI in fir:
                            fir.remove(KESI)
                            fir.add(TERMINATOR)
                            set_follow = fir | set_follow | Follow(left, rules, VT, VN, list_a)
                            pass
                        else:
                            set_follow = fir | set_follow
    if flag:
        set_follow.add(TERMINATOR)
    return set_follow
def Select(st, rules, VT, VN):
    first_1=First(st[1],rules,VT,VN)
    if KESI in first_1:
        first_1.remove(KESI)
        s=Follow(st[0],rules,VT,VN,[])
        return (first_1|Follow(st[0],rules,VT,VN,[]))
    else:
        return first_1
def Get_first(First,ls,rules1,VT0,VN0):
    ls_set = []
    for i in ls:
        ls_set.append(First(i, rules1, VT0, VN0))
    return ls_set
def Get_follow(Follow,ls,rules1,VT0,VN0):
    ls_set=[]
    for i in ls:
        lss=[]
        ls_set.append(Follow(i,rules1,VT0,VN0,lss))
    return ls_set
def Get_select(Select,ls,rules1,VT0,VN0):
    ls_set=dict()
    for i in ls:
        sels=Select(i,rules1,VT0,VN0)
        for sel in sels:
            ls_set[(i[0],sel)]=i[1]
    return ls_set

# def Closure()