import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv", encoding="cp1251")

r = 102303244

ar = 0.05 * (r % 7)
br = 0.3 * ((r % 5) + 1)

x = df["no2"].values
x = x[~np.isnan(x)]

z = x + ar * np.sin(br * x)

print("ar:", ar)
print("br:", br)
print(z[:5])

mu = np.mean(z)
sigma2 = np.var(z)

lam = 1 / (2 * sigma2)
c = 1 / np.sqrt(2 * np.pi * sigma2)

print("mu:", mu)
print("lambda:", lam)
print("c:", c)


z_range = np.linspace(min(z), max(z), 500)
p_hat = c * np.exp(-lam * (z_range - mu) ** 2)

plt.hist(z, bins=50, alpha=0.6)
plt.plot(z_range, p_hat, "r")
plt.savefig("histogram.png")
plt.show()
