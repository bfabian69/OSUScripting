

def calculate_momentum(mass, velocity):
   
    return mass * velocity

if __name__ == "__main__":
   
    mass = float(input("Enter the mass of the object in kilograms: "))
    velocity = float(input("Enter the velocity of the object in meters per second: "))
    
    momentum = calculate_momentum(mass, velocity)
    
    print(f"The momentum of the object is: {momentum} kg·m/s")
