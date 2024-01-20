import numpy as np
from matplotlib import pyplot as plt
t=np.array([10, 10, 10, 10, 30, 40, 40, 50, 70, 70, 80, 80, 80, 80, 100,100,100])
kubelki = [0,20,40,60,80,100]
hist=np.histogram(t, bins=kubelki)
print(hist[0]) # (*) Histogram zawarty jest w pierwszej wartości zwracanej tupli, tu [4 1 3 2 7]
print(kubelki)
plt.hist(t, bins = kubelki)
plt.title("Histogram")
plt.show()