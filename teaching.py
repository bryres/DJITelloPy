from djitellopy import Tello

def flybox(tello):
    #
    # Write your program to fly in a box here.
    #


def main():
    tello = Tello()
    tello.set_speed(50)

    try:
        flybox(tello)

    except Exception as e:
        print(e)
        tello.emergency_land()

if __name__ == '__main__':
    main()
