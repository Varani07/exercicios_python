file_name = "my_first_file.txt"

with open(file_name, "w") as file_obj:
    file_obj.write("Hello File, new text!\n")
    file_obj.write("Youre my favorite file.\n")