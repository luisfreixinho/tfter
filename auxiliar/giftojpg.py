from PIL import Image, GifImagePlugin

giforiginal = Image.open("../training/graves.gif")

i = 0
for frame in range(0, giforiginal.n_frames,5):
    i+=1
    giforiginal.seek(frame)
    # giforiginal.show()
    giforiginal.convert('RGB').save("../training/graves"+str(i)+".jpg")
