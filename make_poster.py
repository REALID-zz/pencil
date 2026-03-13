from PIL import Image, ImageEnhance
import os

img = Image.open('assets/hero-portrait.png')
w, h = img.size
print(f'Original: {w}x{h}')

# Red box area: head to shoulders, roughly top 10% to 55% of height, with some side margin
top = int(h * 0.08)
bottom = int(h * 0.52)
left = int(w * 0.05)
right = int(w * 0.95)

crop = img.crop((left, top, right, bottom))
print(f'Cropped: {crop.size[0]}x{crop.size[1]}')

scale = 3
final = crop.resize((crop.size[0] * scale, crop.size[1] * scale), Image.LANCZOS)
final = ImageEnhance.Sharpness(final).enhance(1.3)
final.save('assets/video-poster.jpg', 'JPEG', quality=92)

sz = os.path.getsize('assets/video-poster.jpg') // 1024
print(f'Final: {final.size[0]}x{final.size[1]}, {sz}KB')
