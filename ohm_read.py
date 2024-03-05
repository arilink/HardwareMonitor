import os
import sys
import clr
import ctypes
import time
import datetime
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin():
    # 如果不是管理员，使用管理员权限重新运行该脚本
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

# 以下是需要以管理员权限运行的代码
# ...
print("Administ running")
clr.AddReference('E:/OpenHard/OpenHardwareMonitor/OpenHardwareMonitorLib')

import OpenHardwareMonitor as ohm
from OpenHardwareMonitor.Hardware import Computer, HardwareType, SensorType
computer = Computer()
computer.CPUEnabled = True
computer.GPUEnabled = True
computer.HDDEnabled = True
computer.RAMEnabled = True
computer.MainboardEnabled = True
computer.FanControllerEnabled = True
hardwareType = ohm.Hardware.HardwareType
sensorType = ohm.Hardware.SensorType

computer.Open()
while True:
    print('{:=^50}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    for hardware in computer.Hardware:
        hardware.Update()
        if hardware.HardwareType == hardwareType.CPU:
            print("This is CPU")
            print(hardware.Name)
            for sensor in hardware.Sensors:
                if sensor.SensorType == sensorType.Load:
                    si_ls = str(sensor.Identifier).split('/')
                    ssname = f'{si_ls[1]}#{si_ls[-1]}'
                    print(ssname, sensor.Value)
        if hardware.HardwareType == hardwareType.Mainboard:
            print("This is Mainboard")
            print(hardware.Name)
        if hardware.HardwareType == hardwareType.RAM:
            print("This is RAM")
            print(hardware.Name)
            for sensor in hardware.Sensors:
                print(sensor.SensorType)
                if sensor.SensorType == sensorType.Load:
                    si_ls = str(sensor.Identifier).split('/')
                    ssname = f'{si_ls[1]}#{si_ls[-1]}'
                    print(ssname, sensor.Value)      
                if sensor.SensorType == sensorType.Data:
                    print("RAM MAX",sensor.Max)  #最大占用
                    si_ls = str(sensor.Identifier).split('/')
                    ssname = f'{si_ls[1]}#{si_ls[-1]}'
                    print(ssname, sensor.Value)
        if hardware.HardwareType == hardwareType.HDD:
            print("This is HDD")
            print(hardware.Name)
            for sensor in hardware.Sensors:
                print(sensor.Value)   #硬件已用空间
        # for sensor in hardware.Sensors:
        #     if sensor.SensorType == sensorType.Load:
        #         si_ls = str(sensor.Identifier).split('/')
        #         ssname = f'{si_ls[1]}#{si_ls[-1]}'
        #         print(ssname, sensor.Value)
            
        time.sleep(1)