import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('sample2.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hImg, wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
print(pytesseract.image_to_string(img))
for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg- y), (w,hImg- h), (50, 50, 255), 2)
    cv2.putText(img,b[0],(x,hImg- y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
cv2.imshow('img', img)
cv2.waitKey(0)


'''
sample_text = 'Wake up with determination. Go to bed with satisfaction.'
l1 = list(sample_text.split(' '))
print(l1)
x = input()
l2 = list(x.split(' '))
print(l2)
c = 0
for i in range(len(l1)):
    if l1[i] == l2[i]:
        c += 1
print(f'Accuracy = {round(((c/len(l1))*100))}%')
'''

