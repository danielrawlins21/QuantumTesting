import numpy as np

# Define parameters and initial conditions
Wf_h, Wf_x, bf = 0, 0, -100
Wi_h, Wi_x, bi = 0, 100, 100
Wc_h, Wc_x, bc = -100, 50, 0
Wo_h, Wo_x, bo = 0, 100, 0
h_minus_1 = 0
c_minus_1 = 0

# Input sequence
input_sequence = [1, 1, 0, 1, 1]

# Initialize lists to store ct and ht values
c_values = []
h_values = []

# Iterate over the input sequence
for xt in input_sequence:
    # Compute ft, it, ot, and ctilde using LSTM equations
    ft = 1 / (1 + np.exp(-(Wf_h * h_minus_1 + Wf_x * xt + bf)))
    it = 1 / (1 + np.exp(-(Wi_h * h_minus_1 + Wi_x * xt + bi)))
    ot = 1 / (1 + np.exp(-(Wo_h * h_minus_1 + Wo_x * xt + bo)))
    ctilde = np.tanh(Wc_h * h_minus_1 + Wc_x * xt + bc)
    
    # Compute ct and ht
    c = ft * c_minus_1 + it * ctilde
    h = ot * np.tanh(c)
    
    # Update previous states
    h_minus_1 = h
    c_minus_1 = c
    
    # Append ct and ht to the lists
    c_values.append(c)
    h_values.append(h)

# Print the computed ct and ht values
for t, (ct, ht) in enumerate(zip(c_values, h_values)):
    print(f"Time step {t} - ct: {ct}, ht: {ht}")
