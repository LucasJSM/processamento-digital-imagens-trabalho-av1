import cv2 as cv
import sys

'''
Script to split the RGB channels of an image and save them as separate images.
'''

def split_rgb_channels(img_path):
	img = cv.imread(img_path)

	if img is None:
		print(f"Erro: não foi possível carregar a imagem '{img_path}'")
		sys.exit()

	b, g, r = cv.split(img)

	cv.imwrite('./images/spiderman_blue.jpg', b)
	cv.imwrite('./images/spiderman_red.jpg', r)
	cv.imwrite('./images/spiderman_green.jpg', g)

	print('Canais RGB separados e salvos com sucesso!')


def main():
	img_path = './images/spiderman.jpg'
	split_rgb_channels(img_path)


if __name__ == '__main__':
	main()
