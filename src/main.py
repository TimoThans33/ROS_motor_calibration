import rospy
from tkinter import *
from std_msgs.msg import String
from python_classes.UI import Window
import python_classes.globals as global_var
import threading



globals = global_var.GLOBALS()
globals.initialize()

def start_root():
    root = Tk()
    topframe = Window(root)
    topframe.init_coefbtn()

    middleframe = Window(root)
    middleframe.init_stateentry()
    middleframe.pack()

    bottomframe = Window(root)
    bottomframe.init_velentry()
    #graphframe = Window(root)
    #graphframe.init_graph(fig)


    #ani = animation.FuncAnimation(f, animate, interval=5)
    #size of the window
    root.geometry("400x300")
    root.mainloop()

def talker():
    pub = rospy.Publisher('par_val', String, queue_size=10)
    rospy.init_node('GUI', anonymous=True)
    #rate =rospy.Rate(10)
    while not rospy.is_shutdown():
        if global_var.vel_event == True:
            msg_str = "V{:3d}".format(global_var.target_velocity)
            pub.publish(msg_str)
            rospy.loginfo(msg_str)
            global_var.vel_event = False
        if global_var.kp_event == True:
            msg_str = "Kp{:d}".format(global_var.kp)
            pub.publish(msg_str)
            rospy.loginfo(msg_str)
            global_var.kp_event = False
        if global_var.kd_event == True:
            msg_str = "Kd{:d}".format(global_var.kd)
            pub.publish(msg_str)
            rospy.loginfo(msg_str)
            global_var.kd_event = False
        if global_var.ki_event == True:
            msg_str = "Ki{:d}".format(global_var.ki)
            pub.publish(msg_str)
            rospy.loginfo(msg_str)
            global_var.ki_event = False
        if global_var.state_event == True:
            msg_str = "S{:d}".format(global_var.state)
            pub.publish(msg_str)
            rospy.loginfo(msg_str)
            global_var.state_event = False
        #rate.sleep()


if __name__ == '__main__':
    try:
        UI_thread = threading.Thread(target=start_root)
        UI_thread.start()
        talker()
    except rospy.ROSInterruptException:
        pass