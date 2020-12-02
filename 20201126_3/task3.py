import sys
import struct


data = sys.stdin.buffer.read()

try:
    if data[:4].decode() != "RIFF" or data[8:12].decode() != "WAVE" or data[12:16].decode() != "fmt " or data[36:40].decode() != "data":
        print("NO")
        exit()

    Size = struct.unpack_from("i", data, 4)[0]
    Type = struct.unpack_from("h", data, 20)[0]
    Channels = struct.unpack_from("h", data, 22)[0]
    Rate = struct.unpack_from("i", data, 24)[0]
    Bits = struct.unpack_from("h", data, 34)[0]
    Data_size = struct.unpack_from("i", data, 40)[0]

    print("Size=", Size, ", Type=", Type, ", Channels=", Channels, ", Rate=",
          Rate, ", Bits=", Bits, ", Data size=", Data_size, sep="")
except struct.error:
    print("NO")
