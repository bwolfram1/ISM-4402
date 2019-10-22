#74 and 76

import pandas as pd
import matplotlib.pyplot as plt
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grade = [76,95,77,78,99]
GradeList = zip(names,status,grade)
df = pd.DataFrame(data = GradeList,
                  columns = ['Names','Status','Grades'])
df.plot(kind='bar')
plt.annotate('Wow!',
             xy =(0,76),
             arrowprops=dict(facecolor='black',
                             shrink=0.05))