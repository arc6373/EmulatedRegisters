# System imports
# None

# Local imports
# None

class RWBit:

    def __init__(self, bit, register_size=16):
        # Store the bit location and the bit mask
        self.bit = bit
        self.bit_mask = (1 << bit)
        # Store the register_size
        self.register_size = register_size
        # Store the value - defaults to 0
        self._value = 0

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def delValue(self):
        del self._value

    value = property(getValue, setValue, delValue, )

# End RWBit

if __name__ == '__main__':
    rwb = RWBit(0)
    assert rwb.value == 0, 'ERROR: Initial RWBit value is not 0!'

    rwb.value = 1
    assert rwb.value == 1, 'ERROR: Initial RWBit value is not 1!'

    val = rwb.value
    assert val == 1, 'ERROR: Value was not stored correctly'

    val = rwb.value
    assert val == 1, 'ERROR: Value was cleared after read'
