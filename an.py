import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag

dane = pd.read_csv(r"sub1trial16.csv", delimiter=',', engine='python')

t = np.linspace (0, 37.92, 200*37.92)
prob=200
sygnal = dane['kol2']

przefiltrowany = ag.pasmowozaporowy(sygnal, prob, 49, 51)
przefiltrowany = ag.pasmowoprzepustowy(przefiltrowany, prob, 1, 50)

plt.plot(t, sygnal)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.plot(przefiltrowany)
plt.show()
