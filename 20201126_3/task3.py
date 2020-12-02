import struct


L, B = "H", "I"
name = input()

seekarr = [4, 20, 22, 24, 34, 40]
fmtarr = [B, L, L, B, L, B]
resarr = [0, 0, 0, 0, 0, 0]
if name.endswith(".wav"):
    F = open(name, "rb")
    for i in range(6):
        F.seek(seekarr[i])
        resarr[i] = struct.unpack(fmtarr[i], F.read(struct.calcsize(fmtarr[i])))[0]
    print("Size={0}, Type={1}, Channels={2}, Rate={3}, Bits={4}, Data size={5}".format(resarr[0], resarr[1],
                                                                                       resarr[2], resarr[3], resarr[4], resarr[5]))
    F.close()
else:
    print("NO")
