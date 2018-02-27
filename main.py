import sys
import json
from hashlib import sha256

args = sys.argv[1:]
files = {}
tags = {}
out = {}
with open("db.json") as f:
	i = json.load(f)

if "-t" and "-f" in args:
	file_hash = sha256()

	t_index = args.index("-t") + 1
	f_index = args.index("-f") + 1
	t_list = args[t_index : f_index - 1]
	f_list = args[f_index:]

	if not t_list or not f_list:
		print("Tags:")
		for f in i["tags"].keys():
			print("  ", f)
		print("Files:")
		for f in i["files"].values():
			print("  ", f["name"])

	for f in i["files"].keys():
		print(f)

	if i["files"].keys():
		file_hashes = list(i["files"].keys())
	else:
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
elif "-t" in args:
	print("")
elif "-f" in args:
	print("")
elif "-s" in args:
	print("")
elif "-h" in args:
	print("""-t tag tag1 ... -f file file1 ... - associates listed tags with listed files
-t -f - lists all tags and all files
-t tag tag1 ... - lists all files associated with tags, adds tags if they don't exist
-t - lists all tags
-f file file1 ... - lists all files with each's tags
-f - lists all files
-s - searches for tag""")
elif not args:
	print("booru version 0.1\ntagging software")
else:
	print("invalid input\n-h for help")
