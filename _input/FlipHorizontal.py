import subprocess

video_file = 'input.mp4'  # Cambia 'video.mp4' por el nombre de tu archivo de video
output_file = 'FlipHorizontal.mp4'  # Cambia 'video_girado.mp4' por el nombre que quieras para el archivo girado

# Comando de FFMPEG para girar el video 180 grados
ffmpeg_command = ['ffmpeg', '-i', video_file, '-vf', 'transpose=2,transpose=2', '-c:a', 'copy', output_file]

# Ejecutar el comando con subprocess
subprocess.run(ffmpeg_command)


