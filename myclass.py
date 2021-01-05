from enum import IntFlag


class LightState(IntFlag):
    On = 0
    Off = 1


class WheelState(IntFlag):
    Normal = 0
    Chain = 1


class Light:
    def __init__(self, number):
        self.number = number
        self.state = LightState(1)

    def __repr__(self):
        return f"Light[number: {self.number}, state: {self.state}]"

    def switch(self):
        if self.state is LightState.Off:
            self.state = LightState(0)
        else:
            self.state = LightState(1)

class Wheel:
    def __init__(self, number):
        self.number = number
        self.state = WheelState(0)

    def __repr__(self):
        return f"Wheel[number: {self.number}, state: {self.state}]"

    def change_wheel(self):
        if self.state is WheelState.Normal:
            self.state = WheelState(1)
        else:
            self.state = WheelState(0)


class Car:
    def __init__(self):
        self.front_light = Light(2)
        self.back_light = Light(2)
        self.wheel = Wheel(4)

    def __repr__(self):
        return f"Car[{self.front_light}, {self.back_light}, {self.wheel}]"


class Bicycle:
    def __init__(self):
        self.light = Light(1)
        self.wheel = Wheel(2)

    def __repr__(self):
        return f"Bicycle[{self.light}, {self.wheel}]"
