key_word = {"if": 1,
            "else": 2,
            "for": 3,
            "while": 4,
            "break": 5,
            "return": 6,
            "continue": 7,
            "float": 8,
            "int": 9,
            "char": 10,}

#处理注释
#记录行数

class InformationGrammar:

    def __init__(self, x, y, z=None, index=None):
        self.x = x  # 单词
        self.y = y  # 编码
        self.z = z  # 语义
        if y == 11:
            self.z = Namel(z, index)
        if y == 12:
            self.z = Consl(z, index)


class Namel:
    def __init__(self, st, index):
        self.st = st
        self.index = index

    def all(self):
        return self.st,self.index

class Consl:
    def __init__(self, st, index):
        self.st = st
        self.index = index
    def all(self):
        return self.st,self.index

def informationword(st):
    index = 0
    count_row = 1
    flag = 1
    ls = []
    namel_index = 0
    consl_index = 0
    dict_namel = []
    ls_consl = []
    ls_false = []
    while (index < len(st)):
        # 删除空格
        if st[index] == ' ' or st[index]=='\t':
            index += 1
            if st[index] == '#':
                break
        # 判断是否是标识符或者关键字
        elif (st[index] <= 'Z' and st[index] >= 'A') or (st[index] <= 'z' and st[index] >= 'a') or st[index]=='_':
            head = index
            index += 1
            while (st[index] <= 'Z' and st[index] >= 'A') or (st[index] <= 'z' and st[index] >= 'a') or (
                    st[index] <= '9' and st[index] >= '0'or st[index]=='_'):
                index += 1
            tail = index
            if st[head:tail] in key_word:
                ls.append(InformationGrammar("关键字", key_word[st[head:tail]], st[head:tail]))
            else:
                ls.append(InformationGrammar("标识符", 11, st[head:tail], namel_index))  # 指针
                dict_namel.append(ls[-1].z)
                namel_index += 1
        # 判断整数和浮点数
        elif st[index] <= '9' and st[index] >= '0':
            head = index
            index += 1
            if st[index] == '.':
                index += 1
                while st[index] <= '9' and st[index ] >= '0':
                    index += 1
                tail = index
                ls.append(InformationGrammar("浮点数", 12, st[head:tail], consl_index))  # 浮点数
            elif st[index] <= '9' and st[index] >= '0':
                index += 1
                while st[index] <= '9' and st[index] >= '0':
                    index += 1
                if st[index] == '.':
                    index += 1
                    while st[index] <= '9' and st[index] >= '0':
                        index += 1
                    tail = index
                    ls.append(InformationGrammar("浮点数", 12, st[head:tail], consl_index))  # 浮点数

                else:
                    index += 1
                    tail = index
                    ls.append(InformationGrammar("整数", 12, st[head:tail], consl_index))  # 整数

            else:
                tail = index
                ls.append(InformationGrammar("整数", 12, st[head:tail], consl_index))  # 整数
            ls_consl.append(ls[-1].z)
            consl_index += 1

        elif st[index] == '+':


            if st[index + 1] == '=':
                ls.append(InformationGrammar(st[index:index + 2], 39))
                index += 2
            elif st[index + 1] == '+':
                ls.append(InformationGrammar(st[index:index + 2], 40))
                index += 2
            else:
                ls.append(InformationGrammar(st[index], 13))
                index += 1

        elif st[index] == '-':
            if st[index + 1] == '=':
                ls.append(InformationGrammar(st[index:index + 2], 41))
                index += 2
            elif st[index + 1] == '+':
                ls.append(InformationGrammar(st[index:index + 2], 42))
                index += 2
            else:
                ls.append(InformationGrammar(st[index], 14))
                index += 1
        elif st[index] == '*':

            if st[index + 1] == '=':
                ls.append(InformationGrammar(st[index:index + 2], 43))
                index += 2
            else:
                ls.append(InformationGrammar(st[index], 15))
                index += 1

        elif st[index] == '/':
            if st[index + 1] == '=':
                ls.append(InformationGrammar(st[index:index + 2], 44))
                index += 2
            elif st[index + 1] == '/': #处理单行注释
                # ls.append(InformationGrammar(st[index:index + 2], 45))
                index += 2
                while st[index]!="\n" :
                    index+=1
                index+=1
                count_row+=1
            elif st[index + 1] == '*':#处理多行注释
                # ls.append(InformationGrammar(st[index:index + 2], 46))
                index += 2
                while index<len(st)-1 and st[index]!='*':
                    if st[index+1]=='/':
                        index+=2
                        break
                    index+=1
            else:
                ls.append(InformationGrammar(st[index], 16))
                index += 1

        elif st[index] == '%':
            ls.append(InformationGrammar(st[index], 17))
            index += 1
        elif st[index] == '>':
            if st[index + 1] != '=':
                ls.append(InformationGrammar(st[index], 18))
                index += 1
            else:
                ls.append(InformationGrammar(st[index:index + 2], 19))
                index += 2
        elif st[index] == '<':
            if st[index + 1] != '=':
                ls.append(InformationGrammar(st[index], 20))
                index += 1
            else:
                ls.append(InformationGrammar(st[index:index + 2], 21))
                index += 2
        elif st[index] == '=':
            if st[index + 1] != '=':
                ls.append(InformationGrammar(st[index], 28))
                index += 1
            else:
                ls.append(InformationGrammar(st[index:index + 2], 23))
                index += 2
        elif st[index] == '!':
            if st[index + 1] != '=':
                ls.append(InformationGrammar(st[index], 24))
                index += 1
            else:
                ls.append(InformationGrammar(st[index:index + 2], 22))
                index += 2
        elif st[index] == '&':
            if st[index + 1] != '&':
                ls_false.append(st[index])
                index += 1
            else:
                ls.append(InformationGrammar(st[index:index + 2], 25))
                index += 2
        elif st[index] == '|':
            if st[index + 1] != '|':
                ls_false.append(st[index])
                index += 1
            else:
                ls.append(InformationGrammar(st[index:index + 2], 26))
                index += 2
        elif st[index] == ',':
            ls.append(InformationGrammar(st[index], 27))
            index += 1
        elif st[index] == '[':
            ls.append(InformationGrammar(st[index], 29))
            index += 1
        elif st[index] == ']':
            ls.append(InformationGrammar(st[index], 30))
            index += 1
        elif st[index] == '(':
            ls.append(InformationGrammar(st[index], 31))
            index += 1
        elif st[index] == ')':
            ls.append(InformationGrammar(st[index], 32))
            index += 1
        elif st[index] == '{':
            ls.append(InformationGrammar(st[index], 33))
            index += 1

        elif st[index] == '}':
            ls.append(InformationGrammar(st[index], 34))
            index += 1

        elif st[index] == ';':
            ls.append(InformationGrammar(st[index], 35))
            index += 1
        elif st[index] == '.':
            ls.append(InformationGrammar(st[index], 36))
            index += 1
        elif st[index] == '\'':
            ls.append(InformationGrammar(st[index], 47))
            index += 1
        elif st[index] == '\"':
            ls.append(InformationGrammar(st[index], 48))
            index += 1
        elif st[index] == "\n":
            # if st[index + 1] != 'n':
            #     ls_false.append(st[index])
            #     index += 1
            # else:
            #     ls.append(InformationGrammar(st[index:index + 2], 37))
            #     index += 2
            count_row+=1
            ls.append(InformationGrammar(st[index], 37))
            index += 1

        elif st[index] == '#':
            ls.append(InformationGrammar(st[index], 38))
            break
        else:
            ls_false.append(st[index])

            index += 1
            print("错误所在行：",count_row,"错误：",st[index-1])
    return ls, dict_namel, ls_consl, ls_false


