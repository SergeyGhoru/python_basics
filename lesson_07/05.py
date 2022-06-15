import os
import sys
from pprint import pprint


help = "Give 1 argument - folder to get statistics by extensions"
stat = {100: (0, []), 1000: (0, []), 10000: (0, []), 100000: (0, [])}

if len(sys.argv) > 2 or len(sys.argv) == 1:
    print(help)
    sys.exit()
else:
    folder = sys.argv[1]

for item in os.listdir(folder):
    obj = os.path.join(folder, item)
    if not os.path.isdir(obj):
        size = os.stat(obj).st_size
        filename, ext = os.path.splitext(item)

        if size > 100000:
            count, curr_ext = stat[100000]
            if ext not in curr_ext:
                curr_ext.append(ext)
            stat[100000] = count + 1, curr_ext
        elif size > 10000:
            count, curr_ext = stat[10000]
            if ext not in curr_ext:
                curr_ext.append(ext)
            stat[10000] = count + 1, curr_ext
        elif size > 1000:
            count, curr_ext = stat[1000]
            if ext not in curr_ext:
                curr_ext.append(ext)
            stat[1000] = count + 1, curr_ext
        else:
            count, curr_ext = stat[100]
            if ext not in curr_ext:
                curr_ext.append(ext)
            stat[100] = count + 1, curr_ext

pprint(stat)
