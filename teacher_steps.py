class Navigator:
    def __init__(self):
        self.position = (0, 0)
        self.direction = 0  # 0=North, 90=East, 180=South, 270=West
    
    def turn(self, degrees, direction):
        """Turn by specified degrees (left or right)"""
        if direction.lower() == "left":
            self.direction = (self.direction - degrees) % 360
        else:  # right
            self.direction = (self.direction + degrees) % 360
        print(f"Turned {direction} {degrees} degrees. Now facing: {self.direction}°")
    
    def walk(self, steps):
        """Walk forward by specified number of steps"""
        print(f"Walked {steps} steps")
    
    def walk_until_distance(self, distance, object_name):
        s
        """Walk until reaching specified distance from an object"""
        print(f"Walked until {distance} step(s) away from {object_name}")


# Navigation sequence
navigator = Navigator()

navigator.turn(90, "left")  # Turn 90 degrees to your left
navigator.walk_until_distance(0.5, "table")  # Walk until 0.5 steps from table
navigator.turn(90, "left")  # Turn 90 degrees to your left
navigator.walk_until_distance(1, "wall")  # Walk until 1 step from wall
navigator.turn(90, "right")  # Turn 90 degrees to your right
navigator.walk_until_distance(1, "table")  # Walk until 1 step from table
navigator.turn(90, "right")  # Turn 90 degrees to your right
navigator.walk(3)  # Walk 3 steps
navigator.turn(90, "left")  # Turn 90 degrees to your left
navigator.walk(2)  # Walk 2 steps