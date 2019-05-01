import logging # Change the default logger settings for more information
logging.basicConfig(level='INFO')
from cdragontoolbox.data import Language
from cdragontoolbox.wad import Wad
from cdragontoolbox.hashes import HashFile, HashGuesser, hashfile_lcu, LcuHashGuesser, hashfile_game, glob, os, build_wordlist
import string
unknown_hashes = HashGuesser.unknown_from_export("export")
unknown_hashes -= set(hashfile_game.load()) # Remove unnecessary game hashes
lcu_guess = LcuHashGuesser(unknown_hashes) # create the instance
wordlist = lcu_guess.build_wordlist() # create a wordlist
swordlist = build_wordlist(p.rsplit('/', 1)[-1] for p in lcu_guess.known.values() if any(ext in p for ext in ['.json'])) # create a special shorter wordlist for higher iteration potential
# print(swordlist)
# with open("G:/Dokumente/Utility Tools/unxxhash/helpers/wordlist_webm.txt", "w+") as out_file: # write wordlist for c++ program
#    for word in sorted(swordlist):
#         out_file.write(f"{word}\n")

print(f"Wordlist length: {len(wordlist)} ({len(swordlist)})")

mylist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
# Iterate multiple paths; print out missing hashes
extensions = set()
for path in lcu_guess.known.values():
    _, ext = os.path.splitext(path)
    extensions.add(ext)
ext = list(extensions)
# print(extensions)
# lcu_guess.check_basenames(f"{a}/gold_i7.png" for a in wordlist)
# lcu_guess.check_iter(f"plugins/rcp-fe-lol-loot/global/default/assets/loot_item_icons/chest_{a}_{b}.png" for b in wordlist for a in wordlist)
# myguess = HashGuesser(hashfile_lcu, unknown_hashes)
# myguess.check_xdbg_hashes(path="G:/Dokumente/Utility Tools/x64dbg/release/x32/log-Di Mrz 12 07-23-50 2019.txt")
lcu_guess.substitute_region_lang()
lcu_guess.substitute_plugin()
# lcu_guess.substitute_basenames()
# lcu_guess.substitute_basename_words(nold=1, nnew=1)
# lcu_guess.substitute_basename_words(plugin="rcp-fe-lol-loot", fileext=".png", words=wordlist, nold=1, nnew=2)
# lcu_guess.add_basename_word()
import timeit
# t = timeit.timeit("lcu_guess.check_basenames(f'{a}.png' for a in lcu_guess.build_wordlist())", "from cdragontoolbox.hashes import HashGuesser, LcuHashGuesser; unknown_hashes = HashGuesser.unknown_from_export(\"export\"); lcu_guess = LcuHashGuesser(unknown_hashes)", number=1)
# t = timeit.timeit("lcu_guess.substitute_basenames()", "from cdragontoolbox.hashes import HashGuesser, LcuHashGuesser; unknown_hashes = HashGuesser.unknown_from_export(\"export\"); lcu_guess = LcuHashGuesser(unknown_hashes)", number=1)
# t = timeit.timeit("lcu_guess.substitute_basename_words()", "from cdragontoolbox.hashes import HashGuesser, LcuHashGuesser; unknown_hashes = HashGuesser.unknown_from_export(\"export\"); lcu_guess = LcuHashGuesser(unknown_hashes)", number=1)
# print(t)
import cProfile
# cProfile.run("lcu_guess.check_basenames(f'{a}.png' for a in swordlist)")
import dis
#dis.dis(HashGuesser._substitute_basename_words)
lcu_guess.substitute_numbers()
lcu_guess.guess_patterns()
lcu_guess.guess_from_game_hashes()
lcu_guess.save() #save guessed hashes
