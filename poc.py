import os
from os import path

print("Item exists:" + str(path.exists("mods.py")))
if not(path.exists("meth.py")):
	print("no")