from PIL import Image

input_image_path = input("Inserisci il percorso dell'immagine di input: ")
output_image_path = input("Inserisci il percorso dove salvare l'immagine: ")

def convertImage():


	img = Image.open(input_image_path)
	img = img.convert("RGBA")

	datas = img.getdata()

	newData = []

	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2] == 255:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

	img.putdata(newData)
	img.save(output_image_path , "PNG")
	print("Salvato con successo")

convertImage()
