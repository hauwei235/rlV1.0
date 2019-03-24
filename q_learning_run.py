#observation 位置信息

import road_env_append
import self_qlearning
import graph_append
import time
#car[0] start_point ;car[1] end_point ;car[2] current_position
def update():
    g = graph_append.graph_set().draw()
    init_car =[1,16,1,5]
    # 大概要训练1600 episde
    car=init_car
    self_q_table = self_qlearning.QlearningTable()
    road_this = road_env_append.road()
    for episode in range (3000):
        step = 0
        while True:
            # car[2] current position
            action = self_q_table.choose_action(int(car[2]))

            # print('hi',action)
            # 这一步是对的
            next_positon , reward ,done,current_position = road_this.travel(action,g=g,car=car)
            self_q_table.learn(next_position=next_positon,action=action,reward=reward,position=current_position,final_positon=car[1])
            #print(position)
            #print(next_positon)
            #car[2] = int(next_positon)
            step+=1
            # print(time)
            if done:
                if (step< 10):
                    print('close enough')
                car = init_car
                break
    print('game over')

if __name__ == '__main__':
    time1 = time.time()
    update()
    time2 = time.time()
    print(time2 - time1)
