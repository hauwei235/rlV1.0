import networkx as nx
import matplotlib.pyplot as plt
g = nx.DiGraph()
f = open('C:/Users/txt/Desktop/match/huawei/new.txt')
#(道路id，道路长度，最高限速，车道数目，起始点id，终点id，是否双向)
# 这是啥

class graph_set():
    def __init__(self):
        pass
    def draw(self):
        nodelist = []
        while True:
            line = f.readline()
            if line:
                start_node = int(line.split(',')[4])
                end_node = int(line.split(',')[5])
                speed_limit  = int(line.split(',')[2])
                nodelist.append(start_node)
                nodelist = list(set(nodelist))
                #print (nodelist)
                g.add_nodes_from(nodelist)
                weight = float(int(line.split(',')[1]))
                is_double = line.split(',')[6].strip().strip(')')
                if is_double =='1':
                    g.add_edges_from([(start_node,end_node,{'weight':weight,'speed_limit':speed_limit}),(end_node,start_node,{'weight':weight,'speed_limit':speed_limit})])
                    #print ('double')
                else :
                    g.add_weighted_edges_from([(start_node,end_node,weight)])
                    #print ('not')
            else :
                break
        #nx.draw_networkx(g,arrows=True,with_labels=True)
        #plt.show()
        return g
#graph_set().draw()
# neighbor = []
# #print (g.number_of_edges())
# for i in nx.all_neighbors(g,1):
#     neighbor.append(i)
# neighbor = list(sorted(set(neighbor)))
# print (neighbor[-1])

#nx.draw_networkx(g,arrows=True,with_labels=True)
#plt.show()
