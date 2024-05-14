import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 105, 5)
y1 = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y2 = np.array([10000, 8000, 6000, 4000, 2000, 0])
print(len(x))
fig, ax = plt.subplots()

ax.plot(x, y1, label='No delay', linestyle='-')
ax.plot(x, y2, label='Delayed labelling (10,000)', linestyle='--')

ax.set_xlim(-5, 105)
ax.set_ylim(-500, 11000)
ax.set_xlabel('# instances (thousands)')
ax.set_ylabel('# drifts detected')

ax.set_title('Drifts detected by a 10 learner SRP model using ADWIN on AGRAWAL with and without labelling delay')
ax.legend(loc='upper left')

plt.show()