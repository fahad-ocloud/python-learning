import struct
class Transaction:
    def __init__(self,bid,bname,pid,pname,transaction_type):
        self.bid = bid
        self.bname = bname
        self.pname = pname
        self.pid = pid
        self.transaction_type = transaction_type
        self.__transaction_path =  "../library_management_system/assets/transactions/transaction.bin"
    @staticmethod
    def serialize(transaction):
        bname_bytes = transaction.bname.encode('utf-8')
        pname_bytes = transaction.pname.encode('utf-8')
        pid_bytes = transaction.pid.encode('utf-8')
        bname_bytes = bname_bytes[:50].ljust(50, b'\0') 
        pname_bytes = pname_bytes[:50].ljust(50, b'\0')
        pid_bytes = pid_bytes[:50].ljust(50, b'\0')
        return struct.pack('i50s50s50si',transaction.bid, bname_bytes, pid_bytes,pname_bytes, transaction.transaction_type)

    @staticmethod
    def deserialize(data):
        bid,bname_bytes, pid,pname_bytes, transaction_type = struct.unpack('i50s50s50si', data)
        bname = bname_bytes.decode('utf-8').rstrip('\0')
        pname = pname_bytes.decode('utf-8').rstrip('\0')
        pid = pid.decode('utf-8').rstrip('\0')
        return Transaction(bid,bname, pid,pname, transaction_type)
    @staticmethod
    def cal_size():
        return struct.calcsize('i50s50s50si')