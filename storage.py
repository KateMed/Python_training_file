import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
parser.add_argument('-r')
namespace = parser.parse_args()
b = namespace.val
a = namespace.key
c = namespace.r

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'r') as f:
    if f.read() == '' or c is not None:
        with open(storage_path, 'w') as f:
            json.dump(dict(), f)
    else:
        f.seek(0)
        data = json.load(f)
  #      print(data)

if b is None:
    if a not in data:
        print(None)
    else:
        print(data[a])
elif a in data:
    data[a] += ', ' + (b)
    json_data = json.dumps(data)
    with open(storage_path, 'w') as f:
        f.write(json_data)
  #  print('d', data)
else:
    with open(storage_path, 'w') as f:
        data[a]=b
        json.dump(data, f)#    print('d', data)

