#observation 位置信息

#import road_env_append
import road_env_good
import self_qlearning
import graph_append
import time
import cars
#car[0] start_point ;car[1] end_point ;car[2] current_position
def update(init_one_car,g):
    #g = graph_append.graph_set().draw()
    #cars_set = cars.car_set()
    #init_car = cars_set.init_car()
    #init_one_car = init_car[car_number-1]
    # 大概要训练1600 episde
    reset_car = str(init_one_car)
    car=init_one_car
    #print(init_one_car)
    self_q_table = self_qlearning.QlearningTable()
    road_this = road_env_good.road()
    #print("this")
    min_action = 100
    for episode in range (300):
        step = 0
        total_action = []
        total_road = []
        while True:
            # car[2] current position

            action = self_q_table.choose_action(int(car[2]))
            #total_action.append(action)
            # 这一步是对的
            #next_positon , reward ,done,current_position = road_this.travel(action,g=g,car=car)
            car_state , reward ,done,current_position,road_id = road_this.travel(action,g=g,car=car)
            total_road.append(road_id)
            next_positon = car_state[2]
            #print(action,next_positon)
            self_q_table.learn(next_position=next_positon,action=action,reward=reward,position=current_position,final_positon=car[1])
            #print(position)
            #print(next_positon)
            #car[2] = int(next_positon)
            step+=1
            #print(reset_car)
            # print(time)
            if done:
                a = step
                if (a<min_action):
                    #print('close enough')
                    #print(episode,step,total_action)
                    min_action = a
                    min_road = total_road
                    print(min_action)
                break
                #print('this is not right',step)
        #print(reset_car)
        # car[0] = int(reset_car.split(',')[0].strip('['))
        # car[1] = int(reset_car.split(',')[1])
        car[2] = int(reset_car.split(',')[2])
        # car[3] = int(reset_car.split(',')[3])
        car[4] = int(reset_car.split(',')[4])
        car[5] = int(reset_car.split(',')[5])
        # car[6] = int(reset_car.split(',')[6])
        # car[7] = int(reset_car.split(',')[7].strip(']'))
        # car_info = [start_node,end_node,current position ,speed_limit,last position ,left distance,plan_time,car_id]
    print('game over')
    print(min_action,min_road)
    with open("C:/Users/txt/Desktop/match/huawei/result.txt",'a') as result:
        result.write(str(car[7]),str(car[6]),str(min_road))

if __name__ == '__main__':
    time1 = time.time()
    g = graph_append.graph_set().draw()
    cars_set = cars.car_set()
    init_car ,car_number= cars_set.init_car()
    # car_number 是从1开始的
    # update(init_one_car=[1, 16, 1, 5, 1, 0, 3, 10000],g=g)
    for i in range(car_number):
        print(i)
        init_one_car = init_car[i]
        print(init_one_car)
        update(init_one_car,g)
    # time2 = time.time()
    #print(time2 - time1)
