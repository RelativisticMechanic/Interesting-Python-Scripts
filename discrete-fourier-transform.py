'''
Discrete Fourier Transform for any function along with
visualization with matplotlib.
'''

import matplotlib.pyplot as plt
import math
import numpy as np

delta_t = 0.001
function_range = np.arange(-6 * np.pi, 6 * np.pi + delta_t, delta_t)

t = [t for t in function_range]
f = [(-x if (x < -2) else np.sin(x)) if (x < 0) else x for x in function_range]

def get_FT(t, f, w):
    f_cos_wt = 0
    f_sin_wt = 0

    for t_i in range(1, len(t)):
        # F cos(wt) dt
        f_cos_wt += f[t_i] * np.cos(w * t[t_i]) * (t[t_i] - t[t_i - 1])
        # F sin(wt) dt
        f_sin_wt += f[t_i] * np.sin(w * t[t_i]) * (t[t_i] - t[t_i - 1])
    
    return (f_cos_wt, f_sin_wt)

def get_FT_Real(t, f, w):
    return get_FT(t, f, w)[0]

def get_FT_Imag(t, f, w):
    return get_FT(t, f, w)[1]


def generate_FT(t, f, w_start, w_end):
    w = np.linspace(w_start, w_end, 1000)
    DFT_Real = get_FT_Real(t, f, w)
    DFT_Imag = get_FT_Imag(t, f, w)
    return (w, DFT_Real, DFT_Imag)

w, DFT_Real, DFT_Imag = generate_FT(t, f, -3, 3)

plt.rcParams["figure.figsize"] = (20, 10)
fig = plt.figure()
ax = plt.subplot(2, 2, 1)

ax.plot(t, f)
ax.set_xlim(xmin=min(function_range)*2, xmax=max(function_range)*2)
ax.axhline(0, color="red", linestyle="--")
ax.axvline(0, color="red", linestyle="--")
ax.set_title("Function")

ax2 = plt.subplot(2, 2, 2)
ax2.set_title("Fourier Transform")
ax2.plot(w, DFT_Real, color="green", label="Real")
ax2.plot(w, DFT_Imag, color="blue", label="Imag")
ax2.axhline(0, color="red", linestyle="--")
ax2.axvline(0, color="red", linestyle="--")
ax2.legend()

ax3 = plt.subplot(2, 2, 3, projection="3d")
ax3.plot(w, DFT_Real, DFT_Imag)

plt.show()
