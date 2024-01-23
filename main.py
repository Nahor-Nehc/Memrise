import os
from components.find import *
from components.files import *

import time
import matplotlib.pyplot as plt

times = []

for i in range(100):
  start = time.perf_counter_ns()
  l = get()
  end = time.perf_counter_ns()
  times.append((end - start)*(10**(-1*9)))

plt.hist(times)
plt.show()