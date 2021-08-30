from numpy.lib.index_tricks import fill_diagonal
import pandas as pd
import plotly_express as px
import numpy as np

df = pd.read_csv("main.csv")

gre_score = df["GRE Score"].tolist()

chance_of_admit = df["Chance"].tolist()

gre = np.array(gre_score)
c_o_a = np.array(chance_of_admit)

m,c = np.polyfit(gre,c_o_a,1)
print(m,c)

y_list = []
for i in range(0, len(gre_score)):
    y_value = m*gre_score[i]+c
    y_list.append(y_value)
    
fig = px.scatter(x=gre_score, y=chance_of_admit)
fig.update_layout(shapes=[dict(type="line", y0=min(
    y_list), y1=max(y_list), x0=min(gre_score), x1=max(gre_score))])
fig.show()