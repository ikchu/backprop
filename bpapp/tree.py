import random
import operator as op
from mpmath import *
from functools import reduce
from bpapp.models import Node, Problem

max_n = -1
varLowerBound = 1
varUpperBound = 5
Operations = ["+", "-", "*", "/", "^"]
Operation_dict = {"+" : lambda x,y: x + y,
                  "-" : lambda x,y: x - y,
                  "*" : lambda x,y: x * y, 
                  "/" : lambda x,y: x / y, 
                  "^" : lambda x,y: x ** y}


def ncr(v1, v2):
    r = min(v2, v1-v2)
    numer = reduce(op.mul, range(v1, v1-v2, -1), 1)
    denom = reduce(op.mul, range(1, v2+1), 1)
    return numer / denom
def catalan(v1):
    return ncr(2*v1, v1) / (v1 + 1)

def tree(n):
    global max_n
    max_n = n
    
    tree_init = tree_aux(n)

    forwardprop(tree_init)
    backprop(tree_init)
    return tree_init
def tree_aux(n):
    if (n == 0): # return a leaf node
        return Node.objects.create(op = "v", fp = random.randint(varLowerBound, varUpperBound))
    else:
        kDraw = []
        # for each possible left subtree height 
        for k in range(0,n):
            p = int(catalan(k)*catalan(n-k-1))#/catalan(n)   NOTE: removing catalan(n) to keep probabilities as ints. They remain the same relative to each other
            # print('p:',p),
            for i in range(0,p):
                kDraw.append(k)
            # print('kdraw:', kDraw)
        k = random.choice(kDraw) # selecting one random k from the distribution
        # print('k:',k)

        # fp, bp uninitialized at start
        node =  Node.objects.create(l = tree_aux(k), r = tree_aux(n-k-1), op = random.choice(Operations))

        # if (n == max_n):
        #     node.bp = 1.00

        return node

def forwardprop(root):
    return forwardprop_aux(root)
def forwardprop_aux(node):
    if (node.op == "v"): # if reached a variable leaf node
        return node.fp
    else:
        fp = Operation_dict[node.op](forwardprop_aux(node.l), forwardprop_aux(node.r))
        node.fp = fp
        node.save()
        return fp

def backprop(root):
    return backprop_aux(root, 1.00)
def backprop_aux(node, bp):
    # suppose we are looking at node x, with parent node y
    # find local derivative dy/dx @fp_x
    # multiply local derivative by parent derivative bp_y

    node.bp = bp
    node.save()

    if (node.op != "v"): # as long as not on variable leaf node
        bp_left = diff(Operation_dict[node.op], (node.l.fp, node.r.fp), (1,0)) * bp
        bp_right = diff(Operation_dict[node.op], (node.l.fp, node.r.fp), (0,1)) * bp

        backprop_aux(node.l, bp_left)
        backprop_aux(node.r, bp_right)

def getDataForTemplate(root, showAll):
    data = getData_aux(root, None, showAll)
    return [ data ]
def getData_aux(node, parent, showAll):
    nodeData = {}
    # if we should show everything (variables, fp values, bp values, etc. )
    if showAll:
        nodeData["name"] = node.allValues()
        if (parent is None):
            nodeData["parent"] = "null"
        else:
            nodeData["parent"] = parent.allValues()
    # if we should only show the initial values (variables, operations)
    else:
        nodeData["name"] = node.initialValues()
        if (parent is None):
            nodeData["parent"] = "null"
        else:
            nodeData["parent"] = parent.initialValues()

    if (node.op != "v"):
        nodeData["children"] = [getData_aux(node.l, node, showAll), getData_aux(node.r, node, showAll)]
    return nodeData
