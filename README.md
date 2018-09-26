# Template

Template is a cli wrapper for string.Template.

## Usage

```sh
$ cat sample.txt
ham: $HAM
egg: $EGG

$ ./bin/template HAM=ham EGG=spam sample.txt
ham: ham
egg: spam

$ ./bin/template HAM=ham EGG=spam sample.txt -o output.txt
$ cat output.txt
ham: ham
egg: spam

```

## Updating

```sh
$ docker pull rhoboro/template:latest
```

