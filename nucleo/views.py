from django.shortcuts import render


def kit_ssh(request):
	"""Renderiza la plantilla del Kit Educativo de SSH.

	Opcionalmente se pueden pasar variables de contexto para rellenar los
	placeholders en la plantilla (nombre de la infografía y enlaces).
	"""
	context = {
		# Cambia estos valores o rellena desde base de datos si lo deseas
		'inf_img_filename': 'infografia_ssh.png',  # PLACEHOLDER: nombre del archivo en static/img
		# Guía técnica subida a Google Drive: se puede usar un enlace de descarga directo
		# ID extraído del enlace que proporcionaste: 1XDyjtHqH0RlN9hecQsfncBxv_oxOQlUE
		# Enlace directo de descarga (Drive): https://drive.google.com/uc?export=download&id=<FILE_ID>
		'link_guia_pdf': 'https://drive.google.com/uc?export=download&id=1XDyjtHqH0RlN9hecQsfncBxv_oxOQlUE',
		# Presentación: si la subes a Google Drive / Google Slides proporciona el ID
		# y aquí puedes usar la URL de vista previa: https://docs.google.com/presentation/d/<FILE_ID>/preview
		# Usando el ID que proporcionaste: 1xrXEY4SHJe6zTd8VLGF8RuvwDr2K4pZ9
		'link_presentacion_slides': 'https://docs.google.com/presentation/d/1xrXEY4SHJe6zTd8VLGF8RuvwDr2K4pZ9/preview',
		# Video de YouTube: extraer ID del enlace y usar en URL embed
		# Link: https://www.youtube.com/watch?v=R2PzogOGavs → ID: R2PzogOGavs
		'url_video_embed': 'https://www.youtube.com/embed/R2PzogOGavs?rel=0',
		'autores': ['Perla, Miguel, Hannah, Fernanda, Mario y Darely'],
	}
	return render(request, 'kit_ssh.html', context)
