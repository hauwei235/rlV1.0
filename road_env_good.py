import networkx as nx
from graph_append import graph_set
import math
class road():
    def __init__(self,reward = 0):
        self.reward = reward
    def travel(self,action,g,car=[]):
        #car[0] start_point ;car[1] end_point ;car[2] current_position ; car[3] speed ; car[4] past_position ; car[5] letf distance
        map = g
        check,car,current_position,time= road().run(car=car,action=action,g=map)
        self.reward = self.reward - time
        flag_done = False
        if car[2] ==car[1]:
            self.reward = self.reward +100
            flag_done = True
        return car,self.reward,flag_done,current_position
    def run(self,action ,g , car =[]):
        map = g
        #speed = car[3]
        time = 0
        neighbor = []
        left_distance = car[5]
        check = False
        car_position = car[2]
        action = int(action)
        for i in nx.all_neighbors(map,car_position):
            neighbor.append(i)
        neighbor = list(sorted(set(neighbor)))
        current_position = car_position
        if action == 0:
            #up
            if ((car_position-neighbor[0])>1):
                check = True
                next_position = neighbor[0]
                time,left_distance = road().time(car,next_position,g)
                car_position = next_position
            else:
                check = False
        if action == 1:
            #down
            if ((car_position-neighbor[-1])<-1) :
                next_position = neighbor[-1]
                time,left_distance = road().time(car,next_position,g)
                car_position = next_position
                check =True
            else:
                check = False
        if action == 2:
            #left
            if ((car_position-1) in neighbor) :
                next_position = car_position -1
                time,left_distance = road().time(car,next_position,g)
                car_position = next_position
                check =True
            else:
                check = False
        if action == 3:
            #right
            if ((car_position+1) in neighbor):
                next_position = car_position+1
                time,left_distance = road().time(car,next_position,g)
                car_position = next_position
                check = True
            else:
                check = False

        car[2] = car_position
        car[5] = left_distance
        return check,car,current_position,time
    def time(self,car,next_position,g):
        #car[0] start_point ;car[1] end_point ;car[2] current_position ; car[3] speed ; car[4] past_position ; car[5] letf distance
        #return time,left_distance
        map = g
        if car[0]==car[2]:
            left_distance = 0
            car_position = car[2]
            distance = map[car_position][next_position]['weight']
            speed_limit = map[car_position][next_position]['speed_limit']
            speed = min(speed_limit,car[3])
            time = math.floor(distance/speed)
            left_distance = distance - time*speed
        else:
            #past_position = car[4]
            left_distance = car[5]
            car_position = car[2]
            #left_speed = min(map[past_position][car_position]['speed_limit'],car[3])
            distance = map[car_position][next_position]['weight']
            speed = min(map[car_position][next_position]['speed_limit'],car[3])
            if left_distance ==0:
                time = math.floor(distance/speed)
                left_distance = distance - time*speed
            elif speed<left_distance:
                time = math.floor(distance/speed) +1
                left_distance = distance - time*speed
            else:
                time = math.floor((distance - (speed - left_distance))/speed)+1
                left_distance = distance - (time - 1) *speed - (speed - left_distance)
        #print(time,left_distance,speed)
        return time,left_distance
# g = graph_set().draw()
# # return car,self.reward,flag_done,current_position
# car_run,reward,done,current_position = road().travel(action=1,car=[1,16,1,4,1,0],g=g)
# print(car_run,reward,done,current_position)
# car_run,reward,done,current_position = road().travel(action=1,car = car_run,g=g)
# print(car_run,reward,done,current_position)
