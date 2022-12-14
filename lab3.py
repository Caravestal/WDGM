r, g, b = im1.split()
print("Porównamy tryby obrazów:")
print("Tryb im_r: ", r.mode)
print("Tryb im_g: ", g.mode)
print("Tryb im_b: ", b.mode)

diff_r = ImageChops.difference(r, im_r)
diff_g = ImageChops.difference(g, im_g)
diff_b = ImageChops.difference(b, im_b)

im3 = Image.merge('RGB', (r, im_r, b))
im3.show()
im3.save("im3.jpg")
im3.save("im3.png")


diff_im2 = ImageChops.difference(im1, im3)
diff_im2.show()

image1 = Image.open("obraz1_1.jpg")
image2 = Image.open("obraz1_1.png")
image3 = Image.open("obraz1_1N.jpg")
image4 = Image.open("obraz1_1N.png")
image5 = Image.open("obraz1_2.jpg")
image6 = Image.open("obraz1_2.png")
image7 = Image.open("obraz1_2N.jpg")
image8 = Image.open("obraz1_2N.png")

diff_im3 = ImageChops.difference(image1, image2)
diff_im3.show()
diff_im4 = ImageChops.difference(image3, image4)
diff_im4.show()
diff_im5 = ImageChops.difference(image5, image6)
diff_im5.show()
diff_im6 = ImageChops.difference(image7, image8)
diff_im6.show()

plt.figure(figsize=(16, 8))
plt.subplot(1, 4, 1)
plt.imshow(diff_im3, "gray")
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(diff_im4, "gray")
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(diff_im5, "gray")
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(diff_im5, "gray")
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()image1 = Image.open("obraz1_1.jpg")
image2 = Image.open("obraz1_1.png")
image3 = Image.open("obraz1_1N.jpg")
image4 = Image.open("obraz1_1N.png")
image5 = Image.open("obraz1_2.jpg")
image6 = Image.open("obraz1_2.png")
image7 = Image.open("obraz1_2N.jpg")
image8 = Image.open("obraz1_2N.png")

diff_im3 = ImageChops.difference(image1, image2)
diff_im3.show()
diff_im4 = ImageChops.difference(image3, image4)
diff_im4.show()
diff_im5 = ImageChops.difference(image5, image6)
diff_im5.show()
diff_im6 = ImageChops.difference(image7, image8)
diff_im6.show()

plt.figure(figsize=(16, 8))
plt.subplot(1, 4, 1)
plt.imshow(diff_im3, "gray")
plt.axis('off')
plt.subplot(1, 4, 2)
plt.imshow(diff_im4, "gray")
plt.axis('off')
plt.subplot(1, 4, 3)
plt.imshow(diff_im5, "gray")
plt.axis('off')
plt.subplot(1, 4, 4)
plt.imshow(diff_im5, "gray")
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()
