
def cube_surface_area(edge_length):

    return 6 * (edge_length ** 2)

if __name__ == "__main__":
  
    edge_length = int(input("Enter the length of the edge of the cube: "))
    

    surface_area = cube_surface_area(edge_length)
    

    print(f"The surface area of the cube is: {surface_area}")
