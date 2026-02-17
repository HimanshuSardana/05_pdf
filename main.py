import numpy as np
import pandas as pd

df = pd.read_csv("data.csv", encoding="cp1251")

r = 102303244

ar = 0.05 * (r % 7)
br = 0.3 * ((r % 5) + 1)

x = df["no2"].values

z = x + ar * np.sin(br * x)

print("ar:", ar)
print("br:", br)
print(z[:5])
