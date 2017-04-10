import Image,ImageFilter
im=Image.open('C:\Users\Administrator\Desktop\IMG_5076 (1).JPG')
im2=im.filter(ImageFilter.BLUR)
im2.save('C:\Users\Administrator\Desktop\IMG_5076 (1)blur.JPG','jpeg')
