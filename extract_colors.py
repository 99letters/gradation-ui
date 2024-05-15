from PIL import Image

def extract_gradient(image_path, region, steps=10):
    image = Image.open(image_path)
    region_width = region[2]
    region_height = region[3] // steps
    colors = []

    for i in range(steps):
        sub_region = image.crop((region[0], region[1] + i * region_height, region[0] + region_width, region[1] + (i + 1) * region_height))
        sub_region_average_color = sub_region.resize((1, 1)).getpixel((0, 0))
        colors.append(sub_region_average_color)

    return colors

if __name__ == "__main__":
    image_path = 'image/5.jpg'  # 画像ファイルへのパスを更新
    region = (50, 50, 100, 100)  # 抽出する領域を更新
    colors = extract_gradient(image_path, region)
    for color in colors:
        print(color)
