import sys
import os
import json
from hashlib import sha256

### needed variables

# generator
file_hash = sha256()

# input
args = sys.argv[1:]
if not os.path.exists("db.json"):
	i = {"tags" : { "" : [] },
       "files" : { "" : { "" : "", "" : []  } } }
	with open("db.json","w+") as f:
		json.dump(i,f,indent=2)
else:
	with open("db.json") as f:
		i = json.load(f)

# utility
files = i["files"]
tags = i["tags"]
file_hashes = []

d = ""
a = {"t" : [],
     "f" : [],
     "s" : []}

for f in args:
	if f == "-t":
		d = "t"
	elif f == "-f":
		d = "f"
	elif f == "-s":
		d = "s"
	else:
		a[d].append(f)

### functions

def t():
	if not a["t"]:
		print("Tags:")
		for f in i["tags"].keys():
			print("  ", f)
	return

def f():
	if not a["f"]:
		print("Files:")
		for f in i["files"].values():
			print("  ", f["name"])
	return

def tf():

	if i["files"].keys():
		file_hashes += list(i["files"].keys())

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

	return

def s():
	return

def h():
	print("""-t tag tag1 ... -f file file1 ... - associates listed tags with listed files
-t -f - lists all tags and all files
-t tag tag1 ... - lists all files associated with tags, adds tags if they don't exist
-t - lists all tags
-f file file1 ... - lists all files with each's tags
-f - lists all files
-s - searches for tag""")
