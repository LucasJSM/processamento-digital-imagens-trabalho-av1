import cv2 as cv

img = cv.imread('./images/spiderman.jpg')

b, g, r = cv.split(img)

cv.imwrite('./images/spiderman_blue.jpg', b)
cv.imwrite('./images/spiderman_red.jpg', r)
cv.imwrite('./images/spiderman_green.jpg', g)

print('Canais RGB separados e salvos com sucesso!')
