import os

dir = os.listdir(os.path.join("data"))

l = [""] * 66

for item in dir:
  os.rename(os.path.join("data", item), os.path.join("data", item + ".txt"))

print(l)