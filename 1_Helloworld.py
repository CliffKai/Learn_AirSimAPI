import airsim
# connect to the AirSim simulator
# 与 AirSim 建立连接，并且返回句柄（client），后面的每次操作需要使用这个句柄
#如果是汽车仿真，代码是：client = airsim.CarClient()
client = airsim.MultirotorClient()
# 检查通信是否建立成功，并且会在命令行中打印连接情况
# 如果连接正常会在命令行中打印如下：
# Connected!
# Client Ver:1 (Min Req: 1), Server Ver:1 (Min Req: 1)
client.confirmConnection()

# get control
# 因为安全问题， API 控制默认是不开启的，遥控器有全部的控制权限
# 需要调用 enableApiControl(True) 来开启 API 控制
client.enableApiControl(True)

# unlock
# 解锁飞机，这个函数会解锁飞机的电机，使得飞机可以起飞
client.armDisarm(True)


# Async methods returns Future. Call join() to wait for task to complete.
# 带有Async后缀的函数是异步函数
# 想要实现同步的效果，需要调用join()函数
client.takeoffAsync().join()
client.landAsync().join()

# lock
client.armDisarm(False)
# release control
client.enableApiControl(False)

'''
AirSim API 使用的是 TCP/IP 中的 msgpack-rpc 协议
当 AirSim 开始仿真的时候，会打开 41451 并监听这个端口的需求
python 程序使用 msgpack serialization 格式向这个端口发送 RPC 包，就可以与AirSim进行通信了
'''