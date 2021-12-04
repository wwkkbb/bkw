from function.func1 import First,Follow,Select,Get_first,Get_follow,Get_select,Vt_Vn

KESI = '$'
TERMINATOR = '@'

rules3={"E":["Te"],"e":["+Te",KESI],"T":["Ft"],'t':['*Ft',KESI],'F':['i','(E)']}
vt3=['E','e', 'T','t','F']


VT,VN=Vt_Vn(rules3)


vn=VN
rules=rules3

first=Get_first(First,vn,rules,VT,VN)
follow=Get_follow(Follow,vn,rules,VT,VN)
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
