# booru
A local booru-style software for managing arbitrary files.

# syntax

* `-t tag tag1 ... -f file file1 ...` - associates listed tags with listed files
* `-t -f` - lists all tags and all files
* `-t tag tag1 ...` - lists all files associated with tags, adds tags if they don't exist
* `-t` - lists all tags
* `-f file file1 ...` - lists all files with each's tags
* `-f` - lists all files
* `-s` - searches for tag

# struct

Creates a json dotfile in home. The structure is:

```
{
  "tags": {
    "tag1": [
      "sha-hash-of-file",
      "sha-hash-of-file2"
    ]
  }
  "files" : {
    "sha-hash-of-file": {
      "name": "/absolute/directory"
      "tags": [
        "tag1",
        "tag2"
      ]
    }
  }
}
```

# todo

* update hashes
