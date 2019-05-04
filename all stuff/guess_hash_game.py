import logging # Change the default logger settings for more information
logging.basicConfig(level='INFO')
from cdragontoolbox.wad import Wad # For the grep_wad function
from cdragontoolbox.hashes import HashGuesser, GameHashGuesser, hashfile_lcu, glob, os, build_wordlist
import string
unknown_hashes = HashGuesser.unknown_from_export("export")
unknown_hashes -= set(hashfile_lcu.load()) # Remove unnecessary lcu hashes
game_guess = GameHashGuesser(unknown_hashes) # create the instance
wordlist = game_guess.build_wordlist() # create a wordlist
swordlist = build_wordlist(p.rsplit('/', 1)[-1] for p in game_guess.known.values() if any(ext in p for ext in ['.dds'])) # create a special shorter wordlist for higher iteration potential
print(f"Wordlist length: {len(wordlist)} ({len(swordlist)})")
#print(f"Amount of unknown hashes: {len(game_guess.unknown)}")


# Iterate multiple paths; print out missing hashes
#with open("G:/Downloads/Map11LEVELS.wad-Hash-v8.24b-1018.txt") as in_file:
#    myarray = in_file.read().lower().split("\n")
#game_guess.check_iter(f"{a}" for a in myarray)
#for a in myarray:
#    print(a)


extensions = set()
for path in game_guess.known.values():
    _, ext = os.path.splitext(path)
    extensions.add(ext)
ext = list(extensions)
mystring = f"hotpursuitmarker.luabin"
#print(mystring.lower())
# game_guess.check_iter(f"{mystring.lower()}" for e in extensions)

# game_guess.check_basenames(f"ghostporoai.luabin" for a in "ab")
# game_guess.check_iter(f"assets/characteres/yuumi/skins/skin0{b}/yuumi_skin0{b}_desk_tx_cm.yuumi.dds" for b in range(20) for a in wordlist)
# game_guess.substitute_basenames()
# game_guess.substitute_basename_words()
# game_guess.grep_file(r"G:\Dokumente\Utility Tools\LeagueDownloader_1_0_2_0\game_old\lol_game_client\releases\0.0.1.101\files\DATA\FINAL\Maps\Shipping\Map11.wad\unknown\4081e5c462798b73.bin")
# game_guess.grep_wad(Wad(r"G:\Riot Games\PBE\Game\DATA\FINAL\Champions\Graves.wad.client"))
# game_guess.guess_skin_groups_bin()
# game_guess.guess_skin_groups_bin_using_chromas()
# game_guess.check_basename_prefixes()
# game_guess.substitute_suffixes()
# game_guess.substitute_extensions()
# game_guess.substitute_numbers()
# game_guess.substitute_skin_numbers()
# game_guess.substitute_lang()
# game_guess.guess_characters_files()
# game_guess.substitute_character()
# game_guess.add_basename_word()
game_guess.save() #save guessed hashes
