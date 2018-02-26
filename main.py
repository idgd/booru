import sys
import json
from hashlib import sha256

file_hash = sha256()

# syntax: booru -t tag1 tag2 tag3 -f file1 file2 file3
args = sys.argv[1:]

files = {}
tags = {}
out = {}

t_index = args.index("-t") + 1
f_index = args.index("-f") + 1
t_list = args[t_index : f_index - 1]
f_list = args[f_index:]

file_hashes = []

for f in f_list:
	with open(f,"rb") as g:
		h = file_hash.copy()
		h.update(g.read())
		file_hashes.append(h.hexdigest())

for h in file_hashes:
	files[h] = { "name" : f_list[file_hashes.index(h)],
               "tags" : t_list }

for t in t_list:
	tags[t] = file_hashes

out = { "files" : files,
        "tags" : tags }

with open("db.json","w") as db:
	json.dump(out,db,indent=2)
