import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#GENERATE DATA
jumlah_data=100

x = np.array([i*0.1+np.random.randn() for i in range(jumlah_data)])
y = np.array([i*0.1 for i in range(jumlah_data)])

#FUNGSI LINEAR
def fungsiLinear(x,gradien):
    y = gradien*x
    return y

#PERHITUNGAN PERSAMAAN LINEAR AWAL
x_predict = np.array([0,10])    
m_init = 5
y_predict = fungsiLinear(x_predict, m_init)

#PERHITUNGAN PREDIKSI
m_predict = m_init
m_list_predict = []
y_list_predict = []
x_list_predict = []
learning_rate = 0.1

for i in range(1,jumlah_data):
    y_predict = fungsiLinear(x[i], m_predict)
    y_actual = y[i]

    error = y_actual - y_predict
    delta_m = learning_rate*error/x[i]
    m_predict = m_predict + delta_m

    m_list_predict.append(m_predict)
    y_list_predict.append(fungsiLinear(np.array([0,10]), m_predict))
    x_list_predict.append(np.array([0,10]))


#VISUALISASI DATA
fig = plt.figure(figsize=(4,4))
line, = plt.plot([], [])

def animate(frame_num):
    x = x_list_predict[frame_num]
    y = y_list_predict[frame_num]
    line.set_data((x, y))
    return line

anime = FuncAnimation(fig, animate, frames=100, interval=100, repeat=False)
plt.scatter(x,y, color='red')
plt.axis([0,10,0,10])
plt.show()