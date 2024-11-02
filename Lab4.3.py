import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt('GEFCOM.txt')
dataset = d[:, 2]

T = 365

beta1_values = []  # To store beta1 values for each hour
beta2_values = []  # To store beta2 values for each hour

for h in range(24):
    data_h = dataset[h::24]
    #train_data = data_h[:T]
    #test_data = data_h[T:]

    #X2 = np.roll(train_data, -7)
    X2 = data_h[0:T-7]
    #X1 = np.roll(train_data, -1)
    X1 = data_h[6:T-1]
    X0 = np.ones(np.shape(X1))
    #Y = train_data
    Y = data_h[7:T]

    X = np.column_stack([X0, X1, X2])
    betas = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

    beta1_values.append(betas[1])  # Append beta1 for this hour
    beta2_values.append(betas[2])  # Append beta2 for this hour
    print(len(beta1_values))

print(len(X1), len(X2), len(Y)) #358
print(X1)
# Plotting the beta values for each hour
hours = np.arange(24)
plt.figure(figsize=(10, 6))
plt.plot(hours, beta1_values, label='Beta1')
plt.plot(hours, beta2_values, label='Beta2')
plt.xlabel('Hour')
plt.ylabel('Beta Values')
plt.title('Values of Beta1 and Beta2 for Each Hour')
plt.legend()
plt.grid(True)
plt.show()

