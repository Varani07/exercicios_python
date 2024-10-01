# mad_libs = "{} laughed at the {} {}."

# print(mad_libs.format("Matheus", "green", "alien"))
# print(mad_libs.format("Matheus", "green", "alien", "Random"))
# # print(mad_libs.format("Boris", "silly")) IndexError

# mad_libs = "{2} laughed at the {1} {0}."

# print(mad_libs.format("Matheus", "green", "alien"))
# print(mad_libs.format("Matheus", "green", "alien", "Random"))

mad_libs = "{name} laughed at the {adjective} {noun}."

# print(mad_libs.format(name = "Matheus", adjective = "green", noun = "alien"))

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(mad_libs.format(name = name, adjective = adjective, noun = noun))