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
       "files" : { "" : { "name" : "", "tags" : []  } } }
	with open("db.json","w+") as f:
		json.dump(i,f,indent=2)
else:
	with open("db.json") as f:
		i = json.load(f)

# utility
tags = i["tags"]
files = i["files"]

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

def t_empty():
	print("Tags:")
	for f in i["tags"].keys():
		print("  ", f)

def f_empty():
	print("Files:")
	for f in i["files"].values():
		print("  ", f["name"])

def tf():
	h_to_append = []
	for f in a["f"]:
		with open(f,"rb") as g:
			h = file_hash.copy()
			h.update(g.read())
			new_hash = h.hexdigest()
			h_to_append.append(new_hash)
			files[new_hash] = { "tags" : a["t"], "name" : f}

	for t in a["t"]:
		tags[t] = h_to_append

	w()

def t():
	for f in a["t"]:
		if f in tags:
			for g in tags[f]:
				print(files[g]["name"])
		else:
			tags[f] = []

		w()

def f():
	h_check = []
	for f in a["f"]:
		with open(f,"rb") as g:
			h = file_hash.copy()
			h.update(g.read())
			h_check.append(h.hexdigest())

	for f in h_check:
		if f in files:
			print("Name: " + str(files[f]['name']) + "\nTags: " + str(files[f]['tags']) + "\n")

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

def w():
	i["tags"] = tags
	i["files"] = files

	with open("db.json","w") as f:
		json.dump(i,f,indent=2)
