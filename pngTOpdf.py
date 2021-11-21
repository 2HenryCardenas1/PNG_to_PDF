from PIL import Image

#Ejecutar como admin
#Installar la libreria Pillow :  pip install Pillow
#Autor: Henry Esteban Cardenas Aleman (H3C4)

if __name__ == '__main__' :
    try :
        file = input('Escriba el nombre del archivo: ')
        route = input('Escriba la ruta donde se encuentra el archivo: ') #Ejemplo: C:\User\Name_user\Directory\
        route_new = input('Escriba la ruta donde quiere que se guarde el archivo: ')
        image = Image.open(fr'{route}\{file}.png')
        pdf = image.convert('RGB')
        pdf.save(fr'{route_new}\{file}.pdf')
        print('\n'+fr'[!] El archivo pdf guardado en la ruta: {route_new}\{file}')
    except :
     print('\n\t[x] Algo salio mal, escriba la ruta correcta y el nombre del archivo sin extencion')
