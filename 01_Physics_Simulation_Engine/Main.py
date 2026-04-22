import numpy as np
from math import cos, sin, pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

while True:
    print("Welcome to the Physics Simulator Engine !!")
    print("Choose from the below options: ")
    print("1. Projectile simulation")
    print("2. Simple Pendulum Simulation")
    print("3. Spring Block System Simulation")
    print("4. Exit")
    user_input = input("Enter from the options (1-4): ")

    
    if user_input == "1":
            #Defining Projectile Simulation Physics/Logic

        def Projectile_sim():
            t = 0
            x0 = 0
            y0 = 0
            dt = 0.01
            user_theta = int(input("Enter the projectile angle: "))
            theta = user_theta*(pi/180)
            u0 = int(input("Enter the projectile velocity: "))
            u0_x = u0*cos(theta)
            u0_y = u0*sin(theta)
            accel_0 = -9.8

            position_data_x = []
            position_data_y = []
            velocity_data_x = []
            velocity_data_y = []
            time_data = []

            while y0 >= 0:
                new_time = t + dt
                t = new_time
                v_final_x = u0_x
                u0_x = v_final_x
                v_final_y = u0_y + accel_0*(dt)
                u0_y = v_final_y
                x_final = x0 + v_final_x*(dt)
                x0 = x_final
                y_final = y0 + v_final_y*(dt)
                y0 = y_final

                position_data_x.append(x0)
                position_data_y.append(y0)
                velocity_data_x.append(u0_x)
                velocity_data_y.append(u0_y)
                time_data.append(t)


            return position_data_x, position_data_y, velocity_data_x, velocity_data_y, time_data
    
        #Animating the Projectile Simulation

        x, y, _, _, _ = Projectile_sim()

        fig, ax = plt.subplots()
        ax.set_title("Projectile Simulation")
        ax.set_xlabel("X-Coordinate (Distance)")
        ax.set_ylabel("Y-Coordinate (Height)")
        ax.set_xlim(0, max(x))
        ax.set_ylim(0, max(y))

        point,  = ax.plot([], [], 'o')
        line,  = ax.plot([], [], '-')

        def init():
            point.set_data([], [])
            line.set_data([], [])
            return point, line
    
        def update(i):
            point.set_data([x[i]], [y[i]])
            line.set_data(x[:i], y[:i])
            return point, line
        
        anim = FuncAnimation(fig, update, frames = len(x), init_func = init)
        anim.save("proj_p1.mp4")
        plt.show()
        break
    
    if user_input == "2":

        #Defining Pendulum Simulation Physics/Logic

        def Pendulum_Sim():
            
            t = 0
            dt = 0.25
            user_theta = int(input("Enter the angle of the pendulum: "))
            Len_string = int(input("Enter the length of the string: "))
            user_vel = int(input("Enter the velocity of the pendulum:"))
            omega_inital = user_vel/Len_string
            theta = user_theta*(pi/180)
            ang_acc = -(9.8/Len_string)*sin(theta)

            position_dist_x=[Len_string*sin(theta)]
            position_dist_y = [-Len_string*cos(theta)]

            T_max = 10

            while t < T_max:
                new_time = t + dt
                t = new_time
                omega_final = omega_inital + ang_acc*dt
                omega_inital = omega_final
                theta = theta + omega_final*dt
                ang_acc = -(9.8/Len_string)*sin(theta)

                x_cord_final_position = Len_string*sin(theta)
                y_cord_final_position = -Len_string*cos(theta)

                position_dist_x.append(x_cord_final_position)
                position_dist_y.append(y_cord_final_position)

            return position_dist_x, position_dist_y, Len_string
        
        #Animating the Projectile Simulation

        x, y, z = Pendulum_Sim()

        fig, ax = plt.subplots()
        ax.set_title("Pendulum Simulation")
        ax.set_xlabel("X-Coordinate (Distance)")
        ax.set_ylabel("Y-Coordinate (Height)")
        ax.set_xlim(-z, z)
        ax.set_ylim(-z, z)
        ax.plot(0,0, 'ro')

        point,  = ax.plot([], [], 'o')
        line,  = ax.plot([], [], '-')

        def init():
            point.set_data([], [])
            line.set_data([], [])
            return point, line
    
        def update(i):
            point.set_data([x[i]], [y[i]])
            line.set_data([0, x[i]],[0, y[i]])
            return point, line
        
        anim = FuncAnimation(fig, update, frames = len(x), init_func = init)
        anim.save("proj_p2.mp4")
        plt.show()
        break

    if user_input == "3":
    
        #Defining the Spring Block System Physics/Logic
        def Spring_sim():
            t = 0
            dt = 0.1
            Length_spring = int(input("Enter the length of the spring: "))
            spring_coeff = int(input("Enter the spring coefficient: "))
            y = 0.1
            u0 = 0
            ball_mass = int(input("Enter the mass of ball: "))
            acc = -(spring_coeff*y/ball_mass)

            position_dis_y = [y]

            T_max = 10

            while t < T_max:
                new_time = t + dt
                t = new_time
                final_velocity = u0 + acc*(dt)
                u0 = final_velocity
                y_new = y + final_velocity*dt
                y = y_new
                new_acc = -(spring_coeff*y/ball_mass)
                acc = new_acc

                position_dis_y.append(y_new)

            return position_dis_y
        
        #Animation the Spring Block System
        x = Spring_sim()

        fig, ax = plt.subplots()
        ax.set_title("Spring Block Simulation")
        ax.set_xlabel("X-Coordinate (Distance)")
        ax.set_ylabel("Y-Coordinate (Height)")
        ax.set_xlim(-1, 1)
        ax.set_ylim(min(x), max(x))
        ax.plot(0, 0, 'ro')

        point,  = ax.plot([], [], 'o')
        line,  = ax.plot([], [], '-')

        def init():
            point.set_data([], [])
            line.set_data([], [])
            return point, line
    
        def update(i):
            point.set_data([0], [x[i]])
            line.set_data([0, 0], [0, x[i]])
            return point, line
        
        anim = FuncAnimation(fig, update, frames = len(x), init_func = init)
        anim.save("proj_p3.mp4")
        plt.show()
        break

    if user_input == "4":
        break