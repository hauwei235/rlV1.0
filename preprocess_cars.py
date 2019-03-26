
f = open('C:/Users/txt/Desktop/match/huawei/car.txt')
file2 = open("C:/Users/txt/Desktop/match/huawei/new_car.txt",'w')
for line in f.readlines():
    if line == '\n':
        line = line.strip('\n')
    if '#' in line:
        continue
    file2.write(line)
f.close()
file2.close()

#(id,from,to,speed,planTime)


# class car_set():
#     def __init__(self):
#         pass
#     def car_list(self):
#         carlist = []
#         while True:
#             line = f.readline()
#             #print(line)
#             if line:
#                 road_id =line.split(',')[0].strip().strip('(')
#                 #print(road_id)
#                 start_node = int(line.split(',')[4])
#                 end_node = int(line.split(',')[5])
#                 speed_limit  = int(line.split(',')[2])
#                 nodelist.append(start_node)
#                 nodelist = list(set(nodelist))
#                 #print (nodelist)
#                 g.add_nodes_from(nodelist)
#                 weight = float(int(line.split(',')[1]))
#                 is_double = line.split(',')[6].strip().strip(')')
#                 if is_double =='1':
#                     g.add_edges_from([(start_node,end_node,{'weight':weight,'speed_limit':speed_limit,'road_id':road_id}),(end_node,start_node,{'weight':weight,'speed_limit':speed_limit,'road_id':road_id})])
#                     #print ('double')
#                 else :
#                     g.add_edges_from([(start_node,end_node,{'weight':weight,'speed_limit':speed_limit,'road_id':road_id})])
#                     # g.add_weighted_edges_from([(start_node,end_node,weight)])
#                     #print ('not')
#             else :
#                 break
#         #nx.draw_networkx(g,arrows=True,with_labels=True)
#         #plt.show()
#         return g
#
# # neighbor = []
# #print (g.number_of_edges())
# for i in nx.all_neighbors(g,1):
#     neighbor.append(i)
# neighbor = list(sorted(set(neighbor)))
# print (neighbor[-1])

#nx.draw_networkx(g,arrows=True,with_labels=True)
#plt.show()
