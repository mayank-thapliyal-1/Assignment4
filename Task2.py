data = input("Enter text to write to the file: ")
file = open('output.txt','w')
file.write(data)
file.close()
print("Data successfully written to output.txt.")


try:
    data = input("Enter text to append: ")
    file = open('output.txt','a')
    file.write('\n')
    file.write(data)
    file.close()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Data successfully appended to output.txt.")

print("Final contents of output.txt.")
file = open('output.txt','r')
print(file.read())
file.close()

