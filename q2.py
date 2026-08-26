import cv2 as cv

def show_images(img_path):
    img = cv.imread(img_path)

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.namedWindow('Imagem Original')
    cv.moveWindow('Imagem Original', 100, 50)
    cv.imshow('Imagem Original', img)

    cv.namedWindow('Imagem em Escala Cinza')
    cv.moveWindow('Imagem em Escala Cinza', 700, 50)
    cv.imshow('Imagem em Escala Cinza', img_gray)

    cv.waitKey()
    cv.destroyAllWindows()


def main():
    img_path = './images/Lena.jpg'
    show_images(img_path)


if __name__ == "__main__":
    main() 