class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu1=CPU()
cpu2=cpu1
print(cpu1,cpu2) #内存地址相同
print(id(cpu1),'---',id(cpu2))
print('----------------')
#浅拷贝
disk=Disk()
computer=Computer(cpu1, disk)

import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
#深拷贝 递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
computer3=copy.deepcopy(computer)
print(computer3,computer3.cpu,computer3.disk)
