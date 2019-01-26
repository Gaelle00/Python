class Car:
    def __init__(self, color, frame_material):
        self.color = color
        self.frame_material = frame_material

    def brake(self):
        print("braking!")

red_car = Car('Red', 'steel')
blue_car = Car('bleue', 'iron')

print(red_car.color)
print(red_car.frame_material)
print(blue_car.color)
print(blue_car.frame_material)

red_car.brake()
 
 