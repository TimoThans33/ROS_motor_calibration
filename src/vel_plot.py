import rospy
import matplotlib.pyplot as plt
import numpy as np
from std_msgs.msg import UInt32
import python_classes.globals as global_var

#globals = global_var.GLOBALS()
#globals.initialize()
global cur_vel
cur_vel = 0
plt.style.use('ggplot')
fig = plt.figure(figsize=(13, 6))
ax = fig.add_subplot(111)

def callback(data):
    global cur_vel
    cur_vel = int(data.data)

def live_plotter(x_vec, y1_data, line1, identifier='velocity profile', pause_time=0.01):
    if line1==[]:
        plt.ion()
        line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.8)
        plt.ylabel('Y label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    line1.set_ydata(y1_data)
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])

    plt.pause(pause_time)
    return line1
def main():
    global cur_vel
    rospy.init_node('plotter', anonymous=True)
    rospy.Subscriber("cur_vel", UInt32, callback)
    x_vec = range(50)
    y_vec = [0] * 50
    line1 = []
    while not rospy.is_shutdown():
        y_vec[-1] = cur_vel
        line1 = live_plotter(x_vec, y_vec, line1)
        y_vec = np.append(y_vec[1:], 0.0)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass