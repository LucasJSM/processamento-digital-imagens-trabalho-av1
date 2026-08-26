import cv2 as cv
import sys

def show_image(img_path):
    img = cv.imread(img_path)

    if img is None:
        print(f"Erro: não foi possível carregar a imagem '{img_path}'")
        sys.exit();

    tamanho = (404, 599)

    img = cv.resize(img, tamanho)

    cv.namedWindow("Questao 1")
    cv.moveWindow("Questao 1", 100, 50)
    cv.imshow("Questao 1", img)
    
    cv.waitKey()

    cv.destroyAllWindows()


def main():
    img_path = "./images/spiderman.jpg"
    show_image(img_path)

if __name__ == "__main__":
    main()