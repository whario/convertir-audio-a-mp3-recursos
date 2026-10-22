# Laboratorio abierto de formatos de audio · Audio Format Lab

**7 archivos desde una misma señal sintética · 22 octubre 2026 · Datos reproducibles**

¿Un archivo **.ogg** siempre usa Opus? ¿**M4A** es un códec? ¿Todo archivo **.3gp** contiene AMR? Este laboratorio compara contenedores y códecs sobre una misma señal de prueba, mediante medidas obtenidas con **FFmpeg/ffprobe**.

> **Alcance:** son ocho segundos de tonos sintéticos mono a 16 kHz, con pausas. **No es voz grabada, un archivo real de WhatsApp, una prueba de compatibilidad con teléfonos, una valoración auditiva, ni un benchmark de servicios de conversión.** No extrapoles los tamaños a grabaciones reales.

## Medidas reales (FFmpeg 7.1.5 / ffprobe 7.1.5)

| Archivo | Códec detectado | Tamaño | Duración informada |
|---|---|---:|---:|
| reference.wav | pcm_s16le | 256 044 bytes | 8.000 s |
| sample.mp3 | mp3 | 65 132 bytes | 8.100 s |
| sample.opus | opus | 32 860 bytes | 8.007 s |
| sample.ogg | vorbis | 13 311 bytes | 8.000 s |
| sample.m4a | aac | 51 419 bytes | 8.000 s |
| sample.aac | aac | 50 999 bytes | 8.461 s |
| sample.3gp | aac | 51 322 bytes | 8.000 s |

**Hallazgos verificables:**

- `.opus` en esta prueba contiene **Opus dentro del contenedor Ogg**; `.ogg` contiene **Vorbis**. La extensión sola no identifica siempre el códec.
- `.m4a`, `.aac` y `.3gp` contienen **AAC** en **contenedores distintos**. **3GP no significa necesariamente AMR.**
- El tiempo de `.aac` estimado por ffprobe es 8.461 s aunque la señal de origen tiene 8 s. Los datos de duración de algunos flujos no indexados pueden estimarse de forma distinta: **no implica audio real adicional**.
- Las variaciones de tamaño no equivalen a comparaciones de calidad perceptiva: los ajustes de codificación y la señal son distintos de los de una nota de voz real.

Datos completos y SHA-256: **[measurements.csv](measurements.csv)** y **[measurements.json](measurements.json)**.

## Reproducir sin subir audios personales

Requisitos: Python 3.9+, FFmpeg y ffprobe instalados; FFmpeg con codificadores `libmp3lame`, `libopus`, `libvorbis` y `aac`.

```bash
python3 generate_samples.py
```

El script crea `generated/reference.wav` y seis archivos derivados; mide sus metadatos con ffprobe y actualiza CSV/JSON. **No llama a servicios remotos**. Los hash y medidas pueden variar según la versión y la compilación de FFmpeg.

**Inspecciona un archivo tuyo de manera local:**

```bash
ffprobe -v error -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels:format=format_name,duration \
  -of json archivo.opus
```

## Diagnóstico de problemas comunes

| Situación | Qué comprobar |
|---|---|
| Un `.ogg` no abre | Detecta si contiene Opus, Vorbis u otro códec, además del contenedor. |
| Un `.m4a` no reproduce en un equipo | Comprueba su códec real (AAC/ALAC, según archivo) y las capacidades del equipo. |
| Un `.3gp` se trata como AMR por defecto | Inspecciona el flujo: el ejemplo `.3gp` de este laboratorio lleva AAC. |
| Quieres archivar un audio en MP3 | Conserva el original; cada conversión con pérdida puede reducir la calidad. |

**Límites:** no hemos generado muestras AMR, porque este entorno FFmpeg no incorpora un codificador AMR. No se ha probado WhatsApp, Telegram, dispositivos, calidad perceptiva ni rendimiento de [ConvertirAudioAmp3](https://convertiraudioamp3.com/).

**Fuentes técnicas:** [MDN audio codecs](https://developer.mozilla.org/en-US/docs/Web/Media/Guides/Formats/Audio_codecs) · [RFC 6716 (Opus)](https://www.rfc-editor.org/rfc/rfc6716) · [RFC 7845 (Ogg Opus)](https://www.rfc-editor.org/rfc/rfc7845) · [ffprobe](https://ffmpeg.org/ffprobe.html).

**Transparencia:** laboratorio mantenido por el desarrollador de ConvertirAudioAmp3; la generación de las muestras no requiere utilizar el servicio web, que realiza las conversiones de usuario en servidor. No hay archivos privados ni código de producción en este repositorio. Código bajo MIT; la señal sintética y los datos producidos por el autor se dedican a CC0 1.0, en la medida permitida por ley.

---

### English summary

**Reproducible 7-format audio codec/container test.** A single synthetic 8-second, mono signal is encoded as WAV/PCM, MP3, Ogg/Opus, Ogg/Vorbis, MP4/AAC (M4A), ADTS/AAC and 3GP/AAC. Run `python3 generate_samples.py` with FFmpeg/ffprobe to regenerate the examples and inspect measurements in CSV/JSON. **No human voices, app-specific WhatsApp samples, device compatibility, or perceptual quality claims.** Encoder version influences output. Maintained by the developer of [ConvertirAudioAmp3](https://convertiraudioamp3.com/).
