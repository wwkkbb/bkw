"""
@author: lishihang
@software: PyCharm
@file: TreeVis.py
@time: 2018/11/29 22:20
"""

TERMINATOR=''
KESI=''
from function.func import First
from graphviz import Digraph

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
def plot_model(tree, name):
    g = Digraph("G", filename=name, format='png', strict=False)
    first_label = list(tree.keys())[0]
    g.node("0", first_label)
    _sub_plot(g, tree, "0")
    g.view()


root = "0"


def _sub_plot(g, tree, inc):
    global root

    first_label = list(tree.keys())[0]
    ts = tree[first_label]
    for i in ts.keys():
        if isinstance(tree[first_label][i], dict):
            root = str(int(root) + 1)
            g.node(root, list(tree[first_label][i].keys())[0])
            g.edge(inc, root, str(i))
            _sub_plot(g, tree[first_label][i], root)
        else:
            root = str(int(root) + 1)
            g.node(root, tree[first_label][i])
            g.edge(inc, root, str(i))


d1 = {"no surfacing": {0: "no", 1: {"flippers": {0: "no", 1: "yes"}}}}

d2 = {'tearRate': {'reduced': 'no lenses', 'normal': {'astigmatic': {'yes': {
    'prescript': {'myope': 'hard', 'hyper': {'age': {'young': 'hard', 'presbyopic': 'no lenses', 'pre': 'no lenses'}}}},
    'no': {'age': {'young': 'soft', 'presbyopic': {
        'prescript': {'myope': 'no lenses',
                      'hyper': 'soft'}},
                   'pre': 'soft'}}}}}}

plot_model(d1, "hello.gv")
plot_model(d2, "hello2.gv")
