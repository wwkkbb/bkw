'''经过化简
S->aSe
S->B
B->bBe
B->C
C->cCc
C->d
'''

#I的四个参数分别表示项目的左侧，右侧，点所在的索引，右侧的长度。
# I=[{('S','aSe',0,3),('S','aSe',0),('S','B',0),('B','bBe',0),('B','C',0),('C','cCc',0),('C','d',0)}]
# I_num=1
# index=0
# while(I_num>index):
#     for f in factor:
#         for i in I:
#             if i[2]<i[3]:
#                 pass


rules0 = {'S': ['aSe', 'B'],  'B': ['bBe', 'C'], 'C': ['cCc', 'd']}




def func(st):
    stack=''
    index=0
    while(True):
        if index==len(st):
            if stack=='':
                print("成功")
                break
            else:
                print("错误")
                break
        if index==0:
            if st[index]=='a':
                stack+='Se'
                index+=1
                continue
            else:
                stack+='B'
                continue
        else:
            if stack=='':
                print("错误")
                break
            if st[index]==stack[0]:
                index+=1
                stack=stack[1:]
                continue
            else:
                if stack[0] in ['S','B','C']:
                    ls=rules0[stack[0]]
                    if stack[0]=='S':
                        if st[index]=='a':
                            stack=ls[0]+stack[1:]
                            continue
                        elif st[index] in ['b','c','d']:
                            stack=ls[1]+stack[1:]
                            continue
                        else:
                            print('错误')
                            break
                    elif stack[0]=='B':
                        if st[index]=='b':
                            stack=ls[0]+stack[1:]
                            continue
                        elif st[index] in ['c','d']:
                            stack=ls[1]+stack[1:]
                            continue
                        else:
                            print('错误')
                            break
                    elif stack[0]=='C':
                        if st[index]=='c':
                            stack=ls[0]+stack[1:]
                            continue
                        elif st[index]in ['d']:
                            stack=ls[1]+stack[1:]
                            continue
                        else:
                            print('错误')
                            break
                    continue
                else:
                    print("错误")
                    break


func('aabcdceee')