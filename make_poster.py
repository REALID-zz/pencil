from PIL import Image, ImageEnhance
import os

img = Image.open('assets/hero-portrait.png')
w, h = img.size
print(f'Original: {w}x{h}')

target_h = int(w * 9 / 16)
top = int(h * 0.05)
bottom = top + target_h
crop = img.crop((0, top, w, bottom))
print(f'Cropped face area: {crop.size[0]}x{crop.size[1]}')

ratio = 1920 / crop.size[0]
final = crop.resize((1920, int(crop.size[1] * ratio)), Image.LANCZOS)
final = ImageEnhance.Sharpness(final).enhance(1.4)
final.save('assets/video-poster.jpg', 'JPEG', quality=92)

sz = os.path.getsize('assets/video-poster.jpg') // 1024
print(f'Final: {final.size[0]}x{final.size[1]}, {sz}KB')
