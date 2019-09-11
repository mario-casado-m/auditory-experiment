import os, random, shutil, time, winsound
# librerias locales
import functions.maximizeConsole as maximizeConsole
import functions.resizer as resizer

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def error():
	print("\n\n{}".format(center_text("El valor introducido no es adecuado.")))
	time.sleep(3)

def windowFormat():
	columns, _ = shutil.get_terminal_size()
	maximizeConsole.maximize_console()
	return columns

def center_text(text):
	if type(text).__name__ == "str":
		text = text.center(shutil.get_terminal_size().columns, " ")
		return text
	if type(text).__name__ == "list":
		textList = list()
		for i in text:
			text = i.center(shutil.get_terminal_size().columns, " ")
			textList.append(text)
		return textList

def warning():
	next_step = None
	while next_step != "":
		clear()
		text = center_text(["Colócate los auriculares",	"y pulsa ENTER cuando estés listo para comenzar."])
		next_step = input("\n\n{}\n{}".format(text[0], text[1]))

def sociology():
	# sexo
	gender = input("\n\nTeclea el número que corresponda a tu sexo y pulsa ENTER.\n\n1 Mujer\n2 Hombre\n3 Otro\n>>> ")
	while gender not in ["1", "2", "3"] or gender.isdigit == False:
		gender = input("\n\nEl dato introducido no es adecuado.\nTeclea el número que corresponda a tu sexo y pulsa ENTER.\n\n1 Mujer\n2 Hombre\n3 Otro\n>>> ")
	if gender == "1":
		gender = "mujer"
	elif gender == "2":
		gender = "hombre"
	elif gender == "3":
		gender = "otro"
	
	# edad
	age = input("\n\nIntroduce tu edad en dígitos y pulsa ENTER.\n\n>>> ")
	while age.isdigit() == False or int(age) not in range(18,60):
		age = input("\n\nEl formato utilizado no es correcto.\nPor favor, introduce tu edad en dígitos y pulsa ENTER.\n\n>>> ")
	
	# origen
	origin = input("\n\nIntroduce de dónde eres (ciudad, país) y pulsa ENTER.\n\n>>> ")
	
	# estudios
	clear()
	studies = input("\n\nIntroduce el número que corresponde\na tu área de especialidad\ny pulsa ENTER.\n\n\n\n1 Traducción, interpretación, filologías\n2 Ingeniería y tecnología\n3 Otros campos de estudios universitarios\n4 Sin estudios universitarios\n>>>  ")
	while studies not in ["1", "2", "3", "4"] or studies.isdigit == False:
		clear()
		studies = input("\n\nEl dato introducido no es adecuado.\nIntroduce el número que corresponde al grado máximo de estudios que has completado y pulsa ENTER.\n\n\n\n1 Traducción, interpretación, filologías\n2 Ingeniería y tecnología\n3 Otros campos de estudios universitarios\n4 Sin estudios universitarios\n>>>  ")
	
	output = outputGen(gender, age, origin, studies)
	return output

def outputGen(gender, age, origin, studies):
	code = str(random.randint(100000000, 300000000))
	date = time.strftime("%Y-%m-%d")
	os.mkdir(code)
	usuario = open("{}/usario_{}.txt".format(code, code), "w", encoding="utf-8")
	usuario.write("id: {}\ngender: {}\nage: {}\norigin: {}\nstudies: {}".format(code, gender, age, origin, studies))
	output = open("{}/test_perceptivo_TTS_{}_{}.csv".format(code, code, date), "w", encoding="utf-8")
	output.write("sample;round;transcript;response\n")
	return output

def levelsGen():
	levels = ["1 La frase me resulta totalmente incomprensible.",
	"2 Poco natural",
	"3 Aceptable",
	"4 Natural",
	"5 Muy natural"]
	return levels

def intro():
	clear()
	levels = levelsGen()
	text = center_text(["A continuación, vas a escuchar unos estímulos.", "Deberás juzgar su naturalidad en una escala del 1 al {}".format(len(levels)), "en la que 1 significa muy poco natural y {} muy natural.".format(len(levels)), "No te preocupes. Tendrás todas las indicaciones necesarias", "en cada uno de los pasos.", "Podrás escuchar cada muestra un máximo de dos veces."])
	print("\n\n", "{}".format('\n'.join(str(line) for line in text)), "\n\n")
	trigger = input("Pulsa ENTER cuando estés listo para comenzar".center(shutil.get_terminal_size().columns, " "))
	return trigger