def save_token(ls,path_token):
    token_list=[]
    for x in ls:
        if x.y == 12 or x.y == 11:
            token_list.append([x.x, x.y, [x.z.all()]])
        else:
            token_list.append([x.x, x.y, [' ']])

    print("token表：")
    for x in token_list:
        print(x)

    fileObject = open(path_token, 'w')
    for ip in token_list:
        fileObject.write(str(ip))
        fileObject.write('\n')
    fileObject.close()

    return token_list
def save_namel(ls_consl,path_consl):
    consl_list = []
    for x in ls_consl:
        consl_list.append(x.all())
    print("namel表：")
    for x in consl_list:
        print(x)
    fileObject = open(path_consl, 'w')
    for ip in consl_list:
        fileObject.write(str(ip))
        fileObject.write('\n')
def save_consl(ls_consl,path_consl):
    consl_list=[]
    for x in ls_consl:
        consl_list.append(x.all())
    print("consl表：")
    for x in consl_list:
        print(x)
    fileObject = open(path_consl, 'w')
    for ip in consl_list:
        fileObject.write(str(ip))
        fileObject.write('\n')
    return consl_list
print("实例：",'\n',
    "2.23 if 234.45>= [ ]\nav av er + cd =\n,234.45 \n#",'\n',
      "./token.txt",'\n',
      "./consl.txt",'\n',
      "./namel.txt")
st=''
print("请输入文件格式（1或0），若为1，则读取文件格式，若为0，则以字符串读取：")
x=input()

if x=='1':
    print(r"请输入文件名(文件以‘#’结束：如：'E:\studyclass3first\Compilers_Principles\code\dist\token.txt'")
    path = input()
    files= open(path)
    st=files.read()
    pass
else :
    print("请输入要分析的源程序（#结束）：")
    while True:
        st+=(input())
        if st[-1]=='#':
            break
        st+='\n'
ls, dict_namel, ls_consl, ls_false = informationword(st)
path_token='./token.txt'
path_consl='./consl.txt'
path_namel='./namel.txt'
path_token=input("请输入保存token表路径：")
path_consl=input("请输入保存consl表路径：")
path_namel=input("请输入保存namel表路径：")

print("token表含义：单词，编码类，语义（若为consl,则表示索引，数值。若为namel,则为标识符，索引） ")
print("consl表含义：索引，数值")
print("namel表含义：标识符，数值")
save_token(ls,path_token)
save_consl(ls_consl,path_consl)
save_namel(dict_namel,path_namel)
x=input()
token_list=[]
# with open('./token.txt') as file:
#     for line in file.readlines():
#         token_list.append(line.strip('\n'))
# print(token_list)
# files= open(r'E:\studyclass3first\Compilers_Principles\code\dist\token.txt','r')
# st=files.read()
# print(st)