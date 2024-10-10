import airsim
import time

# connect to the AirSim simulator
client = airsim.MultirotorClient()

client.enableApiControl(True)  # get control
client.armDisarm(True)  # unlock
client.takeoffAsync().join()  # takeoff

# square flight(position control)
# 飞行路径：（0,0）->（5,0）->（5,5）->（0,5）->（0,0）

# moveToZAysnc(z, speed)以speed(m/s)的速度到z高度
client.moveToZAsync(-3, 1).join()  # 上升到3m高度
# moveToPositionAsync(x, y, z, speed)以speed(m/s)的速度到（x,y,z）点坐标
'''
def moveToPositionAsync(
        self,
        x,          # 位置坐标（北东地坐标系）
        y,
        z,
        velocity,   # 速度
        timeout_sec=3e38,   # 超时时间
        drivetrain=DrivetrainType.MaxDegreeOfFreedom,
        drivingstyle参数可以设置为两个量:
            airsim.DrivetrainType.ForwardOnly:始终朝向速度方向
            airsim.DrivetrainType.MaxDegreeOfFreedom:手动设置yaw角度
        yaw_mode=YawMode(),   # 设置飞行朝向模式和yaw角控制模式
        yaw_mode必须设置为YawMode()，YawMode()有以下参数：
            YawMode().is_rate:True-设置角速度，False-设置角度
            YawMode().yaw_or_rate:设置角速度或角度的值
        lookahead=-1,
        adaptive_lookahead=1,   # 设置路径飞行的时候的yaw角控制模式
        vehicle_name="",    # 飞机名称
     )
'''
client.moveToPositionAsync(5, 0, -3, 1).join()  # 飞到（5,0）点坐标
client.moveToPositionAsync(5, 5, -3, 1).join()  # 飞到（5,5）点坐标
client.moveToPositionAsync(0, 5, -3, 1).join()  # 飞到（0,5）点坐标
client.moveToPositionAsync(0, 0, -3, 1).join()  # 回到（0,0）点坐标

client.landAsync().join()  # land
client.armDisarm(False)  # lock
client.enableApiControl(False)  # release control