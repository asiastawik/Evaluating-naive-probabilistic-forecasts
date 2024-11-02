import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt('GEFCOM.txt')
data = d[:, 2]
data_L = d[:, 4]

T = 365
forecast_list = []
real_list = []
err_h = []

for h in range(24):
    p_hour = data[h::24]
    p_hour_L = data_L[h::24]
    for day in range(T, len(p_hour)):
        real = p_hour[day]
        print(real)
        cal_data = p_hour[day-T:day] #0:T
        cal_data_L = p_hour_L[day - T:day]  # 0:T
        X3 = cal_data[0:T-7]
        X2 = cal_data[5:T-2]
        X1 = cal_data[6:T-1]
        X0 = np.ones(np.shape(X1))
        Y = cal_data[7:T]
        X4 = cal_data_L[7:T]

        X = np.column_stack([X0, X1, X2, X3, X4])
        betas = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
        X_fut = np.array([1, cal_data[T-1], cal_data[T-2], cal_data[T-7], p_hour_L[T]])
        forecast = np.dot(X_fut, betas)
        #real = p_hour[day]
        forecast_list.append(forecast)
        real_list.append(real)
        err_h.append(np.abs(forecast-real))

plt.figure(1)
plt.plot(real_list, label="real")
plt.plot(forecast_list, label="forecast")
plt.title('Forecast and Real')
plt.xlabel('Hour')
plt.ylabel('Zonal prices')
plt.grid()
plt.show()

plt.figure(2)
plt.plot(err_h, label='errors hourly')
plt.legend()
plt.title('Forecast and Real')
plt.xlabel('Hour')
plt.ylabel('Zonal prices')
plt.grid()
plt.show()