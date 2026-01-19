import numpy as np

# 1. Tablica 3x3 wypełniona zerami
tablica = np.zeros((3, 3), dtype=int)

# 2. Wypełnienie zaznaczonych obszarów (przekątna) jedynkami
np.fill_diagonal(tablica, 1)

print(tablica)
