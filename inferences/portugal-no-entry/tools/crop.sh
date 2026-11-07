#!/bin/bash
# crop.sh — recorte e ampliação de fólios digitalizados, para leitura de manuscrito.
#
#   tools/crop.sh <imagem> <x> <y> <l> <a> <nome-de-saída> [zoom=2]
#
# Coordenadas na imagem ORIGINAL (os fólios do SSD «ARSI» têm 2250x3000 px).
# A saída vai para _scratch/crops/<nome>.jpg (pasta ignorada pelo git).
# Requer ImageMagick (`magick`).
set -euo pipefail

if [ $# -lt 6 ]; then
    sed -n '2,8p' "$0" | sed 's/^# \{0,1\}//'
    exit 1
fi

HERE="$(cd "$(dirname "$0")/.." && pwd)"
IM="$1"; X="$2"; Y="$3"; W="$4"; H="$5"; OUT="$6"; Z="${7:-2}"

mkdir -p "$HERE/_scratch/crops"
PCT=$(awk -v z="$Z" 'BEGIN{printf "%d%%", z*100}')
DST="$HERE/_scratch/crops/${OUT}.jpg"

magick "$IM" -crop "${W}x${H}+${X}+${Y}" +repage \
    -colorspace Gray -normalize -sharpen 0x1 -resize "$PCT" "$DST"
magick identify "$DST"
