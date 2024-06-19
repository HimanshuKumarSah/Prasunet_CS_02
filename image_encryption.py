print("This program will encrypt your file and will replace the original file with the encrypted one.")
print("Please make sure that the file is in the same folder as this program.")
print("The same key is used for encryption and decryption of the file.")
print("Enter the name of your file")

#Taking the image name as the input.
path = input("Name: ")

#Taking the key as input
key = input("Enter your key value here: ")

print("Encrypting/Decryptiong the file...")

#Opening the image file.
file = open(path, "rb")
#Reading the image file and storing it in the variable named image.
image = file.read()
#Closing the image file.
file.close()
#Converting the image to bytearray.
image = bytearray(image)
#Performing XOR operation to all the bytes in the image variable.
for i,j in enumerate(image):
    image[i] = j^int(key)
#Opening the image file again, this time with write permissions.
file = open(path, "wb")
#Writing the encrypted image to the file.
file.write(image)
#Closing the file.
file.close()

print("Saving the file...")
