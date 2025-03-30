def read_modify_file():
    try:
        # Ask user for filename
        filename = input("Enter the filename to read: ")
        
        # Open the file for reading
        with open(filename, "r") as file:
            content = file.read()  # Read the file content
        
        # Modify content (convert to uppercase)
        modified_content = content.upper()
        
        # Create a new filename
        new_filename = "modified_" + filename
        
        # Write modified content to a new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content written to {new_filename} ✅")

    except FileNotFoundError:
        print("Error: The file does not exist! ‼️")
    except PermissionError:
        print("Error: You don’t have permission to read this file! 🚫")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_modify_file()





