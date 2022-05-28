import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
import psutil
import tkinter as tk
from tkinter import *
import pylab as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

names = ['Harshitha',"Teena","Sangeeta","Gulafshan"]
Harshitha = ["Aleena","Nibin","Sangeeta","Jennifer"]
Teena = ["Sangeeta","Teena","Gulafshan","Saurav"]
Sangeeta = ["Sangeeta","Joan","Aleena","Swarali"]
Gulafshan = ["Harshitha","Gulafshan","Jennifer","Swarali"]


hi = {}
hi[0] = Harshitha
hi[1] = Teena
hi[2] = Sangeeta
hi[3] = Gulafshan


class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
    
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
            if v1!=v2:
                self.adjMatrix[v2][v1] = 1
                self.adjMatrix[v1][v2] = 1
               
                g.graph4v(v1,v2)
            
    # Print the matrix
    def print_matrix(self):

        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val),end=" "),
            print()

    def graph4v(self,v1,v2):
            plt.plot([v2],[v1], '-ro', label='line & marker')
            plt.plot([v1],[v2], '-ro', label='line & marker')
            plt.annotate(names[v2],(v1,v2))
            plt.annotate(names[v2],(v2,v1))
            plt.tight_layout()


g = Graph(10)

for k in range(len(hi)):
    for i in hi[k]:
        for j in range(len(names)):
            if i == names[j]:
                g.add_edge(j,k)
                


                
print("ADJACENCY MATRIX :")
g.print_matrix()

labels = {}
for i in range(len(names)):
    labels[i]=names[i]
    
root = Tk()
root.title("GRAPH")

mlist = psutil.net_connections(kind="tcp")
fig = plt.figure(frameon=True, figsize=(5,1), dpi=100)
canvas = FigureCanvasTkAgg(fig, root)
Node = nx.Graph()

plt.gca().set_facecolor("grey")
fig.set_facecolor("black")

x = np.array(g.adjMatrix)
x = np.squeeze(x)

G = nx.from_numpy_matrix(np.array(x))  
nx.draw(G,labels = labels, with_labels=True)

canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
canvas.draw()

root.mainloop()