def audio_csv_read(path):
	sounds = list()
	for root, _ , item in os.walk(path):
		for file in item:
			if file.endswith(".tsv"):
				route = os.path.join(root, file)	
				database = open(route, 'r', encoding='utf-8')
				for entry in database:
					audio = entry.rstrip('\n').split('\t')[0] + '.wav'
					route = os.path.join(root, audio)
					transcription = entry.rstrip('\n').split('\t')[1]
					sounds.append((route, transcription))
					sounds.append((route, transcription))
	return sounds

def inquiry(sound, transcription, listenTime):
	print("\n\n\n\n", "Escucha".center(shutil.get_terminal_size().columns, " "))
	time.sleep(2)
	winsound.PlaySound(sound, winsound.SND_ASYNC)
	listenTime += 1
	time.sleep(2)
	clear()
	levels = levelsGen()
	if listenTime < 2:
		text = center_text(["Has escuchado la frase", "{}".format(transcription), "En una escala del 1 al {},".format(len(levels)), "¿Cómo de natural te ha sonado lo que acabas de escuchar?", "Teclea el número y pulsa ENTER.", "0 Volver a escuchar"])
	elif listenTime == 2:
		text = center_text(["Has escuchado la frase", "{}".format(transcription), "En una escala del 1 al {},".format(len(levels)), "¿Cómo de natural te ha sonado lo que acabas de escuchar?", "Teclea el número y pulsa ENTER."])
	text[5:5] = center_text([level for level in levels])
	print("\n\n", "{}{}\n{}{}{}".format(text[0], text[1], text[2], text[3], text[4]), "\n\n", "{}".format('\n\n'.join(str(line) for line in text[5:len(text)])))
	response = input("\n\n>>> ")
	if listenTime < 2:
		while response not in ["0", "1", "2", "3", "4", "5"] or response.isdigit == False:
			clear()
			error()
			clear()
			print("\n\n", "{}{}\n{}{}{}".format(text[0], text[1], text[2], text[3], text[4]), "\n\n", "{}".format('\n\n'.join(str(line) for line in text[5:len(text)])))
			response = input("\n\n>>> ")
	elif listenTime == 2:
		while response not in ["1", "2", "3", "4", "5"] or response.isdigit == False:
			clear()
			error()
			clear()
			print("\n\n", "{}{}\n{}{}{}".format(text[0], text[1], text[2], text[3], text[4]), "\n\n", "{}".format('\n\n'.join(str(line) for line in text[5:len(text)])))
			response = input("\n\n>>> ")
	return response, listenTime

def memory(list, entry):
	if entry in list:
		return "2"
	else:
		list.append(entry)
		return "1"

if __name__ == "__main__":
	resizer.font_size()
	columns = windowFormat()
	warning()
	clear()
	output = sociology()
	clear()
	trigger = intro()    
	while trigger != "":
		trigger = intro()
	clear()
	time.sleep(2)
	buffer = list()
	path = ".\\samples"
	sounds = audio_csv_read(path)
	for i in range(len(sounds)):
		entry = random.choice(sounds)
		listenTime = 0
		roundtime = memory(buffer, entry)
		sound, transcription = entry[0], entry[1]
		response, listenTime = inquiry(sound, transcription, listenTime)
		while response == "0":
			clear()
			response, listenTime = inquiry(sound, transcription, listenTime)
		output.write("{};{};{};{}\n".format(sound.split('\\')[-1].split('.wav')[0], roundtime, transcription, response))
		del sounds[sounds.index(entry)]
		clear()
		time.sleep(2)
	text = center_text(["El experimento ha terminado.", "Muchas gracias por participar", "No olvides enviar la carpeta generada a una de las siguientes direcciones.", "Anota la dirección antes de cerrar el experimento", "email@domain.scope"])
	print("\n\n", "{}".format('\n'.join(str(line) for line in text)))
	input("\n\n{}".format(center_text("Pulsa cualquier tecla para salir")))
