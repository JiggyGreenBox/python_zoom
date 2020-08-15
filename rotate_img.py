from PIL import Image, ImageTk



def rotate_img(img_path, rt_degr):
	img = Image.open(img_path)
	return img.rotate(rt_degr, expand=1)

image = '500_90.png'

img_rt_90 = rotate_img(image, 90)
img_rt_90.save(image)