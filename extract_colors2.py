from PIL import Image, ImageDraw
from datetime import datetime

def apply_center_gradient_mark_line_and_log(image_path, log_interval=100):
    image = Image.open(image_path)
    width, height = image.size

    # 中央のX座標を計算
    center_x = width // 2

    # グラデーションと参照線を描画するための画像のコピーを作成
    gradient_image = image.copy()
    line_image = image.copy()
    draw_gradient = ImageDraw.Draw(gradient_image)
    draw_line = ImageDraw.Draw(line_image)

    for y in range(height):
        ratio = y / height
        gradient_color = tuple(int(image.getpixel((center_x, y))[i] + (image.getpixel((center_x, height - 1))[i] - image.getpixel((center_x, y))[i]) * ratio) for i in range(3))

        # 指定した間隔ごとにターミナルに色情報を出力
        if y % log_interval == 0:
            print(f"Pixel at ({center_x}, {y}): {gradient_color}")

        draw_gradient.line([(0, y), (width - 1, y)], fill=gradient_color)

    # 中央上部から下部にかけての参照線を描画
    draw_line.line([(center_x, 0), (center_x, height - 1)], fill='red', width=3)

    # 現在の日時をファイル名に追加
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 画像を保存
    line_image_path = f'center_line_marked_image_{current_time}.jpg'
    gradient_image_path = f'center_gradient_filled_image_{current_time}.jpg'
    
    line_image.save(line_image_path)
    gradient_image.save(gradient_image_path)

    print(f"Center line marked image saved as {line_image_path}")
    print(f"Center gradient filled image saved as {gradient_image_path}")

# 使用例
image_path = 'image/5.jpg'
log_interval = 100  # 100ピクセルごとに色情報をログに出力

apply_center_gradient_mark_line_and_log(image_path, log_interval)

# python3 extract_colors2.pyで実行します

