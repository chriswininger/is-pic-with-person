from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

def highlight_faces(image, faces):
  # display image
  plt.imshow(image)

  ax = plt.gca()

  # for each face, draw a rectangle based on coordinates
  for face in faces:
    x, y, width, height = face['box']
    face_border = Rectangle((x, y), width, height,
                            fill=False, color='red')
    ax.add_patch(face_border)
  plt.show()