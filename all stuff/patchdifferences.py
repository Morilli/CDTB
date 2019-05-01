
old_version = "8.24"
current_version = "9.1"

import requests
data = set(requests.get(f"https://raw.communitydragon.org/{current_version}.filelist.txt").text.split("\n"))
data -= set(requests.get(f"https://raw.communitydragon.org/{old_version}.filelist.txt").text.split("\n"))

with open("./output.txt", "w+") as out_file:
    out_file.write(f"Files added from version {old_version} to version {current_version}:\n\n")
    for path in sorted(data):
        out_file.write(f"{path}\n")