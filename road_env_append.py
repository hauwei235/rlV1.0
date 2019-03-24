import networkx as nx
from graph_append import graph_set
# 现在应该所有的位置都考虑的是car[2]，也就是现在的位置，而不是初始的位置
class road():
    def __init__(self,reward = 0):
        self.reward = reward
    def travel(self,action,g,car=[]):
        #car[0] start_point ;car[1] end_point ;car[2] current_position ; car[3] speed
        map = g
        #print(map)
        # if car[2] ==car[0]:#应该是运行时间为0
        #     #车在起点
        #     check,car ,current_position,time= road().run(car=car,action=action,g=map)
        #     reward = reward - time
        #     #print(action)
        #     #print ('let''s go',car[2])
        # else:
        #     check,car,current_position = road().run(car=car,action=action,g=map)
        #     #print ('go on')
        check,car ,current_position,time= road().run(car=car,action=action,g=map)
        self.reward = self.reward - time
        flag_done = False
        if car[2] == car[1]:
            #print ('done')
            self.reward = self.reward +100
            flag_done = True
        #print(car[2])
        #print(car)
        return car[2],self.reward,flag_done,current_position
    def run(self,action,g,car=[]):
        map = g
        speed = car[3]
        time = 0
        # car[3] : car speed
        neighbor = []
        check=False
        #print (map)
        #print('car = ',car)
        car_position = car[2]
        #print('car position',car_position)
        action = int(action)
        for i in nx.all_neighbors(map,car_position):
            neighbor.append(i)
        neighbor = list(sorted(set(neighbor)))
        current_position = car_position
        if action == 0:
            #up
            if ((car_position-neighbor[0])>1):
                distance = map[car_position][neighbor[0]]['weight']
                speed_limit = map[car_position][neighbor[0]]['speed_limit']
                time = distance/min(speed_limit,speed)
                car_position = neighbor[0]
                check = True
            else:
                check = False
        if action == 1:
            #down
            if ((car_position-neighbor[-1])<-1) :
                distance = map[car_position][neighbor[-1]]['weight']
                speed_limit = map[car_position][neighbor[-1]]['speed_limit']
                time = distance/min(speed_limit,speed)
                car_position = neighbor[-1]
                check =True
            else:
                check = False
        if action == 2:
            #left
            if ((car_position-1) in neighbor) :
                distance = map[car_position][car_position-1]['weight']
                speed_limit = map[car_position][neighbor-1]['speed_limit']
                time = distance/min(speed_limit,speed)
                car_position = car_position -1
                check =True
            else:
                check = False
        if action == 3:
            #right
            if ((car_position+1) in neighbor):
                distance = map[car_position][car_position+1]['weight']
                speed_limit = map[car_position][neighbor+1]['speed_limit']
                time = distance/min(speed_limit,speed)
                car_position = car_position+1
                check = True
            else:
                check = False

        car[2] = car_position
        return check,car,current_position,time
    def reset(self):
        pass
        #reset car


# usage :
#car_run = road().travel(action='right',car=[1,2,1],g=graph_set().draw())
#
#print (car_run)

#print (g.number_of_edges())
# for i in nx.all_neighbors(g,1):
#     neighbor.append(i)
# print (list(set(neighbor)))

'''
car_run = road().travel(action='down',car=[1,16,1],g=graph_set().draw())
print (car_run)
car_run = road().travel(action='right',car=car_run,g=graph_set().draw())
print(car_run)
car_run = road().travel(action='right',car=car_run,g=graph_set().draw())
car_run = road().travel(action='right',car=car_run,g=graph_set().draw())
car_run = road().travel(action='down',car=car_run,g=graph_set().draw())
car_run = road().travel(action='down',car=car_run,g=graph_set().draw())
'''
