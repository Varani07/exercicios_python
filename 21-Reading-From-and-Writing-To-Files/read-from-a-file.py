# cupcakes_file = open("cupcakes.txt", "r")
# cupcakes_file.close()

# with open("cupcakes.txt", "r") as cupcakes_file:
#     print("The file has been opened!")
#     content = cupcakes_file.read()
#     print(content)

# print("The file has been closed. We are outside the context block!")

file_name = input("Qual arquivo deseja abrir? ")
with open(file_name, "r") as file_object:
    print(file_object.read())

# FileNotFoundError