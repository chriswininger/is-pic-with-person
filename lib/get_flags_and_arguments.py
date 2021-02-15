import sys

FLAG_PREFIX = '--'

def get_flags_and_arguments():
  flags = {}

  agruments = []

  for arg in sys.argv[1:]:
    if arg.startswith(FLAG_PREFIX):
      flags[arg.replace(FLAG_PREFIX, '')] = True
    else:
      agruments.append(arg)

  return (flags, agruments)
