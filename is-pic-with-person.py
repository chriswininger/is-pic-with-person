#!/usr/bin/python

import os

# supress tensor flow logs (must be done immediately)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from lib.get_flags_and_arguments import get_flags_and_arguments
from lib.get_file_path_for_all_files_in_dir import get_file_path_for_all_files_in_dir
from lib.detect_and_show_results_for_all_images import detect_and_show_results_for_all_images

# === Main Code Body ===
flags_and_args = get_flags_and_arguments()
flags = flags_and_args[0]
args = flags_and_args[1]

dir_path = args[0]

is_recursive = 'recursive' in flags and flags['recursive']

print('searching "{}"'.format(dir_path))

image_paths = get_file_path_for_all_files_in_dir(dir_path, is_recursive)

#print(image_paths)
detect_and_show_results_for_all_images(image_paths)
