import subprocess

def apply_blur_filter(input_file, output_file, radius=10, sigma=3):
    # Define el comando de FFMPEG para aplicar el filtro de desenfoque
    ffmpeg_command = ['ffmpeg', '-i', input_file, '-vf', f'boxblur={radius}:{sigma}', '-c:a', 'copy', output_file]

    # Ejecuta el comando de FFMPEG con subprocess
    subprocess.run(ffmpeg_command)

# Ejemplo de uso
input_file = 'input.mp4'
output_file = 'video_desenfocado.mp4'
apply_blur_filter(input_file, output_file, radius=20, sigma=5)

