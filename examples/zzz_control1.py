# 示例（概念性，基于 RTDE_Python_Client_Library / 常见接口）
from rtde_receive import RTDEReceiveInterface
from rtde_control import RTDEControlInterface
import time

ROBOT_IP = "192.168.1.2"   # 改为你的UR5e IP

# 1) 建立接收与控制接口
rtde_r = RTDEReceiveInterface(ROBOT_IP)    # 用来读状态
rtde_c = RTDEControlInterface(ROBOT_IP)    # 用来发送运动命令

# 2) 读取当前关节角（示例）
joint_q = rtde_r.getActualQ()   # 返回 6 元组（rad）
print("当前关节角:", joint_q)

# 3) 简单的 moveJ（点到点）——速度、加速度按需要设置
target = [0.0, -1.57, 0.0, -1.57, 0.0, 0.0]  # 目标关节（rad）
rtde_c.moveJ(target, speed=0.5, acceleration=0.5)

# 4) 也可以用 servoJ / servoL 实现更高频率的实时控制（见示例）
time.sleep(1.0)
