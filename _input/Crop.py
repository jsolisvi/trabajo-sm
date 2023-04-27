import subprocess

def crop_video(input_file, output_file, x, y, width, height):
    # Define el comando de FFMPEG
    command = [
        "ffmpeg",
        "-i", input_file,
        "-filter:v", f"crop={width}:{height}:{x}:{y}",
        "-c:a", "copy",
        output_file
    ]

    # Ejecuta el comando de FFMPEG
    subprocess.run(command)


