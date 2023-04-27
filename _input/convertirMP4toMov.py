import subprocess

input_file = 'input.mp4' # Cambia 'video.mp4' por el nombre de tu archivo de entrada
output_file = 'video_convertido.mov' # Cambia 'video.mov' por el nombre de tu archivo de salida

ffmpeg_command = ['ffmpeg', '-i', input_file, '-c:v', 'copy', '-c:a', 'copy', output_file]

subprocess.run(ffmpeg_command)

