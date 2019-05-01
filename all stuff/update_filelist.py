import requests
from multiprocessing.pool import ThreadPool
import re
import glob
from cdragontoolbox.hashes import hashfile_lcu

# Download and save all *.filelist.txt files
urls = [(f"./filelists/{n_season}.{n_patch}.filelist.txt", f"https://raw.communitydragon.org/{n_season}.{n_patch}.filelist.txt")
       for n_season in range(7, 10) for n_patch in range(1, 25)]
urls.append(("./filelists/pbe.filelist.txt", "https://raw.communitydragon.org/pbe.filelist.txt"))

def fetch_url(entry):
    path, url = entry
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb+') as f:
            for chunk in r:
                f.write(chunk)
    return

for _ in ThreadPool(25).imap_unordered(fetch_url, urls):
    pass


# Filelists for patch 8.2 and lower aren't up-to-date, so we'll update them here
known_values = hashfile_lcu.load()
unknown_line = re.compile(r"^.*/unknown/([0-9a-f]{16}).*$")
for file in glob.glob("filelists/*.filelist.txt"):
    lines = []
    with open(file) as in_file:
        for line in in_file:
            m = unknown_line.match(line)
            if m:
                if int(m.group(1), 16) in known_values.keys():
                    line = f"{known_values[int(m.group(1), 16)]}\n"
            lines.append(line)
    with open(file, "w") as out_file:
        for line in lines:
            out_file.write(line)
