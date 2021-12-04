# global count
# count=0
KESI = '@'#空串
TERMINATOR = '#'#终止符号


def legal_start(s):
    pass


def lower_case(s):
    if 'z' >= s >= 'a':
        return True
    else:
        return False


def upper_case(s):
    if 'Z' >= s >= 'A':
        return True
    else:
        return False


def VT0(s):
    if s in ['(', ')', 'a', 'b', '^', '+', '*']:
        return True
    else:
        return False


def VN0(s):
    if s in ['E', 'e', 'T', 't', 'F', 'f', 'P']:
        return True
    else:
        return False

def VT2(s):
    if s in ['(', ')', 'a', 'b']:
        return True
    else:
        return False


def VN2(s):
    if s in ['Z','L', 'M']:
        return True
    else:
        return False

def VT3(s):
    if s in ['(', ')', 'i', '+','*']:
        return True
    else:
        return False


def VN3(s):
    if s in ['E','e', 'T','t','F']:
        return True
    else:
        return False


def First(st, rules, VT, VN):
    # count+=1
    # print(count)
    # VT=set()
    # VN=set()
    # if X in VT:
    #     return {X}
    # else:
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
def Follow(st, rules, VT, VN,list_a):
    set_follow = set()
    flag = 0
    lefts = rules.keys()
    for left in lefts:
        num=list_a.count(st)
        if num>1:
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
                        set_follow=set_follow|Follow(left,rules,VT,VN,list_a)
                        list_a=list_a[:-1]
                        # if (num_before==len(set_follow)):
                        #

                    else:
                        fir = First(right[dir + 1:], rules, VT, VN)
                        if KESI in fir:
                            fir.remove(KESI)
                            fir.add(TERMINATOR)
                            set_follow = fir | set_follow|Follow(left,rules,VT,VN,list_a)
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

# rules0 = {'S': ['AB', 'bC'], 'A': ['b', KESI], 'B': ['aD', KESI], 'C': ['AD', 'b'], 'D': ['aS', 'c']}
# rules1 = {'E': 'Te', 'e': ['+E', KESI], 'T': 'Ft', 't': ['T', KESI], 'F': 'Pf', 'f': ['*f', KESI],
#           'P': ['(E)', 'a', 'b', '^']}


rules2={"Z":["bMb"],"M":["a","(L"],"L":["Ma)"]}
vt2=['Z','M','L']
# rules3={"E":["Te"],"e":["+Te",KESI],"T":["Ft"],'t':['*Ft',KESI],'F':['i','(E)']}
# vt3=['E','e', 'T','t','F']


VT=VT2
VN=VN2
vt=vt2
rules=rules2
# first_set_stS=First('S',rules,lower_case,upper_case)
# first_set_stA=First('A',rules,lower_case,upper_case)
# first_set_stB=First('B',rules,lower_case,upper_case)
# first_set_stC=First('C',rules,lower_case,upper_case)
# first_set_stD=First('D',rules,lower_case,upper_case)


# first=Get_first(First,['E','e','T','t','F','f','P'],rules1,VT0,VN0)
# follow=Get_follow(Follow,['E','e','T','t','F','f','P'],rules1,VT0,VN0)
# select=Get_select(Select,[["S",'AB'],['S','bC'],['A',KESI],["A","b"],["B",KESI],["B","aD"],["C","AD"],["C","b"],["D","aS"],["D","c"]],rules1,VT0,VN0)

first=Get_first(First,vt,rules,VT,VN)
follow=Get_follow(Follow,vt,rules,VT,VN)
ls=[]
for rule in rules:
    rights=rules[rule]
    for right in rights:
        ls.append([rule,right])
print(ls)
select=Get_select(Select,ls,rules,VT,VN)
st=input("请输入字符串：")+TERMINATOR
print(ls)
stack=ls[0][0]+TERMINATOR
index=1
biao=[]
while True:
    if st==None:#判断空串
        break
    s=[index,stack,st]
    index+=1
    if stack[0]==st[0]:
        if stack==TERMINATOR:#接受
            print("成功")
            tuidao="接受"

        else:#匹配
            tuidao=stack[0]+"匹配"
            stack=stack[1:]
            st=st[1:]
    elif (stack[0],st[0]) in select:#推导
        sel=select[(stack[0],st[0])]
        tuidao=stack[0]+'->'+sel
        if sel==KESI:
            stack=stack[1:]
        else:
            stack=sel+stack[1:]
    else:#错误
        print("在第{0}步骤出现error".format(index-1),st[0])
        st=st[1:]
    s.append(tuidao)
    print(s)
    biao.append(s)

    if tuidao=='接受':
        break
    tuidao='错误'
for i in biao:
    print(i)



