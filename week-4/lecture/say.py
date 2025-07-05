import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex(f"Hello, my name is {sys.argv[1]}")
