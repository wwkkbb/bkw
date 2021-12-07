from function.func1 import First, Follow, Select, Vt_Vn, Closure
from collections import OrderedDict

KESI = '$'
TERMINATOR = '#'



def error_process(I_all_index, every_vt):
    return "error"


def get_i(grammar_original, grammar, vt, vn):
    Go_dic = dict()
    vt_vn = vt | vn
    # grammar = sorted(grammar)
    I_all = OrderedDict()
    I_all[0] = Closure([grammar[0]], vn, grammar)

    I_index = 0

    len_I_all = len(I_all)
    while I_index < len_I_all:
        I = I_all[I_index]
        for t_n in vt_vn:

            I_add = []
            for project in I:
                if project[2] < project[3] and project[1][project[2]] == t_n:
                    I_add.append([project[0], project[1], project[2] + 1, project[3]])
            if len(I_add) != 0:
                I_add = Closure(I_add, vn, grammar)
                values = I_all.values()
                if I_add not in values:
                    x = list(I_all.keys())[-1] + 1
                    I_all[x] = I_add
                else:
                    x = list(values).index(I_add)

                print("I{}=Go(I{},{})".format(x, I_index, t_n))
                Go_dic[(I_index, t_n)] = x
                # print(x , I_add)
        len_I_all = len(I_all)
        I_index += 1
    x_chongtu = []
    for x in list(I_all):
        I = I_all[x]
        flag = False
        for i_index in range(len(I)):
            if I[i_index][3] == I[i_index][2] and len(I) != 1:
                print("I{}产生冲突I{}:{}:".format(x, x, I))
                x_chongtu.append(x)
                flag = True
                break
        if flag:
            num_s = 0
            num_set = set()
            for i_index in range(len(I)):
                if I[i_index][3] == I[i_index][2]:
                    print("{}规约".format(I[i_index]))
                    s = Follow(I[i_index][0], grammar_original, vt, vn,[])
                    print("FOllow{}={}".format(I[i_index][0],s))
                    I[i_index].append(s)
                elif I[i_index][1][I[i_index][2]] in vt:
                    print("{}移进".format(I[i_index]))
                    s = {I[i_index][1][I[i_index][2]]}
                    I[i_index].append(s)
                num_s += len(s)
                num_set = num_set | s
                if len(num_set) != num_s:
                    print("该文法不可以通过SLR(1)处理，请更换文法")
                    return None
        print("I{}={}".format(x, I_all[x]))
    return I_all, Go_dic, x_chongtu


# I_start = (('S', 'aSe', 0, 3), ('S', 'B', 0,1), ('B', 'bBe', 0,3), ('B', 'C', 0,1), ('C', 'cCc', 0,3),
#   ('C', 'd', 0,1))
# ('#', 'S', 0, 1)意思： '#'：文法左侧，‘S':文法右侧，0:点所在的位置 1：右侧文法长度
# grammars = {'#': ['S'], 'S': ['UTa','Tb'],'U': ['US','e'],
#            'T': ['S','Sc','d']}

grammars = {
    'z': ['Z'],
    # # 语句分为执行语句和声明语句
    'Z': ['S', 'P'],
    # 执行语句
    'S': ['i(B)S', 'w(B)S', 'B;'], 'B': ['I=E', 'E'],
    'E': ['E+T', 'E-T', 'T'], 'T': ['T*F', 'T/F', 'F'], 'F': ['I', 'n', '(E)'],
    # 申明语句
    'P': ['QK;'], 'K': ['I=n', 'I'], 'Q': ['c', 'f', 'k']
}


vt, vn = Vt_Vn(grammars)
vt_vn = vt | vn
I_start = []
for grammar in grammars:
    grammar_opens = grammars[grammar]
    for grammar_open in grammar_opens:
        I_start.append([grammar, grammar_open, 0, len(grammar_open)])

I_all_go = get_i(grammars, I_start, vt, vn)
assert I_all_go != None, "错误"

I_all, Go_dic, chongtu = I_all_go

# 获得SLR(1)分析表
stack = [0]
for I_all_index in range(len(I_all)):
    I_all_chongfu = []
    if I_all_index in chongtu:
        for project in I_all[I_all_index]:
            if project[2] != project[3] and project[1][project[2]] in project[4]:  # 移进
                x = [Go_dic[(I_all_index, project[1][project[2]])],
                                                                 0]  # 0表示移进
                if project[1][project[2]] in I_all_chongfu:
                    continue
                else:
                    I_all_chongfu.append(x)
                    Go_dic[(I_all_index, project[1][project[2]])]=x
            else:
                for every_vt in vt | {TERMINATOR}:
                    print(project)
                    if every_vt in project[4]:
                        Go_dic[(I_all_index, every_vt)] = [[project[0], project[1]], 1]  # 1表示规约

    else:
        for project in I_all[I_all_index]:
            if project[2] != project[3]:  # 移进
                x = [Go_dic[(I_all_index, project[1][project[2]])], 0]  # 0表示移进
                if project[1][project[2]] in I_all_chongfu:
                    continue
                else:
                    I_all_chongfu.append(project[1][project[2]])
                    Go_dic[(I_all_index, project[1][project[2]])] = x
            else:
                if project[0:3]== [I_start[0][0], I_start[0][1], I_start[0][3]]:
                    Go_dic[(I_all_index, TERMINATOR)] = [[project[0], project[1]], 2]  # 2表示规约接受
                else:
                    for every_vt in vt | {TERMINATOR}:
                        Go_dic[(I_all_index, every_vt)] = [[project[0], project[1]], 1]  # 1表示规约

print('-----------------------------------------')
vt_vn_TERMINOR = vt_vn | {TERMINATOR}
for I_all_index in range(len(I_all)):
    for every_vt in vt_vn_TERMINOR:
        if (I_all_index, every_vt) in Go_dic:
            print(Go_dic[(I_all_index, every_vt)], end='')
        else:
            Go_dic[(I_all_index, every_vt)] = error_process(I_all_index, every_vt)
            print(Go_dic[(I_all_index, every_vt)], end='')

    print("\n")

# 使用token表
yingshe = {1: 'i', 4: 'w', 8: 'f', 9: 'k', 10: 'c', 11: 'I', 12: 'n', 13: '+', 14: '-', 15: '*', 16: '/', 28: '=',
           31: '(', 32: ')', 33: '{', 34: '}', 35: ';', 38: '#'}
with open(r'E:\studyclass3first\Compilers_Principles\code1\bkw\token.txt', 'r') as f:
    st = f.readlines()
input_ = ''
for i in range(len(st) - 1, -1, -1):
    st[i] = eval((st[i][:-1]))
    if st[i][1] == 37:
        st.remove(st[i])
    else:
        input_ += yingshe[st[i][1]]
stack_states = [0]
stack_fuhao = ['#']
stack_input = list(input_[::-1])
print('-----------------------------------------------------------')

while(True):
    print(stack_states,stack_fuhao,stack_input)
    action = Go_dic[(stack_states[-1], stack_input[0])]
    if action[1]==2:#接受
        print("acc")
        break
    elif action[1]==1:#规约
        stack_fuhao=stack_fuhao[:-len(action[0][1])]+[action[0][0]]
        stack_states=stack_states[:-len(action[0][1])]
        x=Go_dic[(stack_states[-1],stack_fuhao[-1])]
        if x!='error':
            stack_states.append(x[0])
        else:
            print("error",stack_input[i])
            break
    elif action[1]==0:#移进
        stack_states.append(action[0])
        stack_fuhao.append(stack_input[0])
        stack_input=stack_input[1:]
    else:
        print(action)
        break