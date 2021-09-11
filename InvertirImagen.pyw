#########################################
#
#programa que invierte los bits de color en una imagen
#
#########################################

# Importacion de modulos o paquetes
from OpenGL.GL.images import ImageInputConverter
from graphics import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def openGraphicsWindow(title, whidth, height, image):

 # Configuracion de la ventana
    win = GraphWin(title,whidth,height)
    win.setBackground(color_rgb(55, 54, 53))

 # Centrar la imagen en la ventana creada
    image.move(whidth / 2, height / 2)
    image.draw(win)
    return win

 # Abrir carpeta
def openFile():
    inFileName = askopenfilename()  
    inFile = open(inFileName, "h" )
    return inFile

def openImage():

 # Archivo png o gif
    inFileName = askopenfilename()

 # Centrar la imagen basado en su tamaño
    image = Image (Point(0,0), inFileName)
    return image

 # creacion del boton invertir color de imagen
def createButton(win):
    button = Rectangle(Point(1, 1), Point(250,40))  
    button.setOutline(color_rgb(244, 188, 15))
    button.setFill(color_rgb(119, 94, 57))
    button.draw(win)
    buttonText = Text(button.getCenter(), 'Invertir Color GIF')
    buttonText.setTextColor(color_rgb(0, 0, 1))
    buttonText.draw(win)
    return button, buttonText

 # Metodo para hacer la invercion de color en la imagen
def invertirColor(win, image, width, height):
    for y in range (height):
         for x in range (width):
             r, g , b = image.getPixel (x, y)
             image.setPixel(x, y, color_rgb(255-r, 255-g, 255-b))
         image.undraw()
         image.draw(win)

# Abre el explorador para ponerle nombre a la imagen png
def saveFile(image):
    saveFileName = asksaveasfilename ()
    if saveFileName !="":
         image.save(saveFile) 

def main ():

 # Muestra la imagen en la ventana
    image = openImage()

 # Creacion de ventana
    width = image.getWidth()
    height = image.getHeight()
    win = openGraphicsWindow ('color Inverso GIF', width, height, image)

 # Representacion del boton invertir
    button, buttonText = createButton(win)
    win.getMouse()
    invertirColor(win, image, width, height)
     
 # Ejecucion final para guardar la imagen invertida  
    saveFile(image)

 # Pausa para dar click al botón y salir
    button.undraw()
    buttonText.undraw()

 # Creacion del botón salir 
    buttonText.setText('Click para salir')
    button.draw(win)
    buttonText.draw()
    win.getMouse()

main()