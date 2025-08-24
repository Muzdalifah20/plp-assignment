def read_file(file_name):
        
    try:
        with open(file_name , "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return (f"Sorry, '{file_name}' file, does not exists!")
    except IOError:
        return (f"Sorry, '{file_name}' file, can not be read!")
     
        
    
def write_file(file_name, user_input):
    try:
        with open( file_name, "w") as file:
            file.write(user_input)
        return f"Modified content has been written to '{file_name}' file."
    except IOError:
        return f"Error writing to the file '{file_name}'."

print("Welcome to My Note book...")
print("Enter 1 to Read a file / 2 to Write a modified file")

user_number = input("Please Enter '1' for Reading / '2' for Writing? ")

if int(user_number) == 1:
    user_file = input("Please enter the file name you want to read: ").strip()
    read_file(user_file)
elif  int(user_number) == 2: 
    user_file = input("Please enter the file name you want to read and modify: ").strip()
    
    original_content = read_file(user_file)
    modified_content = original_content.title()

    new_file = input("Please enter the new file name to save the modified content: ").strip()
    write_file(new_file, modified_content)

else:
    print("Invalid input! Please enter either '1' or '2'.")