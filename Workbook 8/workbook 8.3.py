import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/gradedata.csv")
plt.scatter(df['hours'], df['grade'])
plt.show()