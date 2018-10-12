PAT_PID = 0x0000
CAT_PID = 0x0001
DES_PID = 0x0002

class PTS:
    sync_byte = 0x47
    pay_load = list()
    def __init__(self, data):
        self.fill_header(data[0:4])

    def fill_header(self,data):
        self.transport_error_indicator = (data[1]>>7) & 0x01
        self.payload_unit_start_indicator = (data[1]>>6) & 0x01
        self.trasnport_priority = (data[1]>>5) & 0x01
        self.PID = data[2] + ((data[1]&0x1F)<<8)
        self.transport_scrambling_control = (data[3]>>6)&0x03
        self.adaptatio_field_control = (data[3] >> 4) & 0x03
        self.continuity_counter = data[3] & 0x0F

    def debug_info(self):
        if self.transport_error_indicator == 1:
            print("transport error")
            return
        if self.payload_unit_start_indicator == 1:
            print("start packet")
        else:
            print("middle packet")
        if self.PID == PAT_PID:
            print("PAT")
        if self.transport_scrambling_control == 0:
            print("No scrambling")
        else:
            print("Scrambling")
        if self.adaptatio_field_control == 1:
            print("Only payload")
        elif self.adaptatio_field_control == 2:
            print("Only adaption")
        elif self.adaptatio_field_control == 3:
            print("adaption and payload")
        else:
            print("Unknow")

        print("packet number %d" %(self.continuity_counter))