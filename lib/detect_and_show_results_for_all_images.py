from PIL import Image
import PIL
from numpy import asarray
from lib.print_match import print_match
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

def detect_and_show_results(image_path):
  image = Image.open(image_path)

  image = image.resize(
    (299, 299),
    PIL.Image.BILINEAR).convert('RGB')

  data = asarray(image)  # np.array(image.getdata(), 'float32')

  faces = detector.detect_faces(data)

  num_faces = len(faces)

  if num_faces > 0:
    print_match(image_path)

def detect_and_show_results_for_all_images(image_paths):
  for image_path in image_paths:
    detect_and_show_results(image_path)