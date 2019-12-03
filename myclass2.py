from abc import ABCMeta, abstractmethod


class DeviceInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def play(self): pass

    @abstractmethod
    def stop(self): pass


class CDPlayer:

    def __init__(self, cd=None):
        self.cd = cd

    def play(self):
        if self.cd is None:
            print("Couldn't play. CDPlayer is empty.")
        else:
            print(f"CD: {self.cd}")

    def stop(self):
        if self.cd is None:
            print("Please set CD.")
        else:
            print("CDPlayer Stopped.")


class DVDPlayer:

    def __init__(self, dvd=None):
        self.dvd = dvd

    def play(self):
        if self.dvd is None:
            print("Couldn't play. DVDPlayer is empty.")
        else:
            print(f"DVD: {self.dvd}")

    def stop(self):
        if self.dvd is None:
            print("Please set DVD.")
        else:
            print("DVDPlayer Stopped.")


DeviceInterface.register(CDPlayer)
DeviceInterface.register(DVDPlayer)


if __name__ == '__main__':
    cd = CDPlayer("Buena Vista Social Club")
    dvd = DVDPlayer("Forest Gump")
    none_cd = CDPlayer()
    none_dvd = DVDPlayer()
    
    cd.play()
    dvd.play()
    none_cd.play()
    none_dvd.play()

    cd.stop()
    dvd.stop()
    none_cd.stop()
    none_dvd.stop()
