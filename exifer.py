import sys
from PIL import Image
from PIL.ExifTags import TAGS

if len(sys.argv) != 2:
    print("usage: exifer /path/to/image")
else:
    imagename = sys.argv[1]
    image = Image.open(imagename)
    exifdata = image._getexif()
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode("utf-8", "ignore")
        print(f"{tag:25}: {data}")
