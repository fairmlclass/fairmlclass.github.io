import matplotlib.pyplot as plt
import numpy as np

def roc_base():
  """Plot basic roc curve"""
  plt.figure(1, figsize=(4, 4))
  x = np.linspace(0, 1, 200)
  plt.subplot(111)
  plt.plot(x, x, color='r')
  plt.title('ROC curve', fontsize=18)
  plt.xlabel('False positive rate', fontsize=18)
  plt.ylabel('True positive rate', fontsize=18)
  plt.gca().set_xticks([0, 0.5, 1])
  plt.gca().set_yticks([0, 0.5, 1])
  plt.xlim(0, 1)
  plt.ylim(0, 1)
  plt.tight_layout()

roc_base()
plt.savefig('../assets/roc_curve_0.svg')

x = np.linspace(0, 1, 200)
plt.plot(x, x**0.2, color='g', label='a')
plt.savefig('../assets/roc_curve_1.svg')

plt.plot(x, x**0.5, color='b', label='b')
plt.legend(loc=4, title='Group')
plt.tight_layout()
plt.savefig('../assets/roc_curve_2.svg')
