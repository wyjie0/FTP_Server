import os
import pickle
from core.user import User
from conf import settings

def login(msg):
    print(msg)

def register(msg):
    # 拿到username与password
    # 创建一个属于这个用户的家目录并记录
    # 把用户名和密码写入userinfo文件，记录用户名
    # 记录用户的初始磁盘配额
    # 记录文件大小
    # 记录用户当前所在的目录
    user_obj = User(msg['username'])#记录用户的信息在内存里
    pickle_path = os.path.join(settings.pickle_path,msg['username'])
    with open(pickle_path,'wb') as f:
        pickle.dump(user_obj,f)
    os.mkdir(user_obj.home)#创建属于用户的文件夹
    with open(settings.user_info,'a') as f:
        f.write('%s|%s|%s'%(msg['username'],msg['password'],pickle_path ))
    return True

def upload(msg):
    print(msg)

def download(msg):
    print(msg)