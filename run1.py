from matplotlib import pyplot as plt


fig, ax = plt.subplots()

ax.plot([1,2,3,4],[4,3,5,5])

plt.close()

fig.savefig('test.png')

