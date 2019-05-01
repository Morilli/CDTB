from cdragontoolbox.hashes import HashGuesser, GameHashGuesser, hashfile_lcu
import string
unknown_hashes = HashGuesser.unknown_from_export("export")
unknown_hashes -= set(hashfile_lcu.load())
game_guess = GameHashGuesser(unknown_hashes) # create the instance
wordlist = game_guess.build_wordlist() # create a wordlist
print(f"Wordlist length: {len(wordlist)}")
# print(f"Missing hashes: {game_guess.unknown}")
print(f"Amount of unknown hashes: {len(game_guess.unknown)}")
from cdragontoolbox.data import Language
characters = game_guess.get_characters()
locales = [l.value for l in Language]
skins = ["base", "skin01", "skin02", "skin03", "skin04", "skin05", "skin06", "skin07", "skin08", "skin09", "skin10",
         "skin11", "skin12", "skin13", "skin14", "skin15", "skin16", "skin17", "skin18", "skin19", "skin20", "skin21",
         "skin22", "skin23", "skin24", "skin25", "skin26", "skin27", "skin28", "skin29", "skin30", "skin31", "skin32", "skin33"]
fileend = ["audio.bnk", "audio.wpk","events.bnk", "events.wpk"]
wise = ["wwise", "wwise2016", "wwise_remix"]
game_guess.check_iter(f"assets/sounds/{w}/vo/{l}/characters/{c}/skins/{s}/{c}{z}_{s}_vo_{f}" for l in locales for w in wise for c in characters for s in skins for z in ["","_future"] for f in fileend)
print("1. Iteration completed")

game_guess.check_iter(f"assets/sounds/{w}/vo/{l}/shared/announcer_global_{z}{a}_vo_{f}" for w in wise for l in locales for z in ["","female1_"] for a in wordlist for f in fileend)
print("2. Iteration completed")
game_guess.check_iter(f"assets/sounds/{w}/vo/{l}/shared/announcer_{a}{z}_vo_{f}" for w in wise for l in locales for a in wordlist for z in ["","_female1","_female1project","_thresh"] for f in fileend)
print("3. Iteration completed")
game_guess.check_iter(f"assets/sounds/{w}/vo/{l}/shared/{p}_{a}_vo_{f}" for w in wise for l in locales for p in ["misc","npc"] for a in wordlist for f in fileend)
print("4. Iteration completed")

game_guess.check_iter(f"assets/sounds/{w}/sfx/characters/{c}/skins/{s}/{c}_{s}_sfx_{f}" for w in wise for c in characters for s in skins for f in fileend)
print("5. Iteration completed")
game_guess.check_iter(f"data/menu/fontconfig_{l}.txt" for l in locales)
game_guess.save() #save guessed hashes
