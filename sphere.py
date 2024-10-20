
import math



def sphere_diameter(radius):
    return 2 * radius

def sphere_circumference(radius):
    return 2 * math.pi * radius

def sphere_surface_area(radius):
    return 4 * math.pi * (radius ** 2)

def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

if __name__ == "__main__":

    radius = float(input("Enter the radius of the sphere: "))
    

    diameter = sphere_diameter(radius)
    circumference = sphere_circumference(radius)
    surface_area = sphere_surface_area(radius)
    volume = sphere_volume(radius)
    

    print(f"Diameter of the sphere: {diameter}")
    print(f"Circumference of the sphere: {circumference}")
    print(f"Surface area of the sphere: {surface_area}")
    print(f"Volume of the sphere: {volume}")
