from cdragontoolbox.hashes import HashGuesser, GameHashGuesser, LcuHashGuesser
from cdragontoolbox.wad import Wad
import time
import glob
import signal
import sys
import logging
# logging.basicConfig(level='INFO')

start_time = time.time()

unknown_hashes = HashGuesser.unknown_from_export("export") # Used for hash guessing methods later
print("Started grepping game files.") # Guess game hashes
myguess_game = GameHashGuesser.from_wads([Wad(path) for path in glob.glob(r"G:\Riot Games\PBE\Game\DATA\FINAL\**\*.wad.client", recursive=True)])
unknown_hashes |= myguess_game.unknown
for wad in myguess_game.wads:
    wad.guess_extensions()
    unknown_before = len(myguess_game.unknown)
    myguess_game.grep_wad(wad)
    found_hashes = unknown_before - len(myguess_game.unknown)
    if found_hashes:
        print(f"found game hashes: {found_hashes}")
s = signal.signal(signal.SIGINT, signal.SIG_IGN)
myguess_game.save() #save guessed game hashes
signal.signal(signal.SIGINT, s)
print("Finished grepping game files.")

print("Started grepping lcu files.") # Guess lcu hashes
lcu_wads = [Wad(path) for path in glob.glob(r"G:\Riot Games\PBE\Plugins\**\*.wad", recursive=True)]
myguess_lcu = LcuHashGuesser.from_wads([Wad(path) for path in glob.glob(r"G:\Riot Games\PBE\Plugins\**\*.wad", recursive=True)])
unknown_hashes |= myguess_lcu.unknown
for wad in myguess_lcu.wads:
    wad.guess_extensions()
    unknown_before = len(myguess_lcu.unknown)
    myguess_lcu.grep_wad(wad)
    found_hashes = unknown_before - len(myguess_lcu.unknown)
    if found_hashes:
        print(f"found lcu hashes: {found_hashes}")
s = signal.signal(signal.SIGINT, signal.SIG_IGN)
myguess_lcu.save() #save guessed lcu hashes
signal.signal(signal.SIGINT, s)
print("Finished grepping lcu files.")

print(time.time() - start_time)

# Run some guessing methods
print("Started guessing game hashes...")
logging.basicConfig(level='INFO')

game_guess = GameHashGuesser(unknown_hashes)
game_guess.guess_skin_groups_bin_using_chromas()
game_guess.check_basename_prefixes()
game_guess.substitute_suffixes()
game_guess.substitute_extensions()
game_guess.substitute_numbers()
game_guess.substitute_skin_numbers()
game_guess.substitute_lang()
game_guess.guess_characters_files()
game_guess.substitute_character()

print("Started guessing lcu hashes...")
lcu_guess = LcuHashGuesser(unknown_hashes)
lcu_guess.substitute_region_lang()
lcu_guess.substitute_plugin()
lcu_guess.substitute_numbers()
lcu_guess.guess_patterns()
lcu_guess.guess_from_game_hashes()
