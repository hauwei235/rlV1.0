import pandas as pd
import numpy as np

class QlearningTable:
    def __init__(self,action=[0,1,2,3],learning_rate = 0.01,reward_decay = 0.9, e_greddy = 0.9):
        self.action = action
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greddy
        self.q_table = pd.DataFrame(columns=self.action,dtype = np.float64)

    def choose_action(self,position):
        self.check_state_exist(position)
        if np.random.uniform()< self.epsilon:
            state_action = self.q_table.loc[position,:]
            #print(self.action)
            #print('good')
            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.idxmax()
            #print(state_action)
            #action =np.random.choice(state_action[state_action == np.max(state_action).index])
            #这一行看不懂 np.random.choice
        else:
            #print (self.action)
            action = np.random.choice(self.action)
            #print ('this')
            #print(action)
        return action

    def learn(self,position,action,reward,next_position,final_positon):

        self.check_state_exist(next_position)
        # print(self.q_table)
        #print(type(position))
       #print(type(action))
        q_predict = self.q_table.loc[position,action]
        if next_position != final_positon:
            q_target = reward + self.gamma* self.q_table.loc[next_position,:].max()
        else :
            q_target = reward
        self.q_table.loc[position,action]+=self.lr*(q_target-q_predict)

    def check_state_exist(self,position):
        # 将新位置添加到q_table 之中，全0
        if position not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0]*len(self.action),
                    index=self.q_table.columns,
                    name=position
                )
            )


