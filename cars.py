
f = open('C:/Users/txt/Desktop/match/huawei/easy_car.txt')
#(道路id，道路长度，最高限速，车道数目，起始点id，终点id，是否双向)

#(id,from,to,speed,planTime)
class car_set():
    def __init__(self):
        pass
    def init_car(self):
        car_list = []
        while True:
            line = f.readline()
            if line:
                car_id =int(line.split(',')[0].strip('('))
                start_node = int(line.split(',')[1])
                end_node = int(line.split(',')[2])
                speed_limit  = int(line.split(',')[3])
                plan_time = int(line.split(',')[4].strip().strip(')'))
                car_info = [start_node,end_node,start_node,speed_limit,start_node,0,plan_time,car_id]
                car_list.append(car_info)
                #car_number = len(car_list)
                #print(car_id,start_node,plan_time)
            else:
                break
        # print(car_list)
        return car_list,len(car_list)
    def choose_car(self,car_number,car_list):
        # 这里拿出一辆车出来，只是在q_kearning 之中起作用
        a_car = car_list[car_number-1]
#car_list = car_set().init_car()
