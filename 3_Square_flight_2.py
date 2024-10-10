import airsim
import time

client = airsim.MultirotorClient()  # connect to the AirSim simulator
client.enableApiControl(True)  # 获取控制权
client.armDisarm(True)  # 解锁
client.takeoffAsync().join()  # 第一阶段：起飞

'''
飞行视角：
    FlyWithMe()：以6自由度跟随四旋翼
    FPV(F)：机载摄像头视角（第一人称视角）
    GroundObserver(\)：在地面上以XY平面自由度跟随四旋翼（地面观察者）
    Manual(M)：手动设置摄像机的位置
    SpringArmChase(/)：摄像机固定在一个隐形的与汽车连在一起的弹性机臂上，跟随汽车，所以会有一些时延
    NoDisplay：不显示画面，这可以提高渲染性能，而且不影响 APIs
'''

# square flight(speed control)

client.moveToZAsync(-2, 1).join()  # 第二阶段：上升到2米高度

# 飞正方形
# moveByVelocityZAsync(vx, vy, z, duration)：无人机在z的高度以vx,vy的速度飞行duration秒
'''
def moveByVelocityZAsync(
        self,
        vx,
        vy,
        z,
        duration,
        drivetrain=DrivetrainType.MaxDegreeOfFreedom,
        yaw_mode=YawMode(),
        vehicle_name="",
    )
'''
client.moveByVelocityZAsync(1, 0, -2, 8).join()  # 第三阶段：以1m/s速度向前飞8秒钟
client.moveByVelocityZAsync(0, 1, -2, 8).join()  # 第三阶段：以1m/s速度向右飞8秒钟
client.moveByVelocityZAsync(-1, 0, -2, 8).join()  # 第三阶段：以1m/s速度向后飞8秒钟
client.moveByVelocityZAsync(0, -1, -2, 8).join()  # 第三阶段：以1m/s速度向左飞8秒钟

# 悬停 2 秒钟
# hoverAsync()：无人机悬停在当前位置
client.hoverAsync().join()  # 第四阶段：悬停6秒钟
time.sleep(6)

client.landAsync().join()  # 第五阶段：降落
client.armDisarm(False)  # 上锁
client.enableApiControl(False)  # 释放控制权


