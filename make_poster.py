import cv2, os

cap = cv2.VideoCapture('assets/studio-video.mp4')
ret, frame = cap.read()
h, w = frame.shape[:2]
print(f"Frame: {w}x{h}")
cv2.imwrite('assets/video-poster.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 95])
cap.release()
sz = os.path.getsize('assets/video-poster.jpg') // 1024
print(f"Saved: {sz}KB")
