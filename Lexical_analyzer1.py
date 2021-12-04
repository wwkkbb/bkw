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


class Consl:
    def __init__(self, st, index):
        self.st = st
        self.index = index


def informationword(st):
    index = 0
    flag = 1
    ls = []
    namel_index = 0
    consl_index = 0
    dict_namel = dict()
    ls_consl = []
    ls_false = []
    while (index < len(st)):
        # 删除空格
        if st[index] == ' ':
            index += 1
            if st[index] == '#':
                break
        # 判断是否是标识符或者关键字
        elif (st[index] <= 'Z' and st[index] >= 'A') or (st[index] <= 'z' and st[index] >= 'a'):
            head = index
            index += 1
            while (st[index] <= 'Z' and st[index] >= 'A') or (st[index] <= 'z' and st[index] >= 'a') or (
                    st[index] <= '9' and st[index] >= '0'):
                index += 1
            tail = index
            if st[head:tail] in key_word:
                ls.append(InformationGrammar("关键字", key_word[st[head:tail]], st[head:tail]))
            else:
                ls.append(InformationGrammar("标识符", 11, st[head:tail], namel_index))  # 指针
                namel_index += 1
                dict_namel[ls[-1].z.st] = (index)
        # 判断整数和浮点数
        elif st[index] <= '9' and st[index] >= '0':
            head = index
            index += 1
            if st[index] == '.':
                index += 1
                while st[index] <= '9' and st[index] >= '0':
                    index += 1
                tail = index
                ls.append(InformationGrammar("float", 12, st[head:tail], consl_index))  # 浮点数
            elif st[index] <= '9' and st[index] >= '0':
                index += 1
                while st[index] <= '9' and st[index] >= '0':
                    index += 1
                if st[index] == '.':
                    index += 1
                    while st[index] <= '9' and st[index] >= '0':
                        index += 1
                    tail = index
                    ls.append(InformationGrammar("float", 12, st[head:tail], consl_index))  # 浮点数

                else:
                    index += 1
                    tail = index
                    ls.append(InformationGrammar("int", 12, st[head:tail], consl_index))  # 整数

            else:
                tail = index
                ls.append(InformationGrammar("int", 12, st[head:tail], consl_index))  # 整数
            ls_consl.append(ls[-1].z)
            consl_index += 1

        elif st[index] == '+':
            ls.append(InformationGrammar(st[index], 13))
            index += 1
        elif st[index] == '-':
            ls.append(InformationGrammar(st[index], 14))
            index += 1
        elif st[index] == '*':
            ls.append(InformationGrammar(st[index], 15))
            index += 1
        elif st[index] == '/':
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

        elif st[index] == "\n":
            # if st[index + 1] != 'n':
            #     ls_false.append(st[index])
            #     index += 1
            # else:
            #     ls.append(InformationGrammar(st[index:index + 2], 37))
            #     index += 2
            ls.append(InformationGrammar(st[index], 37))
            index += 1
        elif st[index] == '#':
            ls.append(InformationGrammar(st[index], 38))
            break
        else:
            ls_false.append(st[index])
            index += 1
    return ls, dict_namel, ls_consl, ls_false


st = '\n 2$.23 if 234.45>= [ ], av av er + cd =  ,234.45 #'
print(st[0])
ls, dict_namel, ls_consl, ls_false = informationword(st)
sll=str(ls)
print(11)
