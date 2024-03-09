#Python Read
import multiprocessing.shared_memory
from ctypes import *
class Req(Structure):
    _pack_=1
    _fields_= \
        [('uRouter',c_ubyte,1),
        ('uSubNode',c_ubyte,1),
        ('uCM',c_ubyte,1),
        ('uCD',c_ubyte,1),
        ('uLevel',c_ubyte,4),
        ('uChannel',c_ubyte,4),
        ('uErrBate',c_ubyte,4),
        ('uResBytes',c_ubyte),
        ('uSpeed',c_ushort,15),
        ('uUnit',c_ushort,1),
        ('uReserve',c_ubyte)]
# 打开共享内存，使用shm_open函数打开共享内存并获取共享内存的名称
shm = multiprocessing.shared_memory.SharedMemory(name='my_share_mem')
 
# 创建一个字节序列，长度为MyStruct的大小
ba = bytearray(sizeof(Req))

# 从共享内存中读取数据到字节序列
ba[:] = shm.buf[:len(ba)]

# 将字节序列转换为结构体
my_struct = Req.from_buffer(ba)

print(my_struct.uReserve)  # 输出：123
print(my_struct.uResBytes)  # 输出：b'Hello'
# 关闭共享内存
shm.close()
 
# 删除共享内存
shm.unlink()
