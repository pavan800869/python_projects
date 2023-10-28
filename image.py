from PIL import Image
pic = Image.open('kimetsu-no-yaiba-tanjiro-kamado-and-kyojuro-rengoku-flames-katana-uhd-4k-wallpaper.jpg')
# pic.rotate(45).show()
# You have to rotate the pic and used the show command immediately.
#pic.show()
print("Size: "+ str(pic.size))
print("Mode: "+ str(pic.mode))