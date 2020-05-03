class GLOBALS():
    def initialize(self):
        global vel_event
        global kp_event
        global kd_event
        global ki_event
        global state_event
        global target_velocity
        global kp
        global kd
        global ki
        global state
        global cur_vel
        vel_event = False
        kp_event = False
        kd_event = False
        ki_event = False
        state_event = False
        target_velocity = 0
        kp = 35
        kd = 60
        ki = 0
        state = 1
        cur_vel = 0
