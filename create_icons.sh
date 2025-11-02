mkdir -p icons

# Iconos cuadrados
for size in 48 72 96 144 192 320 480 640 960 1280; do
    convert skull.png -resize ${size}x${size} icons/skull-square-${size}.png
done

# Iconos redondos (incluye ahora el de 48 px)
for size in 48 72 96 144 192; do
    convert skull.png -resize ${size}x${size} icons/skull-round-${size}.png
done

# Iconos adaptativos
for size in 108 162 216 324 432; do
    convert skull.png -resize ${size}x${size} icons/skull-adaptive-${size}.png
done
