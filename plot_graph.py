import matplotlib.pyplot as plt
import numpy as np

x,y = np.loadtxt('epoch_loss.csv', unpack=True, delimiter=',')

plt.plot(x,y, marker='o')

plt.xlabel ('epoch')
plt.ylabel ('loss')
plt.title('epoch v/s loss curve')
plt.savefig('epoch_loss_curve.png')
plt.show()


