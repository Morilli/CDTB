import struct
data = open("G:/Dokumente/LeagueDownloader_1_0_2_0/DATA.wad/lol_game_client/releases/0.0.1.190/files/DATA/FINAL/DATA.wad/unknown/1de85b3040e21426", "rb").read()
count, = struct.unpack('<L', data[:4])
i = 4 # Skip the header
paths = []
for _ in range(count):
    n, = struct.unpack('<L', data[i:i+4])
    paths.append(data[i+4:i+4+n])
    i = i+4+n
assert i == len(data)

# Guess the hashes
from cdragontoolbox.hashes import GameHashGuesser, hashfile_lcu, glob
import logging # Change the default logger settings for more information
logging.basicConfig(level='INFO')
unknown_hashes = set()
for path in glob.glob('export/*.unknown.txt'): # Store all unknown hashes in unknown_hashes
    with open(path) as f:
        unknown_hashes |= {int(h, 16) for h in f}
        unknown_hashes -= set(hashfile_lcu.load()) # Remove unnecessary lcu hashes
game_guess = GameHashGuesser(unknown_hashes) # create the instance
myarray = []
for k in range(count):
    myarray.append(paths[k].decode("utf-8").lower())
print("Starting guess...")
game_guess.check_iter(f"{a}" for a in myarray)
#game_guess.substitute_extensions()
game_guess.save() #save guessed hashes
exit()




# Unnecessary and superseded by the code above
with open ("G:/Dokumente/LeagueDownloader_1_0_2_0/temp_gutenmorgen/lol_game_client/releases/0.0.1.161/files/DATA/FINAL/Scripts.wad/unknown/9292a9c26c1abd6b", "rt") as in_file:
    contents = in_file.read()

open("./output.txt", "w")
current_position = 0
while True:
    current_position = contents.find("\0\0\0", current_position)
    print("current_position =", current_position, "/", len(contents))
    if (current_position == -1):
        print("Der angegebene Separator konnte nicht gefunden werden. Das Programm wird beendet.")
        break
    current_path = ""
    for i in range(current_position+3,current_position+1000):
        if (i >= len(contents)):
            print(len(contents))
            print("Ende der Eingabedatei erreicht. Das Programm wird beendet.")
            exit()
        if (contents[i] == "\0"):
            current_path = current_path[:-1]
            current_path += "bin"
            current_position = i
            break
        current_path += contents[i]
    with open("./output.txt", "a") as out_file:
        out_file.write(current_path+"\n")
    print(current_path, end="\n")
