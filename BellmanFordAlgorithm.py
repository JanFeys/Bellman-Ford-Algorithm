#!/usr/bin/env python3

import time
from collections import defaultdict
import sys

class WeightedDirectedGraph():
    def __init__(self, nr_vs):
        self.nr_vs = nr_vs #number of vertices
        self.es = defaultdict(set) #dictionary of sets that, for every vertex, stores head of edges leaving it
        self.ws = dict() #dictionary that stores weight of each edge

    def show_nr_vs(self):
        return self.nr_vs

    def add_edge(self, t, h, w):
        (self.es[t]).add(h)
        self.ws[(t,h)] = w

    def get_edges(self, t):
        return self.es[t]
    
    def get_weight(self,t,h):
        return self.ws[(t,h)]

    def removeEdge(self, t, h):
        (self.es[t]).remove(h)
        del self.ws[(t,h)]

    def display(self):
        nr_es_present = 0
        for t in self.es:
            for h in self.es[t]:
                print("edge from %s to %s with weight %s" % (t, h, self.ws[(t,h)]))
                nr_es_present += 1
        print("there are %s edges in total" % nr_es_present)

    def run_Bellman_Ford(self,s):
        self.A = []
        self.A.append([sys.maxsize for v in range(self.nr_vs)])
        self.A[0][s] = 0

        k = 1
        while k<self.nr_vs:
            print('k=',k)
            self.A.append(self.A[k-1][:])
            for w in range(self.nr_vs):
                for v in self.es[w]:
                    self.A[k][v] = min(self.A[k][v],self.A[k-1][w]+self.ws[(w,v)])
            if self.A[k][:] == self.A[k-1][:]:
                break
            k = k+1
        else:
            return None
    
        return self.A[-1][:]

if __name__ == "__main__":
    file_name =  'BellmanFordsimpletest1.txt'

    start_time = time.time()

    with open(file_name, 'r') as f:
        nr_vs, _ = f.readline().strip().split()
        nr_vs = int(nr_vs)
        graph = WeightedDirectedGraph(nr_vs)

        for line in f:
            t, h, w = line.strip().split()
            t, h, w = int(t)-1, int(h)-1, int(w)
            graph.add_edge(t,h,w)

    start = 0

    shortest_paths = graph.run_Bellman_Ford(start)

    end_time = time.time()
    print(end_time - start_time)
    
    if (shortest_paths == None):
        print('negative cycle detected')
    else:
        for v in range(nr_vs):
            print("from %s to %s shortest path is %s" % (start, v, shortest_paths[v]))


