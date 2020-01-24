# System imports
# None

# Local imporst
# None

class RCBit():

    def __init__(self, bit, register_size=16):
        # Store the bit location and the bit mask
        self.bit = bit
        self.bit_mask = (1 << bit)
        # Store the register_size
        self.register_size = register_size
        # Store the value - defaults to 0
        self._value = 0

    def getValue(self):
        tmp_value = self._value
        self._value = 0
        return tmp_value

    def setValue(self, value):
        self._value = value

    def delValue(self):
        del self._value

    value = property(getValue, setValue, delValue, )
# End RCBit

if __name__ == '__main__':
    rcb = RCBit(0)
    assert rcb.value == 0, 'ERROR: Initial RWBit value is not 0!'

    rcb.value = 1
    val = rcb.value
    assert val == 1, 'ERROR: Value was not stored correctly'

    val = rcb.value
    assert val == 0, 'ERROR: Value was not cleared after read'
