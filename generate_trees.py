#%%
from binarytree import tree
t = tree()
t.pprint()
print(t.values)
#%%
from binarytree import tree

def normalize(tree, row=0, col=0):
    try:
        node = tree[(2**row-1)+col]
        if (node is None): return []
        left  = normalize(tree, row+1, col*2)
        right = normalize(tree, row+1, col*2+1)
        if (left is not None and right is not None): return [node, [left, right]]
        if (left is not None): return [node,[left,[]]]
        if (right is not None): return [node,[right,[]]]
        return [node]
    except:
        return None # child index does not exist

def list2tikz(l):
    if l == []:
        return ""
    elif(len(l) == 1):
        return '""'
    else:
        return '""' + ' -- { ' + list2tikz(l[1][0]) + ', ' + list2tikz(l[1][1]) + '} '

def generateTikzBinaryTrees(n):
    print(r'\tikz[tree layout]\graph[nodes={draw, circle,fill=red!60!black}] {')
    for i in range(n):
        print(list2tikz(normalize(tree().values)) + ';')
    print(r'};')

#%%
generateTikzBinaryTrees(10)

#%%
