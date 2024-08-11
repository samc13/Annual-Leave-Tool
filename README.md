# Annual-Leave-Tool

A personal tool for summarising used annual leave used, booked, and remaining

## Installation

Well, you'll need python for a start: 

```bash
brew install python;
```

Make sure it worked, try: 

```bash
python3 --version;
```

You'll also need [PIP](https://pypi.org/project/pip/). 

PIP is a package manager for Python packages, or modules if you like.

If you've got Python3 3.4+, you should already have `pip`. 

To install a module, you can run: 

```bash
python3 -m pip install
``` 

followed by the name of a module, such as `numpy`.

## Running it

Python is easy to run in a terminal. You can just call the script using your `python3` command (it might be nice to define an alias for this). 

```bash
> python3 myDebutPythonScript.py
```

If you have a nice Python script, you can even then make it an executable to call as/when you wish without being in the directory of the file, and without the `python3` prefix. 

You'll need to add a shebang line at the start of the file:

```
#!/usr/bin/env python3
```

If you then mark the file as executable: 

```bash
chmod +x myDebutPythonScript.py
```

That then unlocks the power to run using `./`: 

```bash
./myDebutPythonScript.py
```

If you'd like to be able to run it without the `./`, which is an elite gamer move, you'll need to "install" the script by copying it across into a `/bin` directory.

For custom/local/user files, you should probably stick them into the `/usr/bin` directory. 

```bash
cp myDebutPythonScript.py /usr/bin/myDebutPythonScript
```

(it's nice to drop the `.py` suffix)

Then do the old `chmod +x` on the copy of the file there: 

```bash
chmod +x /usr/bin/myDebutPythonScript
```

So long as you've got `/usr/bin` in your `$PATH` (type `echo $PATH` to check), this should then be runnable using the *very pretty*: 

```bash
> myDebutPythonScript
```