import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy import signal

while True:
    print("Welcome to the signal/wave generator: ")
    print("Choose from the below options: ")
    print("1. Sine Wave: ")
    print("2. Cosine Wave: ")
    print("3. Square: ")
    print("4. Sawtooth: ")
    print("5. Inteference")
    print("6. Exit")

    choice = input("Enter your choice(1 - 6):  ")

    if choice == "1":
        def SineWave():
            frequency = int(input("Enter the frequency of the wave: "))
            amplitude = int(input("Enter the amplitude of the wave: "))
            phase = int(input("Enter the phase of the wave: "))
            
            t = np.linspace(0, 5, 100)
            y = amplitude*np.sin(2*np.pi*frequency*t + phase)
            
            return t, y

        t, y = SineWave()

        fig, ax = plt.subplots()
        ax.set_title("Sine Wave")
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.set_xlim(min(t), max(t))
        ax.set_ylim(2*min(y), 2*max(y))
        ax.grid(True)
                
        point, = ax.plot([], [], 'o')
        line, = ax.plot([], [], '-')

        def init():
            point.set_data([], [])
            line.set_data([], [])
            return point, line
                
        def update(i):
            point.set_data([t[i]], [y[i]])
            line.set_data(t[:i], y[:i])
            return point, line
                
        anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
        anim.save("sine_wave.mp4")
        plt.show()
        break

    if choice == "2":
        def CosineWave():
            frequency = int(input("Enter the frequency of the wave: "))
            amplitude = int(input("Enter the amplitude of the wave: "))
            phase = int(input("Enter the phase of the wave: "))
            
            t = np.linspace(0, 5, 100)
            y = amplitude*np.cos(2*np.pi*frequency*t + phase)
            
            return t, y

        t, y = CosineWave()

        fig, ax = plt.subplots()
        ax.set_title("Cosine Wave")
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.set_xlim(min(t), max(t))
        ax.set_ylim(2*min(y), 2*max(y))
        ax.grid(True)
                
        point, = ax.plot([], [], 'o')
        line, = ax.plot([], [], '-')

        def init():
            point.set_data([], [])
            line.set_data([], [])
            return point, line
                
        def update(i):
            point.set_data([t[i]], [y[i]])
            line.set_data(t[:i], y[:i])
            return point, line
                
        anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
        anim.save("cosine_wave.mp4")
        plt.show()
        break

    if choice == "3":
        def Square():
            frequency = int(input("Enter the frequency of the wave: "))
            t = np.linspace(0, 5, 100)
            y = signal.square(2*np.pi*frequency*t)
            
            return t, y

        t, y = Square()

        fig, ax = plt.subplots()
        ax.set_title("Square Wave")
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.set_xlim(min(t), max(t))
        ax.set_ylim(2*min(y), 2*max(y))
        ax.set_aspect('equal')
        ax.grid(True)
                
        point, = ax.plot([], [], 'o')
        line, = ax.plot([], [], '-')

        def init():
            point.set_data([], [])
            line.set_data([], [])
            return point, line
                
        def update(i):
            point.set_data([t[i]], [y[i]])
            line.set_data(t[:i], y[:i])
            return point, line
                
        anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
        anim.save("square_wave.mp4")
        plt.show()
        break

    if choice == "4":

        def Sawtooth():
            frequency = int(input("Enter the frequency of the wave: "))
            t = np.linspace(0, 5, 100)
            y = signal.sawtooth(2*np.pi*frequency*t)
            
            return t, y

        t, y = Sawtooth()

        fig, ax = plt.subplots()
        ax.set_title("Sawtooth Wave")
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.set_xlim(min(t), max(t))
        ax.set_ylim(2*min(y), 2*max(y))
        ax.set_aspect('equal')
        ax.grid(True)
                
        point, = ax.plot([], [], 'o')
        line, = ax.plot([], [], '-')

        def init():
            point.set_data([], [])
            line.set_data([], [])
            return point, line
                
        def update(i):
            point.set_data([t[i]], [y[i]])
            line.set_data(t[:i], y[:i])
            return point, line
                
        anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
        anim.save("sawtooth_wave.mp4")
        plt.show()
        break

    if choice == "5":
        print("Choose from the below: ")
        print("1. Constructive Interference")
        print("2. Destructive Interference")
        user_input = input("Enter the type of interference you want:")

        if user_input == "1":

            print("which type of constructive interference do you want? ")
            print("1. sine wave + sine wave")
            print("2. sine wave + cosine wave")
            print("3. sine wave + square wave")
            print("4. sine wave + sawtooth wave")
            print("5. cosine wave + cosine wave")
            print("6. cosine wave + square wave")
            print("7. cosine wave + sawtooth wave")
            print("8. square wave + square wave")
            print("9. square wave + sawtooth wave")
            print("10. sawtooth wave + sawtooth wave")

            user_Choice2 = (input("choose from the options (1-10): "))

            t = np.linspace(0, 5, 100)

            def SineWave():
                frequency = int(input("Enter the frequency of the wave: "))
                amplitude = int(input("Enter the amplitude of the wave: "))
                phase = int(input("Enter the phase of the wave: "))
                phi = np.deg2rad(phase)
                y = amplitude*np.sin(2*np.pi*frequency*t + phi)
                
                return y
        
            def CosineWave():
                frequency = int(input("Enter the frequency of the wave: "))
                amplitude = int(input("Enter the amplitude of the wave: "))
                phase = int(input("Enter the phase of the wave: "))
                phi = np.deg2rad(phase)
                
                y = amplitude*np.cos(2*np.pi*frequency*t + phi)
                
                return y
            
            def Square():
                frequency = int(input("Enter the frequency of the wave: "))
                
                y = signal.square(2*np.pi*frequency*t)
                
                return y

            def Sawtooth():
                frequency = int(input("Enter the frequency of the wave: "))
                
                y = signal.sawtooth(2*np.pi*frequency*t)
                
                return y
            
            if user_Choice2 == "1":

                y = SineWave() + SineWave()

                fig, ax = plt.subplots()
                ax.set_title("Sine & Sine constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                        
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                        
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                        
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sine+sine_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "2":

                y = SineWave() + CosineWave()

                fig, ax = plt.subplots()
                ax.set_title("Sine & Cosine constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sine+cosine_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "3":

                y = SineWave() + Square()

                fig, ax = plt.subplots()
                ax.set_title("Sine & Square constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sine+square_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "4":

                y = SineWave() + Sawtooth()

                fig, ax = plt.subplots()
                ax.set_title("Sine & Sawtooth constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sine+sawtooth_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "5":

                y = CosineWave() + CosineWave()

                fig, ax = plt.subplots()
                ax.set_title("Cosine & Cosine constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("cosine+cosine_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "6":

                y = CosineWave() + Square()

                fig, ax = plt.subplots()
                ax.set_title("Cosine & Square constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("cosine+square_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "7":

                y = CosineWave() + Sawtooth()

                fig, ax = plt.subplots()
                ax.set_title("Cosine & Sawtooth constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("cosine+sawtooth_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "8":

                y = Square() + Square()

                fig, ax = plt.subplots()
                ax.set_title("Square & Square constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("square+square_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "9":

                y = Square() + Sawtooth()

                fig, ax = plt.subplots()
                ax.set_title("Square & Sawtooth constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("square+sawtooth_const_int.mp4")
                plt.show()
                break

            if user_Choice2 == "10":

                y = Sawtooth() + Sawtooth()

                fig, ax = plt.subplots()
                ax.set_title("Sawtooth & Sawtooth constructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sawtooth+sawtooth_const_int.mp4")
                plt.show()
                break


        elif user_input == "1":

            print("which type of destructive interference do you want? ")
            print("1. sine wave - sine wave")
            print("2. sine wave - cosine wave")
            print("3. sine wave - square wave")
            print("4. sine wave - sawtooth wave")
            print("5. cosine wave - cosine wave")
            print("6. cosine wave - square wave")
            print("7. cosine wave - sawtooth wave")
            print("8. square wave - square wave")
            print("9. square wave - sawtooth wave")
            print("10. sawtooth wave - sawtooth wave")

            user_Choice3 = (input("choose from the options (1-10): "))

            t = np.linspace(0, 5, 100)

            def SineWave():
                frequency = int(input("Enter the frequency of the wave: "))
                amplitude = int(input("Enter the amplitude of the wave: "))
                phase = int(input("Enter the phase of the wave: "))
                phi = np.deg2rad(phase)
                y = amplitude*np.sin(2*np.pi*frequency*t + phi)
                
                return y
        
            def CosineWave():
                frequency = int(input("Enter the frequency of the wave: "))
                amplitude = int(input("Enter the amplitude of the wave: "))
                phase = int(input("Enter the phase of the wave: "))
                phi = np.deg2rad(phase)
                
                y = amplitude*np.cos(2*np.pi*frequency*t + phi)
                
                return y
            
            def Square():
                frequency = int(input("Enter the frequency of the wave: "))
                
                y = signal.square(2*np.pi*frequency*t)
                
                return y

            def Sawtooth():
                frequency = int(input("Enter the frequency of the wave: "))
                
                y = signal.sawtooth(2*np.pi*frequency*t)
                
                return y
            
            if user_Choice3 == "1":

                y = SineWave() - SineWave()

                fig, ax = plt.subplots()
                ax.set_title("Sine & Sine destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                        
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                        
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                        
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sine-sine_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "2":

                y = SineWave() - CosineWave()

                fig, ax = plt.subplots()
                ax.set_title("Sine & Cosine destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sine-cosine_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "3":

                y = SineWave() - Square()

                fig, ax = plt.subplots()
                ax.set_title("Sine & Square destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sine-square_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "4":

                y = SineWave() - Sawtooth()

                fig, ax = plt.subplots()
                ax.set_title("Sine & Sawtooth destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sine-sawtooth_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "5":

                y = CosineWave() - CosineWave()

                fig, ax = plt.subplots()
                ax.set_title("Cosine & Cosine destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("cosine-cosine_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "6":

                y = CosineWave() - Square()

                fig, ax = plt.subplots()
                ax.set_title("Cosine & Square destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("cosine-square_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "7":

                y = CosineWave() - Sawtooth()

                fig, ax = plt.subplots()
                ax.set_title("Cosine & Sawtooth destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("cosine-sawtooth_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "8":

                y = Square() - Square()

                fig, ax = plt.subplots()
                ax.set_title("Square & Square destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("square-square_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "9":

                y = Square() - Sawtooth()

                fig, ax = plt.subplots()
                ax.set_title("Square & Sawtooth destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("square-sawtooth_dest_int.mp4")
                plt.show()
                break

            if user_Choice3 == "10":

                y = Sawtooth() - Sawtooth()

                fig, ax = plt.subplots()
                ax.set_title("Sawtooth & Sawtooth destructive interference")
                ax.set_xlabel("Time")
                ax.set_ylabel("Amplitude")
                ax.set_xlim(min(t), max(t))
                ax.set_ylim(2*min(y), 2*max(y))
                ax.grid(True)
                            
                point, = ax.plot([], [], 'o')
                line, = ax.plot([], [], '-')

                def init():
                    point.set_data([], [])
                    line.set_data([], [])
                    return point, line
                            
                def update(i):
                    point.set_data([t[i]], [y[i]])
                    line.set_data(t[:i], y[:i])
                    return point, line
                            
                anim = FuncAnimation(fig, update, frames = len(t), init_func = init)
                anim.save("sawtooth-sawtooth_dest_int.mp4")
                plt.show()
                break

    if choice == "6":
        print("Thanks for using the program !!")
        break