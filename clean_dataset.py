from PIL import Image
import os

for subdir in ['add', 'airplane', 'arrow', 'arrows', 'avatar', 'badge', 'bag', 'bank', 'basket', 'battery', 'bell', 'book', 'bookmark', 'bottle', 'box', 'boy', 'briefcase', 'building', 'bus', 'business', 'cake', 'calculator', 'calendar', 'camera', 'car', 'cart', 'chair', 'chart', 'chat', 'check', 'check mark', 'clipboard', 'clock', 'cloud', 'coffee', 'coin', 'compass', 'computer', 'credit card', 'cross', 'crown', 'delete', 'desk', 'diamond', 'document', 'dollar', 'down', 'download', 'edit', 'email', 'emoticon', 'envelope', 'eye', 'file', 'fish', 'flag', 'flower', 'folder', 'gear', 'ghost', 'gift', 'girl', 'glass', 'glasses', 'globe', 'graph', 'handbag', 'happy', 'hat', 'headphones', 'heart', 'home', 'house', 'ice cream', 'idea', 'image', 'key', 'knife', 'lamp', 'laptop', 'leaf', 'light bulb', 'like', 'location', 'lock', 'love', 'mail', 'man', 'map', 'map pin', 'medal', 'menu', 'message', 'microphone', 'mobile', 'money', 'monitor', 'moon', 'mouse', 'music', 'network', 'pen', 'pencil', 'phone', 'pie chart', 'pin', 'plant', 'play', 'plus', 'presentation', 'printer', 'profile', 'radio', 'refresh', 'right', 'robot', 'rocket', 'search', 'settings', 'share', 'shield', 'shirt', 'shopping bag', 'shopping cart', 'smartphone', 'smile', 'snowflake', 'speaker', 'speech bubble', 'star', 'sun', 'sword', 'table', 'tag', 'target', 'telephone', 'television', 'time', 'tree', 'trophy', 'truck', 'umbrella', 'up', 'upload', 'user', 'video', 'wallet', 'watch', 'wifi']:
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
