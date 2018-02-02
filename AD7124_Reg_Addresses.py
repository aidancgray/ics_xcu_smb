"""
Dictionary of AD7124 Register addresses
"""

RegAddrs = [
    {'name': "Comm", 'addr': 0x00, 'value':  0x00, 'size': 1, 'rw': 2},
    {'name': "Status", 'addr': 0x00, 'value':  0x00, 'size': 1, 'rw': 2},
    {'name': "ADC_Control", 'addr': 0x01, 'value': 0x0000, 'size': 2, 'rw': 1},
    {'name': "Data", 'addr': 0x02, 'value':  0x0000, 'size': 3, 'rw': 2},
    {'name': "IOCon1", 'addr' : 0x03, 'value':  0x0000, 'size': 3, 'rw': 1},
    {'name': "IOCon2", 'addr' : 0x04, 'value':  0x0000, 'size': 2, 'rw': 1},
    {'name': "ID", 'addr' : 0x05, 'value':  0x12, 'size': 1, 'rw': 2},
    {'name': "Error", 'addr' : 0x06, 'value':  0x0000, 'size': 3, 'rw': 2},
    {'name': "Error_En", 'addr' : 0x07, 'value':  0x0400, 'size': 3, 'rw': 1},
    {'name': "Mclk_Count", 'addr' : 0x08, 'value':  0x00, 'size': 1, 'rw': 2},
    {'name': "Channel_0", 'addr': 0x09, 'value':  0x8001, 'size': 2, 'rw': 1},
    {'name': "Channel_1", 'addr': 0x0A, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_2", 'addr': 0x0B, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_3", 'addr': 0x0C, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_4", 'addr': 0x0D, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_5", 'addr': 0x0E, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_6", 'addr': 0x0F, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_7", 'addr': 0x10, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_8", 'addr': 0x11, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_9", 'addr': 0x12, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_10", 'addr': 0x13, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_11", 'addr': 0x14, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_12", 'addr': 0x15, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_13", 'addr': 0x16, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_14", 'addr': 0x17, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Channel_15", 'addr': 0x18, 'value':  0x0001, 'size': 2, 'rw': 1},
    {'name': "Config_0", 'addr': 0x19, 'value':  0x0860, 'size': 2, 'rw': 1},
    {'name': "Config_1", 'addr': 0x1A, 'value':  0x0860, 'size': 2, 'rw': 1},
    {'name': "Config_2", 'addr': 0x1B, 'value':  0x0860, 'size': 2, 'rw': 1},
    {'name': "Config_3", 'addr': 0x1C, 'value':  0x0860, 'size': 2, 'rw': 1},
    {'name': "Config_4", 'addr': 0x1D, 'value':  0x0860, 'size': 2, 'rw': 1},
    {'name': "Config_5", 'addr': 0x1E, 'value':  0x0860, 'size': 2, 'rw': 1},
    {'name': "Config_6", 'addr': 0x1F, 'value':  0x0860, 'size': 2, 'rw': 1},
    {'name': "Config_7", 'addr': 0x20, 'value':  0x0860, 'size': 2, 'rw': 1},
    {'name': "Filter_0", 'addr': 0x21, 'value':  0x060180, 'size': 3, 'rw': 1},
    {'name': "Filter_1", 'addr': 0x22, 'value':  0x060180, 'size': 3, 'rw': 1},
    {'name': "Filter_2", 'addr': 0x23, 'value':  0x060180, 'size': 3, 'rw': 1},
    {'name': "Filter_3", 'addr': 0x24, 'value':  0x060180, 'size': 3, 'rw': 1},
    {'name': "Filter_4", 'addr': 0x25, 'value':  0x060180, 'size': 3, 'rw': 1},
    {'name': "Filter_5", 'addr': 0x26, 'value':  0x060180, 'size': 3, 'rw': 1},
    {'name': "Filter_6", 'addr': 0x27, 'value':  0x060180, 'size': 3, 'rw': 1},
    {'name': "Filter_7", 'addr': 0x28, 'value':  0x060180, 'size': 3, 'rw': 1},
    {'name': "Offset_0", 'addr': 0x29, 'value':  0x800000, 'size': 3, 'rw': 1},
    {'name': "Offset_1", 'addr': 0x2A, 'value':  0x800000, 'size': 3, 'rw': 1},
    {'name': "Offset_2", 'addr': 0x2B, 'value':  0x800000, 'size': 3, 'rw': 1},
    {'name': "Offset_3", 'addr': 0x2C, 'value':  0x800000, 'size': 3, 'rw': 1},
    {'name': "Offset_4", 'addr': 0x2D, 'value':  0x800000, 'size': 3, 'rw': 1},
    {'name': "Offset_5", 'addr': 0x2E, 'value':  0x800000, 'size': 3, 'rw': 1},
    {'name': "Offset_6", 'addr': 0x2F, 'value':  0x800000, 'size': 3, 'rw': 1},
    {'name': "Offset_7", 'addr': 0x30, 'value':  0x800000, 'size': 3, 'rw': 1},
    {'name': "Gain_0", 'addr': 0x31, 'value':  0x500000, 'size': 3, 'rw': 1},
    {'name': "Gain_1", 'addr': 0x32, 'value':  0x500000, 'size': 3, 'rw': 1},
    {'name': "Gain_2", 'addr': 0x33, 'value':  0x500000, 'size': 3, 'rw': 1},
    {'name': "Gain_3", 'addr': 0x34, 'value':  0x500000, 'size': 3, 'rw': 1},
    {'name': "Gain_4", 'addr': 0x35, 'value':  0x500000, 'size': 3, 'rw': 1},
    {'name': "Gain_5", 'addr': 0x36, 'value':  0x500000, 'size': 3, 'rw': 1},
    {'name': "Gain_6", 'addr': 0x37, 'value':  0x500000, 'size': 3, 'rw': 1},
    {'name': "Gain_7", 'addr': 0x38, 'value':  0x500000, 'size': 3, 'rw': 1}]

