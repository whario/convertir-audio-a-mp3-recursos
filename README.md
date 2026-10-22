# ConvertirAudioaMP3 – Recursos públicos

Repositorio público informativo para **[Convertir Audio a MP3](https://convertiraudioamp3.com/)**.  
Reúne accesos directos a las herramientas principales y una breve descripción técnica para quien quiera conocer la solución sin exponer el código interno.

---

## 🔬 Recurso técnico original: laboratorio de formatos de audio

Publicamos un [laboratorio de siete archivos sintéticos reproducibles](audio-format-lab/README.md) para comparar contenedores y códecs WAV/PCM, MP3, Ogg/Opus, Ogg/Vorbis, M4A/AAC, ADTS/AAC y 3GP/AAC. Incluye generador Python/FFmpeg, [datos CSV](audio-format-lab/measurements.csv), [JSON](audio-format-lab/measurements.json), SHA-256 y metodología. No utiliza audios reales ni pretende demostrar compatibilidad de dispositivos.

---

## 🔗 Enlaces principales

- Sitio principal (ES): **[Convertir Audio a MP3](https://convertiraudioamp3.com/)**
- Main site (EN): **[Convert audio to MP3 online](https://convertiraudioamp3.com/en)**

---

## 🧰 Herramientas destacadas

Convierte, recorta, mezcla y comprime audio en segundos desde el navegador:

- **[WhatsApp a MP3](https://convertiraudioamp3.com/convertir-whatsapp-audio-a-mp3)** – Convierte notas y audios de WhatsApp a MP3.
- **[Vídeo a MP3](https://convertiraudioamp3.com/convertir_video_a_mp3)** – Extrae el audio de tus vídeos (MP4, MOV, etc.) a MP3.
- **[Mezclar audios online](https://convertiraudioamp3.com/mezclar-audio)** – Une varias pistas, ajusta tiempos y crea una sola mezcla en MP3.
- **[Recortar audio MP3](https://convertiraudioamp3.com/recortar-audio-mp3)** – Corta fragmentos concretos de un archivo de audio.
- **[Comprimir MP3](https://convertiraudioamp3.com/comprimir-mp3)** – Reduce el peso de tus MP3 manteniendo una buena calidad.
- **[Transcribir audio a texto](https://convertiraudioamp3.com/transcribir-audio-a-texto)** – Convierte voz en texto desde el navegador.

---

## 📱 Versiones mobile (interfaz simple)

Pensadas para usarse directamente desde el móvil, con interfaz mínima:

- **[Mezclar audio (simple)](https://convertiraudioamp3.com/mezclar-audio/simple)**
- **[Recortar audio (simple)](https://convertiraudioamp3.com/recortar-audio-mp3/simple)**

---

## ⚙️ Tecnologías (vista general)

La aplicación principal combina varias piezas:

- **FastAPI** para la capa web y API asíncrona  
  - Alto rendimiento, tipado fuerte en Python y arquitectura sencilla de mantener.
- **FFmpeg** para la conversión y procesamiento de audio/vídeo  
  - Soporte amplio de formatos y pipelines robustos para conversión, recorte y mezcla.

Este repositorio es puramente **informativo** y no contiene el código privado de la aplicación.

---

## ✅ Beneficios principales

- Conversión rápida de audio a MP3, sin instalar software.
- Herramientas específicas para:
  - **[audio de WhatsApp → MP3](https://convertiraudioamp3.com/convertir-whatsapp-audio-a-mp3)**
  - **[vídeo → MP3](https://convertiraudioamp3.com/convertir_video_a_mp3)**
  - recorte, mezcla y compresión de MP3.
- Versiones optimizadas para móvil con interfaces simples.
- Flujo muy directo: subir archivo → procesar → descargar.

---

## ❓ FAQ

**¿Necesito instalar algo para usar ConvertirAudioaMP3?**  
No. Todas las herramientas funcionan directamente en el navegador.

**¿Puedo convertir audios de WhatsApp a MP3?**  
Sí. Usa la herramienta de **[WhatsApp a MP3](https://convertiraudioamp3.com/convertir-whatsapp-audio-a-mp3)**.

**¿Cómo recorto un audio o mezclo dos pistas?**  
Entra en **[Recortar audio MP3](https://convertiraudioamp3.com/recortar-audio-mp3)** o **[Mezclar audios online](https://convertiraudioamp3.com/mezclar-audio)** y sigue los pasos guiados.  
En móvil, puedes usar las versiones simples.

**¿Qué formatos soporta la conversión?**  
Gracias a FFmpeg, se soportan la mayoría de formatos de audio y vídeo habituales.  
Si algún archivo no se procesa correctamente, suele bastar con convertirlo primero a un formato estándar (por ejemplo, MP4 o WAV) y volver a subirlo.

---
