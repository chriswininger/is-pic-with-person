from os import listdir
from os.path import isfile, isdir, join
from lib.is_image_file import is_image_file

def get_file_path_for_all_files_in_dir(dir_path, is_recursive=False):
  paths = [dir_path]
  only_images = []

  while(len(paths) > 0):
    current_path = paths.pop()

    files = [join(current_path, f) for f in listdir(current_path) if isfile(join(current_path, f))]

    only_images = only_images + list(filter(is_image_file, files))

    if is_recursive:
      child_dirs = [join(current_path, f) for f in listdir(current_path) if isdir(join(current_path, f))]
      paths = paths + child_dirs

  return only_images
