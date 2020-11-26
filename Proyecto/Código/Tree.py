# Tree Implementation

import math
from graphviz import Digraph
import os

def class_counts(data):
    classes = {}
    for row in data:
        label = row[-1]
        if label not in classes:
            classes[label] = 0
        classes[label] += 1
    return classes

def is_number(value):
    return isinstance(value, int) or isinstance(value, float)

def critical_values(data, column):
    values = {} #creates a values dictionary
    for row in data:
        dato = row[column] # stores all possible values a given column can take
        if dato not in values:
            values [dato] = 0
        values [dato] += int(row[-1])
    bestValue = None
    worstValue = None
    bestSuccess = 0
    worstSucces = len(data)
    for val in values: # determines which is the value that has most success cases.
        if (values[val] >= bestSuccess): 
            bestSuccess = values[val]
            bestValue = val
        if (values[val] <= worstSucces):
            worstSucces = values[val]
            worstValue = val

    return bestValue, worstValue
    
def partition(data, question):
    true_rows, false_rows = [], []
    for row in data:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

def gini(data):
    counts = class_counts(data)
    impurity = 1
    for label in counts:
        prob_of_lbl = counts[label] / float(len(data))
        impurity -= prob_of_lbl**2
    return impurity

def entropy(data):
    counts = class_counts(data)
    impurity = 0
    for label in counts:
        prob_of_lbl = counts[label] / float(len(data))
        impurity -= prob_of_lbl * math.log2(prob_of_lbl)
    return impurity

