import numpy as np
import matplotlib.pyplot as plt

file_prefix = '../assets/citcount'

fig = plt.figure(1, figsize=(10, 6))

citations = np.array([1, 4, 11, 12, 20, 43, 110])
index = np.arange(len(citations))
bar_width = 0.5

plt.xkcd()
plt.title('Brief history of fairness in ML')
plt.bar(index, citations, bar_width, color='r')
plt.ylabel('Papers')
plt.xticks(index, [2011, 2012, 2013, 2014, 2015, 2016, 2017])
plt.yticks([])
plt.tight_layout()
plt.savefig(file_prefix + '-1.svg')
plt.annotate('LOL FAIRNESS!!', xy=(1, 50))
plt.savefig(file_prefix + '-2.svg')
plt.annotate('OH, CRAP.', xy=(4, 70))
plt.savefig(file_prefix + '-3.svg')
plt.savefig(file_prefix + '-3.png')
