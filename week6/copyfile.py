

def copy_file(source_file, destination_file):
    try:
        
        with open(source_file, 'r') as source:
            content = source.read()
              
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        print(f"Content successfully copied from {source_file} to {destination_file}.")
    
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

copy_file(source_file, destination_file)
