import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt('GEFCOM.txt')
data = d[:, 2]
data_L = d[:, 4]

T = 365
forecast_list = []
real_list = []
err_h = []

# Loop through each hour
for h in range(24):
    p_hour = data[h::24]
    p_hour_L = data_L[h::24]

    # Calibrate betas using a fixed window of T days for each hour
    cal_data = p_hour[:T]
    cal_data_L = p_hour_L[:T]
    X3 = cal_data[0:T - 7]
    X2 = cal_data[5:T - 2]
    X1 = cal_data[6:T - 1]
    X0 = np.ones(np.shape(X1))
    Y = cal_data[7:T]
    X4 = cal_data_L[7:T]

    X = np.column_stack([X0, X1, X2, X3, X4])
    betas = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))

    # Forecast for each hour beyond the calibration window
    for day in range(T, len(p_hour)):
        real = p_hour[day]
        X_fut = np.array([1, p_hour[day - 1], p_hour[day - 2], p_hour[day - 7], p_hour_L[day]])
        forecast = np.dot(X_fut, betas)
        forecast_list.append(forecast)
        real_list.append(real)
        err_h.append(np.abs(forecast - real))

# Plotting the results
plt.figure(1)
plt.plot(real_list, label="real")
plt.plot(forecast_list, label="forecast")
plt.title('Forecast and Real')
plt.xlabel('Hour')
plt.ylabel('Zonal prices')
plt.grid()
plt.legend()
plt.show()

plt.figure(2)
plt.plot(err_h, label='errors hourly')
plt.legend()
plt.title('Forecast Errors')
plt.xlabel('Hour')
plt.ylabel('Absolute Errors')
plt.grid()
plt.show()
