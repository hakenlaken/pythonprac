import struct

with open("data/3.in", "wb") as f:
    f.write(struct.pack("4s", "RIFF".encode()))
    f.write(struct.pack("i", 108208))
    f.write(struct.pack("4s", "WAVE".encode()))
    f.write(struct.pack("4s", "fmt ".encode()))
    f.write(struct.pack("i", 16))
    f.write(struct.pack("h", 1))
    f.write(struct.pack("h", 2))
    f.write(struct.pack("i", 44100))
    f.write(struct.pack("i", 176400))
    f.write(struct.pack("h", 4))
    f.write(struct.pack("h", 16))
    f.write(struct.pack("4s", "data".encode()))
    # f.write(struct.pack("i", 108172))
