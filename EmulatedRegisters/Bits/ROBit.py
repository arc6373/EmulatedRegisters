# System imports
# None

# Local imporst
# None

class ROBit():

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
        # Do nothing as it is read only
        pass

    def delValue(self):
        del self._value

    value = property(getValue, setValue, delValue, )
# End ROBit

if __name__ == '__main__':
    rob = ROBit(0)
    assert rob.value == 0, 'ERROR: Initial RWBit value is not 0!'

    rob.value = 1
    assert rob.value == 0, 'ERROR: ROBit was allowed to change!'
