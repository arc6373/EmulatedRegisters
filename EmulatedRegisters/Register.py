# System imports
# None

# Local imports
from Bits.RWBit import RWBit
from Bits.RCBit import RCBit
from Bits.ROBit import ROBit

class Register:

    SUPPORTED_BITS = {
        'RC': RCBit,
        'RW': RWBit,
        'RO': ROBit,
    }

    def __init__(self, register_address, bit_definitions, register_size=16):
        self.bits = [None] * register_size
        self.address = register_address
        self.size = register_size
        self._value = 0

        for bit in bit_definitions:
            # Expects a list of tuples [(bit, type)]
            bit_type = bit[1]
            bit_loc = bit[0]

            if (bit_type in Register.SUPPORTED_BITS):
                self.bits[bit_loc] = Register.SUPPORTED_BITS[bit_type](bit_loc)
            else:
                # Use a default type of RW
                self.bits[bit_loc] = RWBit()
        # End bit creation
    # End __init__

    def __getitem__(self, index):
        if isinstance(index, slice):
            ret_val = 0

            for idx, key in enumerate(range(*index.indices(len(self.bits)))):
                ret_val |= (self.bits[key].value << idx)

            return ret_val

        elif isinstance(index, int):
            if (index < self.size):
                return self.bits[index].value
            else:
                # Requested bit is out of range
                return None

        else:
            return None
    # End __getitem__

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            for idx, key in enumerate(range(*index.indices(len(self.bits)))):
                tmp_mask = (1 << idx)
                self.bits[key].value = (value & tmp_mask) >> idx
                # Value = 2 = 0b10
                # Splice over bits 1 and 0
                # tmp_mask = (1 << 0)
                # self.bits[0].value = (0b10 & 0b01) >> 0 = 0
                # tmp_mask = (1 << 1)
                # self.bits[1].value = (0b10 & 0b10) >> 1 = 1

        elif isinstance(index, int):
            if (index < self.size):
                # Make sure the value is a 1 or a 0 as it is a single bit being set
                self.bits[index] = value & 0x01
            else:
                return None

        else:
            return None
    # End __setitem__

    def getValue(self):
        # Reset field to 0 to calculate
        self._value = 0

        for idx, bit in enumerate(self.bits):
            self._value |= (bit.value << idx)

        return self._value
    # End getValue

    def setValue(self, value):
        for idx, bit in enumerate(self.bits):
            # Extract value
            mask = 1 << idx
            value_to_write = (value & mask) >> idx
            bit.value = value_to_write & 0x1
    # End setValue

    def delValue(self):
        del self._value
    # End delValue

    value = property(getValue, setValue, delValue, )
# End Register

if __name__ == '__main__':
    bit_fields = [(0, 'RW'), (1, 'RW'), (2, 'RW'), (3, 'RW'), (4, 'RW'), (5, 'RW'), (6, 'RW'), (7, 'RW')]
    reg = Register(0x00, bit_fields, 8)

    print(hex(reg.value))

    reg.value = 0x32

    print(hex(reg.value))

    reg.value = 0x00

    print(hex(reg.value))
    