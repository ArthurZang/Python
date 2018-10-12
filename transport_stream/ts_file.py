import struct
import os
from pts import PTS

PTS_SYNC = 0x47
PTS_SIZE = 188

class TSFile:
    def __init__(self,file_name):
        self.file_size = os.path.getsize(file_name)
        self.file_handle = open(file_name, 'rb')
        self.file_pos = 0
        self.PTS_counter = 0
        self.PAT_list = list()
        self.PTS_list = list()


    def read_file(self, file_position, width):
        self.file_handle.seek(file_position, 0)
        if width == 4:
            string = self.file_handle.read(4)
            if string == '':
                raise IOError
            return struct.unpack('>L', string[:4])[0]
        elif width == 2:
            string = self.file_handle.read(2)
            if string == '':
                raise IOError
            return struct.unpack('>H', string[:2])[0]
        elif width == 1:
            string = self.file_handle.read(1)
            if string == '':
                raise IOError
            return struct.unpack('>B', string[:1])[0]

    def PTS_parse(self):
        for current_pos in range(0,self.file_size,PTS_SIZE):
            header_pos = self.find_pts_header_pos(current_pos)

            print("header %d" %header_pos)
            data = list()
            for i in range(PTS_SIZE):
                data.append(self.read_file(i+header_pos, 1))

            packet_ts = PTS(data)
            self.PTS_list.append(packet_ts)
            packet_ts.debug_info()

            if self.PTS_list.__len__() >= 2:
                break




        print("the number of PTS is %d" % self.PTS_counter)

    def find_pts_header_pos(self, pos):
        for i in range(pos,self.file_size,1):
            data = self.read_file(i, 1)
            if(data == PTS_SYNC):
                return pos


    def close(self):
        self.file_handle.close()

if __name__ == "__main__":
    ts_file = TSFile("mepg2.ts")
    ts_file.PTS_parse()