import sys
import pykd

try:
    usage = "Usage: .load pykd\nUsage: !py c:\location\of\script"

    arg1 = (int(sys.argv[1], base=16))
    arg2 = (int(sys.argv[2], base=16))
    addrSpace = int(arg2) - int(arg1)
    opcodes = (pykd.loadBytes(arg1,addrSpace))
    pop = {0x59,0x5A,0x5D,0x58,0x5E}
    ret = {0xC3}


    for x in range (len(opcodes) -2):
        if opcodes[x] in pop and opcodes[x+1] in pop and opcodes[x+2] in ret:
            memlocation = (hex(x + (arg1)))
            print(f"POP POP RET found at:", memlocation)

except IndexError:
    print(usage)
       
