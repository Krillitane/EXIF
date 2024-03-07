from exif import Image
with open('images/four.jpg', 'rb') as image_file:
    my_image = Image(image_file)

#print(my_image.has_exif)

tags_present = dir(my_image)

print(tags_present)

 
#print(my_image.make)

#print(my_image.model)

#print(my_image.gps_latitude)
