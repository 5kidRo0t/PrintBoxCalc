#!/bin/bash
# 
# ==============================================================
#   REQUISITOS PARA COMPILAR LA APP ANDROID CON BRIEFCASE
# ==============================================================
#
# Antes de ejecutar este script, asegúrate de tener instalado:
#
# 1️-Python 3.8 o superior
#    Recomendado: python3.10 o superior
#
# 2️-Briefcase
#    Instalar con: pip install briefcase
#
# 3️-Java JDK 17 o superior
#    Instalar en Debian/Ubuntu con: sudo apt install openjdk-17-jdk
#
# 4️-Android SDK
#    Briefcase lo puede descargar automáticamente
#    O instalar manualmente desde: https://developer.android.com/studio#command-tools
#
# Opcional:
#   Gradle (sudo apt install gradle)
#   Android NDK (Briefcase también lo descarga si es necesario)
#
# ==============================================================
# Este script automatiza el proceso de compilación:
#   Crea los iconos
#   Crea el proyecto con Briefcase
#   Copia los recursos necesarios
#   Y compila
# ==============================================================

clear
echo -e "\nEstamos creando todo, espera un momento crack... (;\n"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
command -v convert >/dev/null 2>&1 || { echo "Falta ImageMagick (comando 'convert'). Instálalo con: sudo apt install imagemagick"; exit 1; }
command -v briefcase >/dev/null 2>&1 || { echo "Falta Briefcase. Instálalo con: pip install briefcase"; exit 1; }
command -v java >/dev/null 2>&1 || { echo "Falta Java (JDK). Instálalo con: sudo apt install openjdk-17-jdk"; exit 1; }


mkdir -p icons

for size in 48 72 96 144 192 320 480 640 960 1280; do
    convert skull.png -resize ${size}x${size} icons/skull-square-${size}.png
done

for size in 48 72 96 144 192; do
    convert skull.png -resize ${size}x${size} icons/skull-round-${size}.png
done

for size in 108 162 216 324 432; do
    convert skull.png -resize ${size}x${size} icons/skull-adaptive-${size}.png
done

sleep 2

briefcase create android
sleep 2

rm "$SCRIPT_DIR/build/printboxcalc/android/gradle/app/src/main/res/values/colors.xml"
cp "$SCRIPT_DIR/colors.xml" "$SCRIPT_DIR/build/printboxcalc/android/gradle/app/src/main/res/values/"
sleep 1

briefcase build android
sleep 3

mv "$SCRIPT_DIR/build/printboxcalc/android/gradle/app/build/outputs/apk/debug/app-debug.apk" "$SCRIPT_DIR/PrintBoxCalc.apk"
echo -e "\n¡Listo!, ahora revisa la carpeta donde has ejecutado este script, debería haber un archivo llamado 'PrintBoxCalc.apk'\n\n"

