import statistics as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('scores.csv')
df.describe(include='all')
df['Test 1'].plot(kind='box', title='Test 1 Boxplot')
plt.show()
df['Test 2'].plot(kind='box', title='Test 2 Boxplot')
plt.show()
df['Test 3'].plot(kind='box', title='Test 3 Boxplot')
plt.show()
