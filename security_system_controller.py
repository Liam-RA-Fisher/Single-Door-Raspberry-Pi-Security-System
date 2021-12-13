import threading
import door_monitor

if __name__ == "__main__":
    t1 = threading.Thread(target = door_monitor.door_sense)
    t1.start()
    door_monitor.power()
