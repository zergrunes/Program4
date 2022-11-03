import statistics as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('planets.csv')
print(df)
# between diameter and mass
print('Correlation between diameter and mass:\n')
print(df['Diam'].corr(df['Mass']))
# between distance and temp
print('\nCorrelation between distance and temperature:\n')
print(df['Distance'].corr(df['Temp']))
# between period and day
print('\nCorrelation between period and day:\n')
print(df['Period'].corr(df['Day']))
