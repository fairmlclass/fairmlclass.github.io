import os
import sys


def include_files(file_name):
  """Search file for include statements and replace with file contents."""
  with open(file_name, 'r') as f:
    lines = f.readlines()
    for line in lines:
      tokens = line.split('@@ INCLUDE ')
      if len(tokens) > 1:
        file_input = tokens[1][:-1]
        assert os.path.exists(file_input), "File must exist: %s." % file_input
        with open(file_input, 'r') as fi:
          print fi.read()
      else:
        print line


assert len(sys.argv) > 1, "Must provide filename."
file_name = sys.argv[1]
assert os.path.exists(file_name), "File must exist: %s." % file_name
include_files(file_name)
