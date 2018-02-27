# booru
A local booru-style software for managing arbitrary files.

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

* tags and files to json dotfile
* list all tags
* search tags
* add new tags
* list all files
* search files by tag
* add tags to file
* hashing capabilities
