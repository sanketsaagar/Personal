#Q5. Read the contents of image in list


# Python program to read
# image using PIL module


from PIL import Image


img = Image.open('Sample.jpeg', 'r')
width,height=img.size

pixel_value = list(img.getdata())
for i in pixel_value:

    print(i)

