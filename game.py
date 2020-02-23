import time
import numpy as np

## 对时间的格式做出规定，示例：'2020/2/23-21:37:02'
def gettime():
    t = time.localtime(time.time())
    strtime = '{}/{}/{}-{}:{}:{}'.format(t[0],t[1],t[2],t[3],t[4],t[5])
    return strtime

def readtime(strtime):#将文本时间读取为计算机时间
    rtime = time.mktime(time.strptime('{}'.format(strtime), "%Y/%m/%d-%H:%M:%S"))
    return rtime

## 设置奖励函数
def reward(chooses, price = 100):
    u = np.mean(chooses)
    std = np.std(array,ddof=1)
    scores = []
    rewards = []
    for choose in chooses:
        score = np.exp(-(x - u) ** 2 / (2 * std ** 2)) / (math.sqrt(2 * math.pi) * std)
        scores.append(score)
    scoresum = sum(scores)
    for score in scores:
        rewards.append(score/scoresum*price)
    return rewards


##对象
class Player():
    #玩家对象

    def __init__(self):
        self.name = ''
        self.password = ''
        self.createtime = ''
        self.id = ''
        #本金
        self.money = 400
        self.history#历史操作，暂不开发

    def creatPlayer(self):
        pass
    
    def resetPassword(self, newpassword):
        self.password = newpassword
        pass

class Game():
    #每轮游戏对象
    
    def __init__(self):
        #游戏轮次
        self.id = ''
        #时间
        self.starttime = ''
        self.endtime = ''
        #参与人数
        self.scale = ''
        #玩家们提交的结果
        self.chooseinfos = [{'playerid':'000001',
                             'choose':12,
                             'time':'2020/2/23-21:37:02',},
                            
                            ]
        #本轮游戏的1/2均值
        self.halfmean = ''

class Question():
    #题目对象
    
    def __init__(self):
        self.id = ''
        self.stem = ''
        self.answers = ['',
                        '',
                        '',
                        '',
                        ]
        self.correct = 0 #每一道都是第一个正确，但是显示的时候是打乱顺序的
    
    def makeQue(self):
        pass
