import os


FOLDER = "."
stat = {100: 0, 1000: 0, 10000: 0, 100000: 0}

for item in os.listdir(FOLDER):
    obj = os.path.join(FOLDER, item)
    if not os.path.isdir(obj):
        size = os.stat(obj).st_size
        filename, ext = os.path.splitext(item)
        if size > 100000:
            stat[100000] += 1
        elif size > 10000:
            stat[10000] += 1
        elif size > 1000:
            stat[1000] += 1
        else:
            stat[100] += 1

print(stat)
