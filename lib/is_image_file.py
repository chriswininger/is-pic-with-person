EXTENSIONS = ['jpeg', 'jpg', 'png']

def is_image_file(file_path):
  for ext in EXTENSIONS:
    if ext in file_path.lower():
      return True

  return False