import os

from PIL import Image

def thumbnail(infile, size=(128, 128)):
    outfile = os.path.splitext(
        infile)[0] + ".thumbnail"
    print("====>>>   ", outfile)
    # C:\Windows\Web\Screen\img102.thumbnail
    try:
        im = Image.open(infile)
        print(im)
        print("====>", im.thumbnail(size))
        print("=======>",im.save(outfile, "JPEG"))
    except IOError:
        print("cannot create thumbnail for", infile)


if __name__ == "__main__":
    thumbnail(r"C:\workspace\한교동2.jpg",(256,256))           