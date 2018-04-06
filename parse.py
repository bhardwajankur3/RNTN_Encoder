from Tree import Node
import utils
from Train_LBFGS import Train_LBFGS

def stringToTree(s, loc):
    #print s[loc[0]:]
    #print loc[0]
    if loc[0]>= len(s):
        return None

    ind = 0
    while loc[0]+ind < len(s) and (s[loc[0]+ind]!='(' and s[loc[0]+ind]!=')') :
        ind+=1
    #print ind
    #print s[loc[0]:(loc[0]+ind)]
    res = Node(s[loc[0]:(loc[0]+ind)])
    loc[0]=loc[0]+ind

    if  s[loc[0]]=='(':
        loc[0]=loc[0]+1
        res.left = stringToTree(s,loc)
        loc[0]=loc[0]+1

    if  s[loc[0]]=='(':
        loc[0]=loc[0]+1
        res.right = stringToTree(s,loc)
        loc[0]=loc[0]+1

    return res

def stringToTreeWrapper(s):
    loc = [0]
    return stringToTree(s,loc)

def printInorder(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        #print root.data
        return [root.data]

    label=printInorder(root.left)+printInorder(root.right)
    print label
    return label

#my_string = "(ROOT (S (NP (PRP I)) (@S (VP (VBD shot) (NP (@NP (@NP (@NP (NP (DT an) (NN elephant)) (, ,)) (NP (NN rabbit))) (CC and)) (NP (NP (NN goat)) (PP (IN in) (NP (PRP$ my) (NNS pajamas)))))) (. .))))"
#my_string=my_string.replace("(","").replace(")","").replace("ROOT","")
#my_string="(ROOT (S (NP (PRP He)) (VP (VBD jumped) (PP (IN over) (NP (DT the) (NN wall))))))"
#s=my_string.split()

#content=''

f = open('out.txt', "r")
lines = list(f)
f.close()

#with open("out.txt") as f:
#    content=f.readlines

trees_train=[]
for my_string in lines:
    s=my_string.split()
    for i in range(len(s)):
        if s[i].endswith(')'):
            s[i]="("+s[i]+")"
    pre="".join(s)
    pre=pre[6:(len(pre)-1)]
    print pre
    root=stringToTreeWrapper(pre)
    trees_train.append(root)

#for tree in trees_train:
#    print tree.word_yield()

dictionary = utils.constructCompactDictionary(trees_train)
trainObj = Train_LBFGS(dictionary, trees_train)
optResult = trainObj.train()

#for i in range(len(s)):
#    if s[i].endswith(')'):
#        s[i]="("+s[i]+")"

#pre="".join(s)
#pre=pre[6:(len(pre)-1)]
#print pre

#root=stringToTreeWrapper(pre)
#print root
#print root.word_yield()
#print "Preorder traversal of the constructed tree:"
#printInorder(root)
#print "######Copied#####"
#printInorder(root.clone())


