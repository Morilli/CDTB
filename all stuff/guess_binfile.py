import logging # Change the default logger settings for more information
logging.basicConfig(level='INFO')
import string
from cdragontoolbox import binfile

with open("G:/Downloads/binHashes.txt") as in_file:
    hashes = in_file.read().split("\n")

unknown_values = {h for h in hashes}
# print(unknown_values)

with open("G:/Dokumente/GitHub/CDTB/cdragontoolbox/hashes.bin_new.txt") as f:
    hashes = (l.strip().split(' ', 1) for l in f)
    baum = {f"{int(h):08x} {s}" for h, s in hashes}
# print(baum)
with open("./hashes.bin_new_test.txt", "w+") as out_file:
    for b in sorted(baum):
        out_file.write(b + "\n")
exit()
mystring = "eying"
hashvalue = binfile.compute_binhash(mystring)
print(hashvalue)
if str(hashvalue) in unknown_values:
    print("new")
    print(hashvalue)
    with open("./found_binhashes.txt", "a+") as out_file:
        out_file.write(mystring + "\n")
# print(f"{hashvalue:08x}")
