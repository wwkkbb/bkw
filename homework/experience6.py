from function.func import First,Follow,Select,Get_first,Get_follow,Get_select

KESI = '@'#空串
TERMINATOR = '#'#终止符号
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

rules2={"Z":["bMb"],"M":["a","(L"],"L":["Ma)"]}
vt2=['Z','M','L']
# rules3={"E":["Te"],"e":["+Te",KESI],"T":["Ft"],'t':['*Ft',KESI],'F':['i','(E)']}
# vt3=['E','e', 'T','t','F']


VT=VT2
VN=VN2
vt=vt2
rules=rules2

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
tuidao=''
while True:
    if st=='' :#判断空串
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
