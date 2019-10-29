#82,86,87
import pandas as pd

df = pd.read_csv("datasets/gradedata.csv")
df.hist(column="age", by="gender")