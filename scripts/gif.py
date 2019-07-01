import imageio, glob
import argparse

parser = argparse.ArgumentParser(description='generate gif')
parser.add_argument('--exp', dest='exp')
parser.add_argument('--dest', dest='dest', default=None)

args = parser.parse_args()

dest = args.dest or args.exp
anim_file = '{}.gif'.format(dest)

with imageio.get_writer(anim_file, mode='I') as writer:
  filenames = glob.glob('./samples/{}/1111/interpZY*.jpg'.format(args.exp))
  filenames.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
  last = -1
  for i,filename in enumerate(filenames):
    frame = 20*(i**0.5)
    if round(frame) > round(last):
      last = frame
    else:
      continue
    image = imageio.imread(filename)
    writer.append_data(image)
  image = imageio.imread(filename)
  writer.append_data(image)
