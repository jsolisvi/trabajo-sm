import subprocess

video_file = 'input.mp4'  # Cambia 'video.mp4' por el nombre de tu archivo de video
output_file = 'FlipVertical.mp4'  # Cambia 'video_volteado.mp4' por el nombre que quieras para el archivo volteado

# Comando de FFMPEG para voltear el video
ffmpeg_command = ['ffmpeg', '-i', video_file, '-vf', 'transpose=2', '-c:a', 'copy', output_file]

# Ejecutar el comando con subprocess
subprocess.run(ffmpeg_command)


