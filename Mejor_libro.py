# Modulos necesarios
import bs4
import requests
# Abrir la página para web de la librería
url = "https://www.cuspide.com/"
pagina = requests.get(url)

# Pasar formato
sopa = bs4.BeautifulSoup(pagina.content, 'lxml')

# Buscar el libro mas vendido del mes en la página
imagen = sopa.select('.lazy')[0]['data-original']
titulo = sopa.select('.lazy')[0]['title']
print(f'El libro mas vendido del momento es {titulo}')

# Guardar portada del libro y transformar a JPG
libro_mas_vendido = requests.get(imagen)
crear_img = (open('libro_mas_vendido.jpg', 'wb'))
crear_img.write(libro_mas_vendido.content)
crear_img.close()
