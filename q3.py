import cv2 as cv
from matplotlib import pyplot as plt

def show_image():
    blue = cv.imread("./images/spiderman_blue.jpg", 0)
    green = cv.imread("./images/spiderman_green.jpg", 0)
    red = cv.imread("./images/spiderman_red.jpg", 0)

    # Juntando os canais
    img = cv.merge([blue, green, red])

    # Convertendo para RGB
    blue = cv.cvtColor(blue, cv.COLOR_BGR2RGB)
    green = cv.cvtColor(green, cv.COLOR_BGR2RGB)
    red = cv.cvtColor(red, cv.COLOR_BGR2RGB)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    plt.subplot(2, 2, 1)
    plt.imshow(red)
    plt.title("Canal Vermelho")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(green)
    plt.title("Canal Verde")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(blue)
    plt.title("Canal Azul")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(img)
    plt.title("Imagem Colorida")
    plt.axis("off")

    plt.show()

def main():
    show_image()

if __name__ == "__main__":
    main()