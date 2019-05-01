import requests
from multiprocessing.pool import ThreadPool
import glob
from cdragontoolbox.hashes import hashfile_lcu, hashfile_game

# Download and save all *.unknown.txt files
urls = [(f"./export/{n_season}.{n_patch}.unknown.txt", f"https://raw.communitydragon.org/{n_season}.{n_patch}.unknown.txt")
       for n_season in range(7, 10) for n_patch in range(1, 25)]
urls.append(("./export/pbe.unknown.txt", "https://raw.communitydragon.org/pbe.unknown.txt"))

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
known_values = {**hashfile_lcu.load(), **hashfile_game.load()}
for file in glob.glob("export/*.unknown.txt"):
    lines = []
    with open(file) as in_file:
        for line in in_file:
            if int(line, 16) not in known_values.keys():
                lines.append(line)
    with open(file, "w") as out_file:
        for line in lines:
            out_file.write(line)


# Obsolete
# urllib = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where(), num_pools=50)
# # Handle pbe.unknown.txt explicitly
# pbe_request = urllib.request("GET", "https://raw.communitydragon.org/pbe.unknown.txt")
# if str(pbe_request.status).startswith("2"):
#     with open("./export/pbe.unknown.txt", "w+", newline="\n") as out_file:
#         out_file.write(pbe_request.data.decode())

# for n_season in range(7, 10):
#     for n_patch in range(1, 25):
#         request = urllib.request("GET", f"https://raw.communitydragon.org/{n_season}.{n_patch}.unknown.txt")
#         if str(request.status).startswith("2"):
#             with open(f"./export/{n_season}.{n_patch}.unknown.txt", "w+", newline="\n") as out_file:
#                 out_file.write(request.data.decode())
