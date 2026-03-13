from PIL import Image, ImageEnhance, ImageFilter
import os

img = Image.open('assets/hero-portrait.png')
w, h = img.size
print(f'Original: {w}x{h}')

# Video is 640x480 (4:3). Crop portrait to 4:3 centered on face.
target_ratio = 4 / 3  # width / height

# The face center is roughly at 30% from top
face_center_y = int(h * 0.30)
face_center_x = w // 2

# Try to use full width, calculate height from ratio
crop_w = w
crop_h = int(crop_w / target_ratio)

if crop_h > h:
    crop_h = h
    crop_w = int(crop_h * target_ratio)

# Center crop on face
top = face_center_y - crop_h // 2
if top < 0:
    top = 0
bottom = top + crop_h
if bottom > h:
    bottom = h
    top = bottom - crop_h

left = face_center_x - crop_w // 2
if left < 0:
    left = 0
right = left + crop_w
if right > w:
    right = w
    left = right - crop_w

crop = img.crop((left, top, right, bottom))
print(f'Cropped: {crop.size[0]}x{crop.size[1]}')

# Scale to exactly 640x480
final = crop.resize((640, 480), Image.LANCZOS)
final = ImageEnhance.Sharpness(final).enhance(1.3)
final.save('assets/video-poster.jpg', 'JPEG', quality=95)

sz = os.path.getsize('assets/video-poster.jpg') // 1024
print(f'Final: {final.size[0]}x{final.size[1]}, {sz}KB')
