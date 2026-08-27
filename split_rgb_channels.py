import cv2 as cv
import sys

'''
Script para separar os canais RGB de uma imagem e salvar separadamente
'''

def split_rgb_channels(img_path, img_name):
	img = cv.imread(img_path)

	if img is None:
		print(f"Erro: não foi possível carregar a imagem '{img_path}'")
		sys.exit()

	b, g, r = cv.split(img)

	cv.imwrite(f'./images/{img_name}_blue.jpg', b)
	cv.imwrite(f'./images/{img_name}_red.jpg', r)
	cv.imwrite(f'./images/{img_name}_green.jpg', g)

	print('Canais RGB separados e salvos com sucesso!')

def main():
	img_name = 'spiderman'
	img_path = f'./images/{img_name}.jpg'
	split_rgb_channels(img_path, img_name)

if __name__ == '__main__':
	main()
