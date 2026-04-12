from PIL import Image
import os

images = ['symbol-arc-flash.png', 'symbol-electrocution.png', 'symbol-hand-shock.png']
asset_dir = '/home/jgrah/Blog_EI_Safety/ai-in-mining-blog/src/assets/'

for img_name in images:
    path = os.path.join(asset_dir, img_name)
    try:
        img = Image.open(path).convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Change white backgrounds to transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(path, "PNG")
        print(f"Successfully processed {img_name}")
    except Exception as e:
        print(f"Failed {img_name}: {e}")
