from PIL import Image, ImageEnhance
import os

img = Image.open('assets/hero-portrait.png')
print(f'Original: {img.size[0]}x{img.size[1]}')

w, h = img.size
new_w, new_h = w * 3, h * 3
img2 = img.resize((new_w, new_h), Image.LANCZOS)

img2 = ImageEnhance.Sharpness(img2).enhance(1.3)

img2.save('assets/hero-portrait-hd.png')
sz = os.path.getsize('assets/hero-portrait-hd.png') // 1024
print(f'Upscaled: {new_w}x{new_h}, {sz}KB')
