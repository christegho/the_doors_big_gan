from PIL import Image
import os

for subdir in ['lizards']:
    directory = 'data/doors/{}'.format(subdir)
    list_files = os.listdir(directory)

    for filename in list_files:
      try:
        filename = os.path.join(directory, filename)
        im = Image.open(filename)
        im.verify()
        im.close()
      except:
        print(filename)
        os.remove(filename)