def info_gain(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def info_gain_e(left, right, current_uncertainty):
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * entropy(left) - (1 - p) * entropy(right)

def find_best_split_CART(data, header):
    best_gain = 0
    best_question = None
    current_uncertainty = gini(data)
    n_features = len(header) - 1

    for column in range(n_features):

        values = critical_values(data, column)

        for val in values:

            question = Question(column, val, header)
            true_rows, false_rows = partition(data, question)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain(true_rows, false_rows, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question

def find_best_split_ID3(data, header):
    best_gain = 0
    best_question = None
    current_uncertainty = entropy(data)
    n_features = len(header) - 1

    for column in range(n_features):
    
        values = critical_values(data, column)

        for val in values:
            
            question = Question(column, val, header)
            true_rows, false_rows = partition(data, question)

            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            gain = info_gain_e(true_rows, false_rows, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question

def build_CART_tree(data, header, limit = -1):

    if limit == 0:
        return Leaf(data)

    gain, question = find_best_split_CART(data, header)

    if gain == 0:
        return Leaf(data)

    true_rows, false_rows = partition(data, question)

    true_child = build_CART_tree(true_rows, header, limit - 1)
    false_child = build_CART_tree(false_rows, header, limit - 1)

    return DecisionNode(question, true_child, false_child)

def build_ID3_tree(data, header, limit = -1):
    
    if limit == 0:
        return Leaf(data)

    gain, question = find_best_split_ID3(data, header)

    if gain == 0:
        return Leaf(data)

    true_rows, false_rows = partition(data, question)

    true_child = build_ID3_tree(true_rows, header, limit - 1)
    false_child = build_ID3_tree(false_rows, header, limit - 1)

    return DecisionNode(question, true_child, false_child)

def import_tree():
    r = str(input("Ingrese el nombre del archivo a leer: "))
    print()
    os.system("pause")
    os.system("cls")
    print("Leyendo...\n")
    f = open(r, "r")
    header = f.readline()
    header = header[2:len(header)-2].split("', '")
    header[-1] = header[-1][0:len(header[-1])-2]
    tree = DefaultTree(read_node(f, header), header)
    return tree
    
def read_node(f, header):
    s = f.readline()
    if s == "" or s == None:
        return None
    s = s.split()
    question = ""
    if s[0] == "Is":
        t = s[3][0:len(s[3])-1]
        try:
            t = int(t)
            question = Question(header.index(s[1]), t, header)
        except(ValueError):
            try:
                t = float(t)
                question = Question(header.index(s[1]), t, header)
            except(ValueError):
                question = Question(header.index(s[1]), t, header)
        f.readline()
        true_child = read_node(f, header)
        f.readline()
        false_child = read_node(f, header)
        return DecisionNode(question, true_child, false_child)
    elif len(s) == 5:
        data = [[int(s[1][1])]]*int(s[2][0:len(s[2])-1]) + [[int(s[3][0])]]*int(s[4][0:len(s[4])-1])
        return Leaf(data)
    else:
        data = [[int(s[1][1])]]*int(s[2][0:len(s[2])-1])
        return Leaf(data)

class Question:

    def __init__(self, column, value, header):
        self.column = column
        self.value = value
        self.header = header

    def match(self, data):
        val = data[self.column]
        if is_number(val) and is_number(self.value):
            return val >= self.value
        else:
            return str(val) == str(self.value)

    def __str__(self):
        condition = "=="
        if is_number(self.value):
            condition = ">="
        return "Is %s %s %s?" % (self.header[self.column], condition, str(self.value))

class Leaf:

    def __init__(self, data):
        self.predictions = class_counts(data)

    def imprimir(self, spacing = ""):
        return spacing + "Prediction: " + str(self.predictions)

    def graph(self, digraph, name):
        try:
            p = round((self.predictions.get(1)/(sum(self.predictions.values()) * 1.0)) * 100, 2)
        except(TypeError, ValueError):
            p = 0
        label = "Probability of success: " + str(p) + "%"
        color = "red"
        if p > 50.0:
            color = "orange"
        if p > 60.0:
            color = "gold"
        if p > 75.0:
            color = "cyan"
        if p > 90.0:
            color = "lime"
        digraph.node(name, label, style = "filled", color = color)
        return digraph

class DecisionNode:

    def __init__(self, question, true_child, false_child):
        self.question = question
        self.true_child = true_child
        self.false_child = false_child

    def imprimir(self, spacing = ""):
        s = spacing + str(self.question) + "\n" + spacing + "--> True:" + "\n" + self.true_child.imprimir(spacing + "  ")  + "\n" + spacing + "--> False:" + "\n" + self.false_child.imprimir(spacing + "  ")
        return s
    
    def graph(self, digraph, name):
        digraph.node(name, str(self.question)[3:len(str(self.question))-1], style = "filled")
        digraph = self.true_child.graph(digraph, name + 't')
        digraph.edge(name, name + 't', 'True')
        digraph = self.false_child.graph(digraph, name + 'f')
        digraph.edge(name, name + 'f', 'False')
        return digraph

class CARTTree:

    def __init__(self, data, header, limit = -1):
        self.root = build_CART_tree(data, header, limit)
        self.header = header

    def __str__(self):
        return str(self.header) + "\n" + self.root.imprimir()

    def graphic(self):
        digraph = Digraph(format = "png")
        return self.root.graph(digraph, 'r')


class ID3Tree:
    
    def __init__(self, data, header, limit = -1):
        self.root = build_ID3_tree(data, header, limit)
        self.header = header

    def __str__(self):
        return str(self.header) + "\n" + self.root.imprimir()

    def graphic(self):
        digraph = Digraph(format = "png")
        return self.root.graph(digraph, 'r')

class DefaultTree:

    def __init__(self, root, header):
        self.root = root
        self.header = header

    def __str__(self):
        return str(self.header) + "\n" + self.root.imprimir()

    def graphic(self):
        digraph = Digraph(format = "png")
        return self.root.graph(digraph, 'r')

def classify(row, node):
    if isinstance(node, Leaf):
        return node.predictions

    if node.question.match(row):
        return classify(row, node.true_child)
    else:
        return classify(row, node.false_child)

def print_prediction(predictions):
    total = sum(predictions.values()) * 1.0
    probs = {}
    for lbl in predictions.keys():
        probs[lbl] = str(int(predictions[lbl] / total * 100)) + "%"
    return probs