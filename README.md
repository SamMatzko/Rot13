# Rot13
A simple command-line Python program to make Rot13 ciphers (created for those on [Puzzling Stack Exchange](https://puzzling.stackexchange.com/)).

## Installation
Just put it wherever you want it.

## Usage
To rot13 a message, simply run `rot13.py`. Then, when the `Message:` prompt shows, type in the message you want to decode or encode. The program will then output the resulting message.

Here's an example:

```
$ python3 rot13.py
Message: Hello, world!
Uryyb, jbeyq!
$ python3 rot13.py
Message: Uryyb, jbeyq!
Hello, world!
```

## Making it an executable (on Linux)
To make it an executable, move it to `/usr/bin/` or `/home/<username>/.local/bin/`. If you want, you can rename it from `rot13.py` simply to `rot13`. You also need to add `#! /usr/bin/python3` at the top of the program. 

Then, run `chmod +x rot13` (or `chmod +x rot13.py`). Now, you can run it in the terminal using `rot13`, no matter what directory your terminal is in!
