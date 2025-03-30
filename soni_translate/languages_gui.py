# flake8: noqa

news = """ ## 📖 News

        🔥 2024/05/18: Overlap reduction. OpenAI API key integration for transcription, translation, and TTS. Output type: subtitles by speaker, separate audio sound, and video only with subtitles. Now you have access to a better-performing version of Whisper for transcribing speech. For example, you can use `kotoba-tech/kotoba-whisper-v1.1` for Japanese transcription, available [here](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1). You can find these improved models on the [Hugging Face Whisper page](https://huggingface.co/models?pipeline_tag=automatic-speech-recognition&sort=trending&search=whisper). Simply copy the repository ID and paste it into the 'Whisper ASR model' in 'Advanced Settings'. Support for ass subtitles and batch processing with subtitles. Vocal enhancement before transcription. Added CPU mode with `app_rvc.py --cpu_mode`. TTS now supports up to 12 speakers. OpenVoiceV2 has been integrated for voice imitation. PDF to videobook (displays images from the PDF).

        🔥 2024/03/02: Preserve file names in output. Multiple archives can now be submitted simultaneously by specifying their paths, directories or URLs separated by commas. Added option for disabling diarization. Implemented soft subtitles. Format output (MP3, MP4, MKV, WAV, and OGG), and resolved issues related to file reading and diarization.

        🔥 2024/02/22: Added freevc for voice imitation, fixed voiceless track, divide segments. New languages support. New translations of the GUI. With subtitle file, no align and the media file is not needed to process the SRT file. Burn subtitles to video. Queue can accept multiple tasks simultaneously. Sound alert notification. Continue process from last checkpoint. Acceleration rate regulation

        🔥 2024/01/16: Expanded language support, the introduction of whisper large v3, configurable GUI options, integration of BARK, Facebook-mms, Coqui XTTS, and Piper-TTS. Additional features included audio separation utilities, XTTS WAV creation,  use an SRT file as a base for translation, document translation, manual speaker editing, and flexible output options (video, audio, subtitles).

        🔥 2023/10/29: Edit the translated subtitle, download it, adjust volume and speed options.

        🔥 2023/08/03: Changed default options and added directory view of downloads..

        🔥 2023/08/02: Added support for Arabic, Czech, Danish, Finnish, Greek, Hebrew, Hungarian, Korean, Persian, Polish, Russian, Turkish, Urdu, Hindi, and Vietnamese languages. 🌐

        🔥 2023/08/01: Add options for use R.V.C. models.

        🔥 2023/07/27: Fix some bug processing the video and audio.

        🔥 2023/07/26: New UI and add mix options.
        """

language_data = {
    "english": {
        "description": """
        ### **Translate videos easily with N.E.R.V Translate!**

        See the tab `Help` for instructions on how to use it. Let's start having fun with video translation! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Instructions for use:**

        1. 📤 Upload a **video**, **subtitle file**, **audio file**, or provide a 🌐 **URL link** to a video like YouTube.

        2. 🌍 Choose the language in which you want to **translate the video**.

        3. 🗣️ Specify the **number of people speaking** in the video and **assign each one a text-to-speech voice** suitable for the translation language.

        4. 🚀 Press the '**Translate**' button to obtain the results.

        ---

        # 🧩 **N.E.R.V Translate supports different TTS (Text-to-Speech) engines, which are:**
        - EDGE-TTS → format `en-AU-WilliamNeural-Male` → Fast and accurate.
        - FACEBOOK MMS → format `en-facebook-mms VITS` → The voice is more natural; at the moment, it only uses CPU.
        - PIPER TTS → format `en_US-lessac-high VITS-onnx` → Same as the previous one, but it is optimized for both CPU and GPU.
        - BARK → format `en_speaker_0-Male BARK` → Good quality but slow, and it is prone to hallucinations.
        - OpenAI TTS → format `>alloy OpenAI-TTS` → Multilingual but it needs an OpenAI API key.
        - Coqui XTTS → format `_XTTS_/AUTOMATIC.wav` → Only available for Chinese (Simplified), English, French, German, Italian, Portuguese, Polish, Turkish, Russian, Dutch, Czech, Arabic, Spanish, Hungarian, Korean and Japanese.

        ---

        # 🎤 How to Use R.V.C. and R.V.C.2 Voices (Optional) 🎶

        The goal is to apply a R.V.C. to the generated TTS (Text-to-Speech) 🎙️

        1. In the `Custom Voice R.V.C.` tab, download the models you need 📥 You can use links from Hugging Face and Google Drive in formats like zip, pth, or index. You can also download complete HF space repositories, but this option is not very stable 😕

        2. Now, go to `Replace voice: TTS to R.V.C.` and check the `enable` box ✅ After this, you can choose the models you want to apply to each TTS speaker 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Adjust the F0 method that will be applied to all R.V.C. 🎛️

        4. Press `APPLY CONFIGURATION` to apply the changes you made 🔄

        5. Go back to the video translation tab and click on 'Translate' ▶️ Now, the translation will be done applying the R.V.C. 🗣️

        Tip: You can use `Test R.V.C.` to experiment and find the best TTS or configurations to apply to the R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Video translation",
        "video_source": "Choose Video Source",
        "link_label": "Media link.",
        "link_info": "Example: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL goes here...",
        "dir_label": "Video Path.",
        "dir_info": "Example: /usr/home/my_video.mp4",
        "dir_ph": "Path goes here...",
        "sl_label": "Source language",
        "sl_info": "This is the original language of the video",
        "tat_label": "Translate audio to",
        "tat_info": "Select the target language and also make sure to choose the corresponding TTS for that language.",
        "num_speakers": "Select how many people are speaking in the video.",
        "min_sk": "Min speakers",
        "max_sk": "Max speakers",
        "tts_select": "Select the voice you want for each speaker.",
        "sk1": "TTS Speaker 1",
        "sk2": "TTS Speaker 2",
        "sk3": "TTS Speaker 3",
        "sk4": "TTS Speaker 4",
        "sk5": "TTS Speaker 5",
        "sk6": "TTS Speaker 6",
        "sk7": "TTS Speaker 7",
        "sk8": "TTS Speaker 8",
        "sk9": "TTS Speaker 9",
        "sk10": "TTS Speaker 10",
        "sk11": "TTS Speaker 11",
        "sk12": "TTS Speaker 12",
        "vc_title": "Voice Imitation in Different Languages",
        "vc_subtitle": """
        ### Replicate a person's voice across various languages.
        While effective with most voices when used appropriately, it may not achieve perfection in every case.
        Voice Imitation solely replicates the reference speaker's tone, excluding accent and emotion, which are governed by the base speaker TTS model and not replicated by the converter.
        This will take audio samples from the main audio for each speaker and process them.
        """,
        "vc_active_label": "Active Voice Imitation",
        "vc_active_info": "Active Voice Imitation: Replicates the original speaker's tone",
        "vc_method_label": "Method",
        "vc_method_info": "Select a method for Voice Imitation process",
        "vc_segments_label": "Max samples",
        "vc_segments_info": "Max samples: Is the number of audio samples that will be generated for the process, more is better but it can add noise",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Applies vocal dereverb to the audio samples.",
        "vc_remove_label": "Remove previous samples",
        "vc_remove_info": "Remove previous samples: Remove the previous samples generated, so new ones need to be created.",
        "xtts_title": "Create a TTS based on an audio",
        "xtts_subtitle": "Upload an audio file of maximum 10 seconds with a voice. Using XTTS, a new TTS will be created with a voice similar to the provided audio file.",
        "xtts_file_label": "Upload a short audio with the voice",
        "xtts_name_label": "Name for the TTS",
        "xtts_name_info": "Use a simple name",
        "xtts_dereverb_label": "Dereverb audio",
        "xtts_dereverb_info": "Dereverb audio: Applies vocal dereverb to the audio",
        "xtts_button": "Process the audio and include it in the TTS selector",
        "xtts_footer": "Generate voice xtts automatically: You can use `_XTTS_/AUTOMATIC.wav` in the TTS selector to automatically generate segments for each speaker when generating the translation.",
        "extra_setting": "Advanced Settings",
        "acc_max_label": "Max Audio acceleration",
        "acc_max_info": "Maximum acceleration for translated audio segments to avoid overlapping. A value of 1.0 represents no acceleration",
        "acc_rate_label": "Acceleration Rate Regulation",
        "acc_rate_info": "Acceleration Rate Regulation: Adjusts acceleration to accommodate segments requiring less speed, maintaining continuity and considering next-start timing.",
        "or_label": "Overlap Reduction",
        "or_info": "Overlap Reduction: Ensures segments don't overlap by adjusting start times based on previous end times; could disrupt synchronization.",
        "aud_mix_label": "Audio Mixing Method",
        "aud_mix_info": "Mix original and translated audio files to create a customized, balanced output with two available mixing modes.",
        "vol_ori": "Volume original audio",
        "vol_tra": "Volume translated audio",
        "voiceless_tk_label": "Voiceless Track",
        "voiceless_tk_info": "Voiceless Track: Remove the original audio voices before combining it with the translated audio.",
        "sub_type": "Subtitle type",
        "soft_subs_label": "Soft Subtitles",
        "soft_subs_info": "Soft Subtitles: Optional subtitles that viewers can turn on or off while watching the video.",
        "burn_subs_label": "Burn Subtitles",
        "burn_subs_info": "Burn Subtitles: Embed subtitles into the video, making them a permanent part of the visual content.",
        "whisper_title": "Config transcription.",
        "lnum_label": "Literalize Numbers",
        "lnum_info": "Literalize Numbers: Replace numerical representations with their written equivalents in the transcript.",
        "scle_label": "Sound Cleanup",
        "scle_info": "Sound Cleanup: Enhance vocals, remove background noise before transcription for utmost timestamp precision. This operation may take time, especially with lengthy audio files.",
        "sd_limit_label": "Segment Duration Limit",
        "sd_limit_info": "Specify the maximum duration (in seconds) for each segment. The audio will be processed using VAD, limiting the duration for each segment chunk.",
        "asr_model_info": "It converts spoken language to text using the 'Whisper model' by default. Use a custom model, for example, by inputting the repository name 'BELLE-2/Belle-whisper-large-v3-zh' in the dropdown to utilize a Chinese language finetuned model. Find finetuned models on Hugging Face.",
        "ctype_label": "Compute type",
        "ctype_info": "Choosing smaller types like int8 or float16 can improve performance by reducing memory usage and increasing computational throughput, but may sacrifice precision compared to larger data types like float32.",
        "batchz_label": "Batch size",
        "batchz_info": "Reducing the batch size saves memory if your GPU has less VRAM and helps manage Out of Memory issues.",
        "tsscale_label": "Text Segmentation Scale",
        "tsscale_info": "Divide text into segments by sentences, words, or characters. Word and character segmentation offer finer granularity, useful for subtitles; disabling translation preserves original structure.",
        "srt_file_label": "Upload an SRT subtitle file (will be used instead of the transcription of Whisper)",
        "divide_text_label": "Redivide text segments by:",
        "divide_text_info": "(Experimental) Enter a separator to split existing text segments in the source language. The tool will identify occurrences and create new segments accordingly. Specify multiple separators using |, e.g.: !|?|...|。",
        "diarization_label": "Diarization model",
        "tr_process_label": "Translation process",
        "out_type_label": "Output type",
        "out_name_label": "File name",
        "out_name_info": "The name of the output file",
        "task_sound_label": "Task Status Sound",
        "task_sound_info": "Task Status Sound: Plays a sound alert indicating task completion or errors during execution.",
        "cache_label": "Retrieve Progress",
        "cache_info": "Retrieve Progress: Continue process from last checkpoint.",
        "preview_info": "Preview cuts the video to only 10 seconds for testing purposes. Please deactivate it to retrieve the full video duration.",
        "edit_sub_label": "Edit generated subtitles",
        "edit_sub_info": "Edit generated subtitles: Allows you to run the translation in 2 steps. First with the 'GET SUBTITLES AND EDIT' button, you get the subtitles to edit them, and then with the 'TRANSLATE' button, you can generate the video",
        "button_subs": "GET SUBTITLES AND EDIT",
        "editor_sub_label": "Generated subtitles",
        "editor_sub_info": "Feel free to edit the text in the generated subtitles here. You can make changes to the interface options before clicking the 'TRANSLATE' button, except for 'Source language', 'Translate audio to', and 'Max speakers', to avoid errors. Once you're finished, click the 'TRANSLATE' button.",
        "editor_sub_ph": "First press 'GET SUBTITLES AND EDIT' to get the subtitles",
        "button_translate": "TRANSLATE",
        "output_result_label": "DOWNLOAD TRANSLATED VIDEO",
        "sub_ori": "Subtitles",
        "sub_tra": "Translated subtitles",
        "ht_token_info": "One important step is to accept the license agreement for using Pyannote. You need to have an account on Hugging Face and accept the license to use the models: https://huggingface.co/pyannote/speaker-diarization and https://huggingface.co/pyannote/segmentation. Get your KEY TOKEN here: https://hf.co/settings/tokens",
        "ht_token_ph": "Token goes here...",
        "tab_docs": "Document translation",
        "docs_input_label": "Choose Document Source",
        "docs_input_info": "It can be PDF, DOCX, TXT, or text",
        "docs_source_info": "This is the original language of the text",
        "chunk_size_label": "Max number of characters that the TTS will process per segment",
        "chunk_size_info": "A value of 0 assigns a dynamic and more compatible value for the TTS.",
        "docs_button": "Start Language Conversion Bridge",
        "cv_url_info": "Automatically download the R.V.C. models from the URL. You can use links from HuggingFace or Drive, and you can include several links, each one separated by a comma. Example: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Replace voice: TTS to R.V.C.",
        "sec1_title": "### 1. To enable its use, mark it as enable.",
        "enable_replace": "Check this to enable the use of the models.",
        "sec2_title": "### 2. Select a voice that will be applied to each TTS of each corresponding speaker and apply the configurations.",
        "sec2_subtitle": "Depending on how many <TTS Speaker> you will use, each one needs its respective model. Additionally, there is an auxiliary one if for some reason the speaker is not detected correctly.",
        "cv_tts1": "Choose the voice to apply for Speaker 1.",
        "cv_tts2": "Choose the voice to apply for Speaker 2.",
        "cv_tts3": "Choose the voice to apply for Speaker 3.",
        "cv_tts4": "Choose the voice to apply for Speaker 4.",
        "cv_tts5": "Choose the voice to apply for Speaker 5.",
        "cv_tts6": "Choose the voice to apply for Speaker 6.",
        "cv_tts7": "Choose the voice to apply for Speaker 7.",
        "cv_tts8": "Choose the voice to apply for Speaker 8.",
        "cv_tts9": "Choose the voice to apply for Speaker 9.",
        "cv_tts10": "Choose the voice to apply for Speaker 10.",
        "cv_tts11": "Choose the voice to apply for Speaker 11.",
        "cv_tts12": "Choose the voice to apply for Speaker 12.",
        "cv_aux": "- Voice to apply in case a Speaker is not detected successfully.",
        "cv_button_apply": "APPLY CONFIGURATION",
        "tab_help": "Help",
    },
    "spanish": {
        "description": """
        ### 🎥 **¡Traduce videos fácilmente con SoniTranslate!** 📽️

        Sube un video, audio o proporciona un enlace de YouTube. 📽️ **Obtén el cuaderno actualizado desde el repositorio oficial: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Consulta la pestaña `Ayuda` para obtener instrucciones sobre cómo usarlo. ¡Comencemos a divertirnos con la traducción de videos! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Instrucciones de uso:**

        1. 📤 Sube un archivo de **video**, **audio** o proporciona un enlace de 🌐 **YouTube**.

        2. 🌍 Elige el idioma en el que deseas **traducir el video**.

        3. 🗣️ Especifica el **número de personas que hablan** en el video y **asigna a cada una una voz de texto a voz** adecuada para el idioma de traducción.

        4. 🚀 Presiona el botón '**Traducir**' para obtener los resultados.

        ---

        # 🧩 **SoniTranslate admite diferentes motores de TTS (Texto a Voz), los cuales son:**
        - EDGE-TTS → formato `en-AU-WilliamNeural-Male` → Rapidos y precisos.
        - FACEBOOK MMS → formato `en-facebook-mms VITS` → Voz más natural, por el momento solo usa CPU.
        - PIPER TTS → formato `en_US-lessac-high VITS-onnx` → Igual que el anterior, pero está optimizado tanto para CPU como para GPU.
        - BARK → formato `en_speaker_0-Male BARK` → De buena calidad pero lento y propenso a alucinaciones.
        - OpenAI TTS → formato `>alloy OpenAI-TTS` → Multilingüe pero necesita una OpenAI API key.
        - Coqui XTTS → formato `_XTTS_/AUTOMATIC.wav` → Solo disponible para Chinese (Simplified), English, French, German, Italian, Portuguese, Polish, Turkish, Russian, Dutch, Czech, Arabic, Spanish, Hungarian, Korean y Japanese.

        ---

        # 🎤 Cómo usar las voces R.V.C. y R.V.C.2 (Opcional) 🎶

        El objetivo es aplicar un R.V.C. al TTS (Texto a Voz) generado 🎙️

        1. En la pestaña `Voz Personalizada R.V.C.`, descarga los modelos que necesitas 📥 Puedes utilizar enlaces de Hugging Face y Google Drive en formatos como zip, pth o index. También puedes descargar repositorios completos de espacio HF, pero esta opción no es muy estable 😕

        2. Ahora, ve a `Reemplazar voz: TTS a R.V.C.` y marca la casilla `habilitar` ✅ Después de esto, puedes elegir los modelos que deseas aplicar a cada hablante de TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Ajusta el método F0 que se aplicará a todos los R.V.C. 🎛️

        4. Presiona `APLICAR CONFIGURACIÓN` para aplicar los cambios que hayas realizado 🔄

        5. Vuelve a la pestaña de traducción de video y haz clic en 'Traducir' ▶️ Ahora, la traducción se realizará aplicando el R.V.C. 🗣️

        Consejo: Puedes usar `Probar R.V.C.` para experimentar y encontrar el mejor TTS o configuraciones para aplicar al R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Traducción de video",
        "video_source": "Seleccionar Fuente de Video",
        "link_label": "URL del video.",
        "link_info": "Ejemplo: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "Ingrese la URL aquí...",
        "dir_label": "Ubicación del video.",
        "dir_info": "Ejemplo: /usr/home/my_video.mp4",
        "dir_ph": "Ingrese la ruta aquí...",
        "sl_label": "Idioma de origen",
        "sl_info": "Este es el idioma original del video",
        "tat_label": "Traducir audio a",
        "tat_info": "Seleccione el idioma de destino y asegúrese también de seleccionar los TTS correspondientes a ese lenguaje.",
        "num_speakers": "Seleccione cuántas personas están hablando en el video.",
        "min_sk": "Mín. de hablantes",
        "max_sk": "Máx. de hablantes",
        "tts_select": "Seleccione la voz que desea para cada hablante.",
        "sk1": "TTS Hablante 1",
        "sk2": "TTS Hablante 2",
        "sk3": "TTS Hablante 3",
        "sk4": "TTS Hablante 4",
        "sk5": "TTS Hablante 5",
        "sk6": "TTS Hablante 6",
        "sk7": "TTS Hablante 7",
        "sk8": "TTS Hablante 8",
        "sk9": "TTS Hablante 9",
        "sk10": "TTS Hablante 10",
        "sk11": "TTS Hablante 11",
        "sk12": "TTS Hablante 12",
        "vc_title": "Imitación de voz en diferentes idiomas",
        "vc_subtitle": """
        ### Replicar la voz de una persona en varios idiomas.
        Si bien es efectiva con la mayoría de las voces cuando se usa adecuadamente, puede no alcanzar la perfección en todos los casos.
        La imitación de voz solo replica el tono del hablante de referencia, excluyendo el acento y la emoción, que son controlados por el modelo TTS del hablante base y no son replicados por el convertidor.
        Esto tomará muestras de audio del audio principal para cada hablante y las procesará.
        """,
        "vc_active_label": "Imitación de voz activa",
        "vc_active_info": "Imitación de voz activa: Replica el tono del hablante original",
        "vc_method_label": "Método",
        "vc_method_info": "Selecciona un método para el proceso de imitación de voz",
        "vc_segments_label": "Máximo de muestras",
        "vc_segments_info": "Máximo de muestras: Es el número de muestras de audio que se generarán para el proceso, más es mejor pero puede agregar ruido",
        "vc_dereverb_label": "Dereverberación",
        "vc_dereverb_info": "Dereverberación: Aplica la dereverberación vocal a las muestras de audio.",
        "vc_remove_label": "Eliminar muestras anteriores",
        "vc_remove_info": "Eliminar muestras anteriores: Elimina las muestras generadas anteriormente, por lo que es necesario crear nuevas.",
        "xtts_title": "Crear un TTS basado en un audio",
        "xtts_subtitle": "Sube un archivo de audio de máximo 10 segundos con una voz. Utilizando XTTS, se creará un nuevo TTS con una voz similar al archivo de audio proporcionado.",
        "xtts_file_label": "Subir un breve audio con la voz",
        "xtts_name_label": "Nombre para el TTS",
        "xtts_name_info": "Usa un nombre sencillo",
        "xtts_dereverb_label": "Dereverberación del audio",
        "xtts_dereverb_info": "Dereverberación del audio: Aplica la dereverberación vocal al audio",
        "xtts_button": "Procesar el audio e incluirlo en el selector de TTS",
        "xtts_footer": "Generar voz XTTS automáticamente: Puedes usar `_XTTS_/AUTOMATIC.wav` en el selector de TTS para generar automáticamente segmentos para cada hablante al generar la traducción.",
        "extra_setting": "Configuraciones Avanzadas",
        "acc_max_label": "Máx. de Aceleración de Audio",
        "acc_max_info": "Aceleración máxima para segmentos de audio traducidos para evitar superposiciones. Un valor de 1.0 representa ninguna aceleración.",
        "acc_rate_label": "Regulación de la Tasa de Aceleración",
        "acc_rate_info": "Regulación de la Tasa de Aceleración: Ajusta la aceleración para adaptarse a segmentos que requieren menos velocidad, manteniendo la continuidad y considerando el momento de inicio siguiente.",
        "or_label": "Reducción de superposición",
        "or_info": "Reducción de superposición: Asegura que los segmentos no se superpongan ajustando los tiempos de inicio en función de los tiempos de finalización anteriores; podría interrumpir la sincronización.",
        "aud_mix_label": "Método de Mezcla de Audio",
        "aud_mix_info": "Mezclar archivos de audio original y traducido para crear una salida personalizada y equilibrada con dos modos de mezcla disponibles.",
        "vol_ori": "Volumen audio original",
        "vol_tra": "Volumen audio traducido",
        "voiceless_tk_label": "Pista sin voz",
        "voiceless_tk_info": "Pista sin voz: Elimina las voces originales del audio antes de combinarlo con el audio traducido.",
        "sub_type": "Tipo de Subtítulos",
        "soft_subs_label": "Subtítulos Suaves",
        "soft_subs_info": "Subtítulos Suaves: Subtítulos opcionales que los espectadores pueden activar o desactivar mientras ven el video.",
        "burn_subs_label": "Grabar subtítulos",
        "burn_subs_info": "Grabar subtítulos: Incrusta los subtítulos en el video, convirtiéndolos en una parte permanente del contenido visual.",
        "whisper_title": "Configuracion Transcripción.",
        "lnum_label": "Literalizar Números",
        "lnum_info": "Literalizar Números: Reemplazar representaciones numéricas con sus equivalentes escritos en la transcripción.",
        "scle_label": "Limpieza de Sonido",
        "scle_info": "Limpieza de Sonido: Mejora de vocales, elimina ruido de fondo antes de la transcripción para una precisión máxima en la marca de tiempo. Esta operación puede tomar tiempo, especialmente con archivos de audio extensos.",
        "sd_limit_label": "Límite de Duración del Segmento",
        "sd_limit_info": "Especifique la duración máxima (en segundos) para cada segmento. El audio se procesará utilizando VAD, limitando la duración para cada fragmento de segmento.",
        "asr_model_info": "Convierte el lenguaje hablado a texto utilizando el modelo 'Whisper' de forma predeterminada. Utilice un modelo personalizado, por ejemplo, ingresando el nombre del repositorio 'BELLE-2/Belle-whisper-large-v3-zh' en el menú desplegable para utilizar un modelo en chino preajustado. Encuentre modelos preajustados en Hugging Face.",
        "ctype_label": "Tipo de Cálculo",
        "ctype_info": "Elegir tipos más pequeños como int8 o float16 puede mejorar el rendimiento al reducir el uso de memoria y aumentar el rendimiento computacional, pero puede sacrificar precisión en comparación con tipos de datos más grandes como float32.",
        "batchz_label": "Tamaño del Lote",
        "batchz_info": "Reducir el tamaño del lote ahorra memoria si su GPU tiene menos VRAM y ayuda a gestionar problemas de falta de memoria.",
        "tsscale_label": "Escala de Segmentación de Texto",
        "tsscale_info": "Divide el texto en segmentos por oraciones, palabras o caracteres. La segmentación por palabras y caracteres ofrece una granularidad más fina, útil para subtítulos; desactivar la traducción conserva la estructura original.",
        "srt_file_label": "Subir un archivo de subtítulos SRT (Se utilizará en lugar de la transcripción de Whisper)",
        "divide_text_label": "Redividir segmentos de texto por:",
        "divide_text_info": "(Experimental) Ingresa un separador para dividir los segmentos de texto existentes en el idioma origen. La herramienta identificará las ocurrencias y creará nuevos segmentos en consecuencia. Especifica múltiples separadores usando |, por ejemplo: !|?|...|。",
        "diarization_label": "Modelo de diarización",
        "tr_process_label": "Proceso de traducción",
        "out_type_label": "Tipo de salida",
        "out_name_label": "Nombre del archivo",
        "out_name_info": "El nombre del archivo de salida",
        "task_sound_label": "Sonido de estado de la tarea",
        "task_sound_info": "Sonido de estado de la tarea: Reproduce una alerta de sonido que indica la finalización de la tarea o errores durante la ejecución.",
        "cache_label": "Recuperar Progreso",
        "cache_info": "Recuperar Progreso: Continuar proceso desde el último punto de control.",
        "preview_info": "La vista previa corta el video a solo 10 segundos con fines de prueba. Desactívelo para obtener la duración completa del video.",
        "edit_sub_label": "Editar subtítulos generados",
        "edit_sub_info": "Editar subtítulos generados: Permite ejecutar la traducción en 2 pasos. Primero, con el botón 'OBTENER SUBTÍTULOS Y EDITAR', obtiene los subtítulos para editarlos, y luego con el botón 'TRADUCIR', puede generar el video.",
        "button_subs": "OBTENER SUBTÍTULOS Y EDITAR",
        "editor_sub_label": "Subtítulos generados",
        "editor_sub_info": "Siéntase libre de editar el texto de los subtítulos generados aquí. Puede realizar cambios en las opciones de la interfaz antes de hacer clic en el botón 'TRADUCIR', excepto en 'Idioma de origen', 'Traducir audio a' y 'Máx. de hablantes', para evitar errores. Una vez que haya terminado, haga clic en el botón 'TRADUCIR'.",
        "editor_sub_ph": "Presione primero 'OBTENER SUBTÍTULOS Y EDITAR' para obtener los subtítulos",
        "button_translate": "TRADUCIR",
        "output_result_label": "DESCARGAR VIDEO TRADUCIDO",
        "sub_ori": "Subtítulos originales",
        "sub_tra": "Subtítulos traducidos",
        "ht_token_info": "Un paso importante es aceptar el acuerdo de licencia para usar Pyannote. Debe tener una cuenta en Hugging Face y aceptar la licencia para usar los modelos: https://huggingface.co/pyannote/speaker-diarization y https://huggingface.co/pyannote/segmentation. Obtenga su TOKEN aquí: https://hf.co/settings/tokens",
        "ht_token_ph": "Ingrese el token aquí...",
        "tab_docs": "Traducción de documento",
        "docs_input_label": "Elegir origen del documento",
        "docs_input_info": "Puede ser PDF, DOCX, TXT o texto",
        "docs_source_info": "Este es el idioma original del texto",
        "chunk_size_label": "Máximo numero de caracteres que el TTS procesará por segmento.",
        "chunk_size_info": "Un valor de 0 signa un valor dinámico y mejor combatible con el TTS.",
        "docs_button": "Iniciar Puente de Conversión de Idioma",
        "cv_url_info": "Descargue automáticamente los modelos R.V.C. desde la URL. Puede utilizar enlaces de HuggingFace o Drive, e incluso puede incluir varios enlaces, cada uno separado por una coma. Ejemplo: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Reemplazar voz: TTS a R.V.C.",
        "sec1_title": "### 1. Para habilitar su uso, márquelo como habilitado.",
        "enable_replace": "Marque esto para habilitar el uso de los modelos.",
        "sec2_title": "### 2. Seleccione una voz que se aplicará a cada TTS de cada hablante correspondiente y aplique las configuraciones.",
        "sec2_subtitle": "Dependiendo de cuántos <TTS Hablante> vaya a usar, cada uno necesita su respectivo modelo. Además, hay uno auxiliar si por alguna razón el hablante no es detectado correctamente.",
        "cv_tts1": "Voz a aplicar al TTS Hablante 1.",
        "cv_tts2": "Voz a aplicar al TTS Hablante 2.",
        "cv_tts3": "Voz a aplicar al TTS Hablante 3.",
        "cv_tts4": "Voz a aplicar al TTS Hablante 4.",
        "cv_tts5": "Voz a aplicar al TTS Hablante 5.",
        "cv_tts6": "Voz a aplicar al TTS Hablante 6.",
        "cv_tts7": "Voz a aplicar al TTS Hablante 7.",
        "cv_tts8": "Voz a aplicar al TTS Hablante 8.",
        "cv_tts9": "Voz a aplicar al TTS Hablante 9.",
        "cv_tts10": "Voz a aplicar al TTS Hablante 10.",
        "cv_tts11": "Voz a aplicar al TTS Hablante 11.",
        "cv_tts12": "Voz a aplicar al TTS Hablante 12.",
        "cv_aux": "- Voz a aplicar en caso de que un hablante no sea detectado correctamente.",
        "cv_button_apply": "APLICAR CONFIGURACIÓN",
        "tab_help": "Ayuda",
    },
    "french": {
        "description": """
        ### 🎥 **Traduisez facilement les vidéos avec SoniTranslate !** 📽️

        Téléchargez une vidéo, un fichier audio ou fournissez un lien YouTube. 📽️ **Obtenez le notebook mis à jour à partir du référentiel officiel : [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Consultez l'onglet `Aide` pour des instructions sur son utilisation. Amusons-nous à traduire des vidéos ! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Instructions d'utilisation :**

        1. 📤 Téléchargez une **vidéo**, un **fichier audio** ou fournissez un lien 🌐 **YouTube**.

        2. 🌍 Choisissez la langue dans laquelle vous souhaitez **traduire la vidéo**.

        3. 🗣️ Spécifiez le **nombre de personnes parlant** dans la vidéo et **attribuez à chacune une voix de synthèse textuelle** adaptée à la langue de traduction.

        4. 🚀 Appuyez sur le bouton '**Traduire**' pour obtenir les résultats.

        ---

        # 🧩 **SoniTranslate prend en charge différents moteurs TTS (Text-to-Speech), à savoir :**
        - EDGE-TTS → format `en-AU-WilliamNeural-Male` → Rapide et précis.
        - FACEBOOK MMS → format `en-facebook-mms VITS` → La voix est plus naturelle ; pour le moment, il utilise uniquement le CPU.
        - PIPER TTS → format `en_US-lessac-high VITS-onnx` → Identique au précédent, mais optimisé pour le CPU et le GPU.
        - BARK → format `en_speaker_0-Male BARK` → Bonne qualité mais lent, et sujet aux hallucinations.
        - OpenAI TTS → format `>alloy OpenAI-TTS` → Multilingue mais nécessite une OpenAI API key.
        - Coqui XTTS → format `_XTTS_/AUTOMATIC.wav` → Disponible uniquement pour le chinois (simplifié), l'anglais, le français, l'allemand, l'italien, le portugais, le polonais, le turc, le russe, le néerlandais, le tchèque, l'arabe, l'espagnol, le hongrois, le coréen et le japonais.

        ---

        # 🎤 Comment utiliser les voix R.V.C. et R.V.C.2 (Facultatif) 🎶

        L'objectif est d'appliquer un R.V.C. à la TTS (Text-to-Speech) générée 🎙️

        1. Dans l'onglet `Voix personnalisée R.V.C.`, téléchargez les modèles dont vous avez besoin 📥 Vous pouvez utiliser des liens depuis Hugging Face et Google Drive dans des formats tels que zip, pth, ou index. Vous pouvez également télécharger des dépôts complets de l'espace HF, mais cette option n'est pas très stable 😕

        2. Allez maintenant dans `Remplacer la voix : TTS par R.V.C.` et cochez la case `activer` ✅ Ensuite, vous pouvez choisir les modèles que vous souhaitez appliquer à chaque locuteur TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Ajustez la méthode F0 qui sera appliquée à tous les R.V.C. 🎛️

        4. Appuyez sur `APPLIQUER LA CONFIGURATION` pour appliquer les modifications que vous avez apportées 🔄

        5. Retournez à l'onglet de traduction vidéo et cliquez sur 'Traduire' ▶️ Maintenant, la traduction se fera en appliquant le R.V.C. 🗣️

        Astuce : Vous pouvez utiliser `Test R.V.C.` pour expérimenter et trouver les meilleures TTS ou configurations à appliquer au R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Traduction vidéo",
        "video_source": "Choisir la source vidéo",
        "link_label": "Lien multimédia.",
        "link_info": "Exemple : www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "L'URL va ici...",
        "dir_label": "Chemin de la vidéo.",
        "dir_info": "Exemple : /usr/home/ma_video.mp4",
        "dir_ph": "Le chemin va ici...",
        "sl_label": "Langue source",
        "sl_info": "Il s'agit de la langue d'origine de la vidéo",
        "tat_label": "Traduire l'audio en",
        "tat_info": "Sélectionnez la langue cible et assurez-vous également de choisir le TTS correspondant pour cette langue.",
        "num_speakers": "Sélectionnez combien de personnes parlent dans la vidéo.",
        "min_sk": "Locuteurs min",
        "max_sk": "Locuteurs max",
        "tts_select": "Sélectionnez la voix que vous souhaitez pour chaque locuteur.",
        "sk1": "Locuteur TTS 1",
        "sk2": "Locuteur TTS 2",
        "sk3": "Locuteur TTS 3",
        "sk4": "Locuteur TTS 4",
        "sk5": "Locuteur TTS 5",
        "sk6": "Locuteur TTS 6",
        "sk7": "Locuteur TTS 7",
        "sk8": "Locuteur TTS 8",
        "sk9": "Locuteur TTS 9",
        "sk10": "Locuteur TTS 10",
        "sk11": "Locuteur TTS 11",
        "sk12": "Locuteur TTS 12",
        "vc_title": "Imitation de voix dans différentes langues",
        "vc_subtitle": """
        ### Répliquez la voix d'une personne dans différentes langues.
        Bien que efficace avec la plupart des voix lorsqu'il est utilisé correctement, cela peut ne pas atteindre la perfection dans tous les cas.
        L'imitation de voix ne reproduit que le ton du locuteur de référence, excluant l'accent et l'émotion, qui sont régis par le modèle TTS du locuteur de base et non reproduits par le convertisseur.
        Cela prendra des échantillons audio de l'audio principal pour chaque locuteur et les traitera.
        """,
        "vc_active_label": "Imitation de voix active",
        "vc_active_info": "Imitation de voix active : Reproduit le ton du locuteur original",
        "vc_method_label": "Méthode",
        "vc_method_info": "Sélectionnez une méthode pour le processus d'imitation de voix",
        "vc_segments_label": "Échantillons max",
        "vc_segments_info": "Échantillons max : Nombre d'échantillons audio qui seront générés pour le processus, plus il y en a, mieux c'est, mais cela peut ajouter du bruit",
        "vc_dereverb_label": "Déréverbération",
        "vc_dereverb_info": "Déréverbération : Applique une déréverbération vocale aux échantillons audio.",
        "vc_remove_label": "Supprimer les échantillons précédents",
        "vc_remove_info": "Supprimer les échantillons précédents : Supprime les échantillons précédents générés, de sorte que de nouveaux doivent être créés.",
        "xtts_title": "Créer un TTS basé sur un audio",
        "xtts_subtitle": "Téléchargez un fichier audio d'une durée maximale de 10 secondes avec une voix. En utilisant XTTS, un nouveau TTS sera créé avec une voix similaire au fichier audio fourni.",
        "xtts_file_label": "Télécharger un court audio avec la voix",
        "xtts_name_label": "Nom pour le TTS",
        "xtts_name_info": "Utilisez un nom simple",
        "xtts_dereverb_label": "Déréverbération de l'audio",
        "xtts_dereverb_info": "Déréverbération de l'audio : Applique une déréverbération vocale à l'audio",
        "xtts_button": "Traiter l'audio et l'inclure dans le sélecteur TTS",
        "xtts_footer": "Générer automatiquement un TTS vocal : Vous pouvez utiliser `_XTTS_/AUTOMATIC.wav` dans le sélecteur TTS pour générer automatiquement des segments pour chaque locuteur lors de la génération de la traduction.",
        "extra_setting": "Paramètres avancés",
        "acc_max_label": "Accélération audio max",
        "acc_max_info": "Accélération maximale pour les segments audio traduits afin d'éviter les chevauchements. Une valeur de 1,0 représente aucune accélération",
        "acc_rate_label": "Régulation du taux d'accélération",
        "acc_rate_info": "Régulation du taux d'accélération : Ajuste l'accélération pour prendre en compte les segments nécessitant moins de vitesse, en maintenant la continuité et en tenant compte du timing du prochain démarrage.",
        "or_label": "Réduction des chevauchements",
        "or_info": "Réduction des chevauchements : Garantit que les segments ne se chevauchent pas en ajustant les heures de début en fonction des heures de fin précédentes ; pourrait perturber la synchronisation.",
        "aud_mix_label": "Méthode de mixage audio",
        "aud_mix_info": "Mixer les fichiers audio original et traduit pour créer une sortie équilibrée et personnalisée avec deux modes de mixage disponibles.",
        "vol_ori": "Volume audio original",
        "vol_tra": "Volume audio traduit",
        "voiceless_tk_label": "Piste sans voix",
        "voiceless_tk_info": "Piste sans voix : Supprime les voix audio originales avant de les combiner avec l'audio traduit.",
        "sub_type": "Type de sous-titres",
        "soft_subs_label": "Sous-titres souples",
        "soft_subs_info": "Sous-titres souples : Sous-titres facultatifs que les spectateurs peuvent activer ou désactiver pendant le visionnage de la vidéo.",
        "burn_subs_label": "Incorporer les sous-titres",
        "burn_subs_info": "Incorporer les sous-titres : Intégrer les sous-titres dans la vidéo, les rendant ainsi une partie permanente du contenu visuel.",
        "whisper_title": "Config transcription.",
        "lnum_label": "Literaliser les Nombres",
        "lnum_info": "Literaliser les Nombres: Remplacer les représentations numériques par leurs équivalents écrits dans la transcription.",
        "scle_label": "Nettoyage du Son",
        "scle_info": "Nettoyage du Son: Amélioration des voix, suppression du bruit de fond avant la transcription pour une précision maximale des horodatages. Cette opération peut prendre du temps, notamment avec des fichiers audio volumineux.",
        "sd_limit_label": "Limite de Durée du Segment",
        "sd_limit_info": "Spécifiez la durée maximale (en secondes) pour chaque segment. L'audio sera traité en utilisant VAD, limitant la durée pour chaque fragment de segment.",
        "asr_model_info": "Il convertit la langue parlée en texte en utilisant le modèle 'Whisper' par défaut. Utilisez un modèle personnalisé, par exemple, en saisissant le nom du référentiel 'BELLE-2/Belle-whisper-large-v3-zh' dans la liste déroulante pour utiliser un modèle chinois préajusté. Trouvez des modèles préajustés sur Hugging Face.",
        "ctype_label": "Type de Calcul",
        "ctype_info": "Choisir des types plus petits comme int8 ou float16 peut améliorer les performances en réduisant l'utilisation de la mémoire et en augmentant le débit computationnel, mais peut sacrifier la précision par rapport à des types de données plus grands comme float32.",
        "batchz_label": "Taille du Lot",
        "batchz_info": "Réduire la taille du lot permet d'économiser de la mémoire si votre GPU dispose de moins de VRAM et aide à gérer les problèmes de mémoire insuffisante.",
        "tsscale_label": "Échelle de Segmentation de Texte",
        "tsscale_info": "Divisez le texte en segments par phrases, mots ou caractères. La segmentation par mots et caractères offre une granularité plus fine, utile pour les sous-titres; désactiver la traduction conserve la structure d'origine.",
        "srt_file_label": "Télécharger un fichier de sous-titres SRT (sera utilisé à la place de la transcription de Whisper)",
        "divide_text_label": "Rediviser les segments de texte par :",
        "divide_text_info": "(Expérimental) Entrez un séparateur pour diviser les segments de texte existants dans la langue source. L'outil identifiera les occurrences et créera de nouveaux segments en conséquence. Spécifiez plusieurs séparateurs en utilisant |, par ex. : !|?|...|。",
        "diarization_label": "Modèle de diarisation",
        "tr_process_label": "Processus de traduction",
        "out_type_label": "Type de sortie",
        "out_name_label": "Nom de fichier",
        "out_name_info": "Le nom du fichier de sortie",
        "task_sound_label": "Son d'état de la tâche",
        "task_sound_info": "Son d'état de la tâche : Joue une alerte sonore indiquant la fin de la tâche ou les erreurs lors de l'exécution.",
        "cache_label": "Récupération de la progression",
        "cache_info": "Récupération de la progression : Continuer le processus depuis le dernier point de contrôle.",
        "preview_info": "L'aperçu coupe la vidéo à seulement 10 secondes à des fins de test. Veuillez le désactiver pour récupérer la durée complète de la vidéo.",
        "edit_sub_label": "Modifier les sous-titres générés",
        "edit_sub_info": "Modifier les sous-titres générés : Vous permet d'exécuter la traduction en 2 étapes. Tout d'abord avec le bouton 'OBTENIR LES SOUS-TITRES ET ÉDITER', vous obtenez les sous-titres pour les éditer, puis avec le bouton 'TRADUIRE', vous pouvez générer la vidéo",
        "button_subs": "OBTENIR LES SOUS-TITRES ET ÉDITER",
        "editor_sub_label": "Sous-titres générés",
        "editor_sub_info": "N'hésitez pas à éditer le texte dans les sous-titres générés ici. Vous pouvez apporter des modifications aux options d'interface avant de cliquer sur le bouton 'TRADUIRE', sauf pour 'Langue source', 'Traduire l'audio en' et 'Locuteurs max', pour éviter les erreurs. Une fois terminé, cliquez sur le bouton 'TRADUIRE'.",
        "editor_sub_ph": "Appuyez d'abord sur 'OBTENIR LES SOUS-TITRES ET ÉDITER' pour obtenir les sous-titres",
        "button_translate": "TRADUIRE",
        "output_result_label": "TÉLÉCHARGER LA VIDÉO TRADUITE",
        "sub_ori": "Sous-titres",
        "sub_tra": "Sous-titres traduits",
        "ht_token_info": "Une étape importante est d'accepter l'accord de licence pour utiliser Pyannote. Vous devez avoir un compte sur Hugging Face et accepter la licence pour utiliser les modèles : https://huggingface.co/pyannote/speaker-diarization et https://huggingface.co/pyannote/segmentation. Obtenez votre JETON CLÉ ici : https://hf.co/settings/tokens",
        "ht_token_ph": "Le jeton va ici...",
        "tab_docs": "Traduction de documents",
        "docs_input_label": "Choisir la source du document",
        "docs_input_info": "Il peut s'agir de PDF, DOCX, TXT ou texte",
        "docs_source_info": "Il s'agit de la langue d'origine du texte",
        "chunk_size_label": "Nombre maximal de caractères que le TTS traitera par segment",
        "chunk_size_info": "Une valeur de 0 attribue une valeur dynamique et plus compatible pour le TTS.",
        "docs_button": "Démarrer le pont de conversion de langue",
        "cv_url_info": "Téléchargez automatiquement les modèles R.V.C. depuis l'URL. Vous pouvez utiliser des liens depuis HuggingFace ou Drive, et vous pouvez inclure plusieurs liens, chacun séparé par une virgule. Exemple : https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Remplacer la voix : TTS par R.V.C.",
        "sec1_title": "### 1. Pour activer son utilisation, marquez-la comme activée.",
        "enable_replace": "Cochez pour activer l'utilisation des modèles.",
        "sec2_title": "### 2. Sélectionnez une voix qui sera appliquée à chaque TTS de chaque locuteur correspondant et appliquez les configurations.",
        "sec2_subtitle": "En fonction du nombre de <Locuteur TTS> que vous utiliserez, chacun doit avoir son modèle respectif. De plus, il y a un auxiliaire si pour une raison quelconque le locuteur n'est pas détecté correctement.",
        "cv_tts1": "Choisissez la voix à appliquer pour le Locuteur 1.",
        "cv_tts2": "Choisissez la voix à appliquer pour le Locuteur 2.",
        "cv_tts3": "Choisissez la voix à appliquer pour le Locuteur 3.",
        "cv_tts4": "Choisissez la voix à appliquer pour le Locuteur 4.",
        "cv_tts5": "Choisissez la voix à appliquer pour le Locuteur 5.",
        "cv_tts6": "Choisissez la voix à appliquer pour le Locuteur 6.",
        "cv_tts7": "Choisissez la voix à appliquer pour le Locuteur 7.",
        "cv_tts8": "Choisissez la voix à appliquer pour le Locuteur 8.",
        "cv_tts9": "Choisissez la voix à appliquer pour le Locuteur 9.",
        "cv_tts10": "Choisissez la voix à appliquer pour le Locuteur 10.",
        "cv_tts11": "Choisissez la voix à appliquer pour le Locuteur 11.",
        "cv_tts12": "Choisissez la voix à appliquer pour le Locuteur 12.",
        "cv_aux": "- Voix à appliquer en cas de détection incorrecte d'un locuteur.",
        "cv_button_apply": "APPLIQUER LA CONFIGURATION",
        "tab_help": "Aide",
    },
    "german": {
        "description": """
        ### 🎥 **Übersetzen Sie Videos einfach mit SoniTranslate!** 📽️

        Laden Sie ein Video, eine Audiodatei hoch oder geben Sie einen YouTube-Link an. 📽️ **Holen Sie sich das aktualisierte Notizbuch aus dem offiziellen Repository: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Sehen Sie sich den Tab `Hilfe` für Anweisungen zur Verwendung an. Fangen wir an, Spaß beim Übersetzen von Videos zu haben! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Anleitung zur Verwendung:**

        1. 📤 Laden Sie ein **Video**, eine **Audiodatei** hoch oder geben Sie einen 🌐 **YouTube-Link** an.

        2. 🌍 Wählen Sie die Sprache aus, in die Sie das **Video übersetzen möchten**.

        3. 🗣️ Geben Sie die **Anzahl der Sprecher im Video** an und **weisen Sie jedem einen Text-to-Speech-Stimme** zu, die für die Übersetzungssprache geeignet ist.

        4. 🚀 Drücken Sie die Schaltfläche '**Übersetzen**', um die Ergebnisse zu erhalten.

        ---

        # 🧩 **SoniTranslate unterstützt verschiedene TTS (Text-to-Speech)-Engines, darunter:**
        - EDGE-TTS → Format `en-AU-WilliamNeural-Male` → Schnell und präzise.
        - FACEBOOK MMS → Format `en-facebook-mms VITS` → Die Stimme ist natürlicher; derzeit nur CPU.
        - PIPER TTS → Format `en_US-lessac-high VITS-onnx` → Wie das vorherige, aber optimiert für CPU und GPU.
        - BARK → Format `en_speaker_0-Male BARK` → Gute Qualität, aber langsam und anfällig für Halluzinationen.
        - OpenAI TTS → Format `>alloy OpenAI-TTS` → Multisprachig, erfordert jedoch einen OpenAI API key
        - Coqui XTTS → Format `_XTTS_/AUTOMATIC.wav` → Nur verfügbar für Chinesisch (vereinfacht), Englisch, Französisch, Deutsch, Italienisch, Portugiesisch, Polnisch, Türkisch, Russisch, Niederländisch, Tschechisch, Arabisch, Spanisch, Ungarisch, Koreanisch und Japanisch.

        ---

        # 🎤 So verwenden Sie R.V.C. und R.V.C.2 Stimmen (optional) 🎶

        Das Ziel ist es, eine R.V.C. auf das generierte TTS (Text-to-Speech) anzuwenden 🎙️

        1. Laden Sie in der Registerkarte `Benutzerdefinierte Stimme R.V.C.` die Modelle herunter, die Sie benötigen 📥 Sie können Links von Hugging Face und Google Drive in Formaten wie zip, pth oder Index verwenden. Sie können auch komplette HF-Raum-Repositories herunterladen, aber diese Option ist nicht sehr stabil 😕

        2. Gehen Sie nun zu `Stimme ersetzen: TTS zu R.V.C.` und aktivieren Sie das Kontrollkästchen `aktivieren` ✅ Danach können Sie die Modelle auswählen, die Sie auf jeden TTS-Sprecher anwenden möchten 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Passen Sie die F0-Methode an, die auf alle R.V.C. angewendet wird. 🎛️

        4. Drücken Sie `KONFIGURATION ANWENDEN`, um die vorgenommenen Änderungen anzuwenden 🔄

        5. Gehen Sie zurück zum Tab für die Videoübersetzung und klicken Sie auf 'Übersetzen' ▶️ Jetzt wird die Übersetzung mit der R.V.C. angewendet. 🗣️

        Tipp: Sie können `Test R.V.C.` verwenden, um zu experimentieren und die besten TTS oder Konfigurationen zu finden, die auf die R.V.C. angewendet werden sollen. 🧪🔍

        ---

        """,
        "tab_translate": "Videotranslation",
        "video_source": "Wählen Sie die Videoquelle",
        "link_label": "Medienlink.",
        "link_info": "Beispiel: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL hier eingeben...",
        "dir_label": "Videopfad.",
        "dir_info": "Beispiel: /usr/home/my_video.mp4",
        "dir_ph": "Pfad hier eingeben...",
        "sl_label": "Ausgangssprache",
        "sl_info": "Dies ist die Originalsprache des Videos",
        "tat_label": "Audio übersetzen nach",
        "tat_info": "Wählen Sie die Zielsprache aus und stellen Sie sicher, dass Sie die entsprechende TTS für diese Sprache auswählen.",
        "num_speakers": "Wählen Sie, wie viele Personen im Video sprechen.",
        "min_sk": "Min Sprecher",
        "max_sk": "Max Sprecher",
        "tts_select": "Wählen Sie die Stimme für jeden Sprecher aus.",
        "sk1": "TTS-Sprecher 1",
        "sk2": "TTS-Sprecher 2",
        "sk3": "TTS-Sprecher 3",
        "sk4": "TTS-Sprecher 4",
        "sk5": "TTS-Sprecher 5",
        "sk6": "TTS-Sprecher 6",
        "sk7": "TTS-Sprecher 7",
        "sk8": "TTS-Sprecher 8",
        "sk9": "TTS-Sprecher 9",
        "sk10": "TTS-Sprecher 10",
        "sk11": "TTS-Sprecher 11",
        "sk12": "TTS-Sprecher 12",
        "vc_title": "Stimmenimitation in verschiedenen Sprachen",
        "vc_subtitle": """
        ### Reproduzieren Sie die Stimme einer Person in verschiedenen Sprachen.
        Obwohl es bei den meisten Stimmen wirksam ist, kann es nicht in jedem Fall perfekt sein.
        Die Stimmenimitation repliziert ausschließlich den Ton des Referenzsprechers und schließt Akzent und Emotion aus, die durch das TTS-Modell des Basis-Sprechers gesteuert werden und nicht vom Konverter repliziert werden.
        Es werden Audioaufnahmen aus dem Hauptaudio für jeden Sprecher entnommen und verarbeitet.
        """,
        "vc_active_label": "Aktive Stimmenimitation",
        "vc_active_info": "Aktive Stimmenimitation: Reproduziert den Ton des Originalsprechers",
        "vc_method_label": "Methode",
        "vc_method_info": "Wählen Sie eine Methode für den Stimmenimitationsprozess aus",
        "vc_segments_label": "Max Proben",
        "vc_segments_info": "Max Proben: Ist die Anzahl der Audioaufnahmen, die für den Prozess generiert werden, mehr ist besser, aber es kann Lärm hinzufügen",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Wendet vokalen Dereverb auf die Audioaufnahmen an.",
        "vc_remove_label": "Vorherige Proben entfernen",
        "vc_remove_info": "Vorherige Proben entfernen: Entfernt die zuvor generierten Proben, sodass neue erstellt werden müssen.",
        "xtts_title": "Erstellen Sie ein TTS basierend auf einem Audio",
        "xtts_subtitle": "Laden Sie eine Audiodatei von maximal 10 Sekunden mit einer Stimme hoch. Mit XTTS wird ein neues TTS mit einer Stimme ähnlich der bereitgestellten Audiodatei erstellt.",
        "xtts_file_label": "Laden Sie eine kurze Audio mit der Stimme hoch",
        "xtts_name_label": "Name für das TTS",
        "xtts_name_info": "Verwenden Sie einen einfachen Namen",
        "xtts_dereverb_label": "Dereverb-Audio",
        "xtts_dereverb_info": "Dereverb-Audio: Wendet vokalen Dereverb auf die Audioaufnahme an",
        "xtts_button": "Verarbeiten Sie das Audio und fügen Sie es dem TTS-Auswähler hinzu",
        "xtts_footer": "Generieren Sie Stimme xtts automatisch: Sie können `_XTTS_/AUTOMATIC.wav` im TTS-Auswähler verwenden, um automatisch Segmente für jeden Sprecher zu generieren, wenn die Übersetzung generiert wird.",
        "extra_setting": "Erweiterte Einstellungen",
        "acc_max_label": "Max Audiobeschleunigung",
        "acc_max_info": "Maximale Beschleunigung für übersetzte Audiosegmente, um Überlappungen zu vermeiden. Ein Wert von 1,0 repräsentiert keine Beschleunigung",
        "acc_rate_label": "Beschleunigungsrate-Regelung",
        "acc_rate_info": "Beschleunigungsrate-Regelung: Passt die Beschleunigung an, um Segmente mit weniger Geschwindigkeit anzupassen, um die Kontinuität zu erhalten und den Zeitpunkt des nächsten Starts zu berücksichtigen.",
        "or_label": "Überlappungsreduzierung",
        "or_info": "Überlappungsreduzierung: Stellt sicher, dass Segmente sich nicht überschneiden, indem Startzeiten auf Grundlage vorheriger Endzeiten angepasst werden; könnte die Synchronisierung stören.",
        "aud_mix_label": "Audio-Mixing-Methode",
        "aud_mix_info": "Mischen Sie Original- und übersetzte Audiodateien, um eine individuelle, ausgewogene Ausgabe mit zwei verfügbaren Mischmodi zu erstellen.",
        "vol_ori": "Lautstärke des Originaltons",
        "vol_tra": "Lautstärke des übersetzten Tons",
        "voiceless_tk_label": "Stimmenloses Track",
        "voiceless_tk_info": "Stimmenloses Track: Entfernen Sie die Original-Audio-Stimmen, bevor Sie sie mit dem übersetzten Audio kombinieren.",
        "sub_type": "Untertiteltyp",
        "soft_subs_label": "Weiche Untertitel",
        "soft_subs_info": "Weiche Untertitel: Optionale Untertitel, die Zuschauer während des Videostreamings ein- oder ausschalten können.",
        "burn_subs_label": "Untertitel einbetten",
        "burn_subs_info": "Untertitel einbetten: Untertitel in das Video einbetten und somit zu einem festen Bestandteil des visuellen Inhalts machen.",
        "whisper_title": "Konfiguration Transkription.",
        "lnum_label": "Zahlen Literalisieren",
        "lnum_info": "Zahlen Literalisieren: Ersetzen numerischer Darstellungen durch ihre geschriebenen Äquivalente in der Transkription.",
        "scle_label": "Tonbereinigung",
        "scle_info": "Tonbereinigung: Verbesserung der Stimme, Entfernen von Hintergrundgeräuschen vor der Transkription für maximale Zeitstempelgenauigkeit. Diese Operation kann Zeit in Anspruch nehmen, insbesondere bei längeren Audiodateien.",
        "sd_limit_label": "Segmentdauerbegrenzung",
        "sd_limit_info": "Geben Sie die maximale Dauer (in Sekunden) für jeden Abschnitt an. Der Ton wird unter Verwendung von VAD verarbeitet, wobei die Dauer für jeden Segmentabschnitt begrenzt wird.",
        "asr_model_info": "Es wandelt gesprochene Sprache standardmäßig mit dem 'Whisper'-Modell in Text um. Verwenden Sie ein benutzerdefiniertes Modell, indem Sie beispielsweise den Repository-Namen 'BELLE-2/Belle-whisper-large-v3-zh' im Dropdown-Menü eingeben, um ein chinesisches Sprachmodell zu verwenden. Finden Sie feinabgestimmte Modelle auf Hugging Face.",
        "ctype_label": "Berechnungstyp",
        "ctype_info": "Die Auswahl kleinerer Typen wie int8 oder float16 kann die Leistung verbessern, indem der Speicherverbrauch reduziert und die Rechenleistung erhöht wird, kann jedoch im Vergleich zu größeren Datentypen wie float32 an Präzision verlieren.",
        "batchz_label": "Batch-Größe",
        "batchz_info": "Die Reduzierung der Batch-Größe spart Speicherplatz, wenn Ihre GPU weniger VRAM hat, und hilft bei der Verwaltung von Out-of-Memory-Problemen.",
        "tsscale_label": "Textsegmentierungsskala",
        "tsscale_info": "Teilen Sie den Text in Segmente nach Sätzen, Wörtern oder Zeichen auf. Die Segmentierung nach Wörtern und Zeichen bietet eine feinere Granularität, die für Untertitel nützlich ist. Das Deaktivieren der Übersetzung erhält die Originalstruktur.",
        "srt_file_label": "Laden Sie eine SRT-Untertiteldatei hoch (wird anstelle der Transkription von Whisper verwendet)",
        "divide_text_label": "Textsegmente neu aufteilen nach:",
        "divide_text_info": "(Experimentell) Geben Sie einen Separator ein, um vorhandene Textsegmente in der Ausgangssprache aufzuteilen. Das Tool erkennt Vorkommen und erstellt entsprechend neue Segmente. Geben Sie mehrere Trennzeichen mit | an, z. B.: !|?|...|。",
        "diarization_label": "Diarisierungsmodell",
        "tr_process_label": "Übersetzungsprozess",
        "out_type_label": "Ausgabetyp",
        "out_name_label": "Dateiname",
        "out_name_info": "Der Name der Ausgabedatei",
        "task_sound_label": "Aufgabenstatus-Sound",
        "task_sound_info": "Aufgabenstatus-Sound: Gibt einen akustischen Hinweis auf den Abschluss der Aufgabe oder Fehler während der Ausführung.",
        "cache_label": "Fortschritt abrufen",
        "cache_info": "Fortschritt abrufen: Fortfahren vom letzten Kontrollpunkt.",
        "preview_info": "Die Vorschau schneidet das Video zu Testzwecken auf nur 10 Sekunden. Deaktivieren Sie es bitte, um die volle Videodauer abzurufen.",
        "edit_sub_label": "Generierte Untertitel bearbeiten",
        "edit_sub_info": "Generierte Untertitel bearbeiten: Ermöglicht Ihnen, die Übersetzung in 2 Schritten durchzuführen. Zuerst mit der Schaltfläche 'UNTERTEITEL BEKOMMEN UND BEARBEITEN' erhalten Sie die Untertitel, um sie zu bearbeiten, und dann mit der Schaltfläche 'ÜBERSETZEN' können Sie das Video generieren",
        "button_subs": "UNTERTEITEL BEKOMMEN UND BEARBEITEN",
        "editor_sub_label": "Generierte Untertitel",
        "editor_sub_info": "Bearbeiten Sie den Text in den generierten Untertiteln hier. Sie können Änderungen an den Schnittstellenoptionen vornehmen, bevor Sie auf die Schaltfläche 'ÜBERSETZEN' klicken, außer 'Ausgangssprache', 'Audio übersetzen nach' und 'Max Sprecher', um Fehler zu vermeiden. Wenn Sie fertig sind, klicken Sie auf die Schaltfläche 'ÜBERSETZEN'.",
        "editor_sub_ph": "Drücken Sie zuerst 'UNTERTEITEL BEKOMMEN UND BEARBEITEN', um die Untertitel zu erhalten",
        "button_translate": "ÜBERSETZEN",
        "output_result_label": "ÜBERSETZTES VIDEO HERUNTERLADEN",
        "sub_ori": "Untertitel",
        "sub_tra": "Übersetzte Untertitel",
        "ht_token_info": "Ein wichtiger Schritt besteht darin, die Lizenzvereinbarung für die Verwendung von Pyannote zu akzeptieren. Sie müssen ein Konto bei Hugging Face haben und die Lizenz akzeptieren, um die Modelle zu verwenden: https://huggingface.co/pyannote/speaker-diarization und https://huggingface.co/pyannote/segmentation. Holen Sie sich hier Ihren SCHLÜSSELTOKEN: https://hf.co/settings/tokens",
        "ht_token_ph": "Token hier eingeben...",
        "tab_docs": "Dokumentübersetzung",
        "docs_input_label": "Dokumentquelle auswählen",
        "docs_input_info": "Es kann PDF, DOCX, TXT oder Text sein",
        "docs_source_info": "Dies ist die Originalsprache des Textes",
        "chunk_size_label": "Maximale Anzahl von Zeichen, die der TTS pro Segment verarbeiten soll",
        "chunk_size_info": "Ein Wert von 0 weist einen dynamischen und kompatibleren Wert für den TTS zu.",
        "docs_button": "Starten Sie die Sprachkonvertierung Bridge",
        "cv_url_info": "Laden Sie die R.V.C.-Modelle automatisch von der URL herunter. Sie können Links von HuggingFace oder Drive verwenden und mehrere Links, jeweils durch ein Komma getrennt, einfügen. Beispiel: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Stimme ersetzen: TTS zu R.V.C.",
        "sec1_title": "### 1. Um seine Verwendung zu aktivieren, markieren Sie es als aktiv.",
        "enable_replace": "Aktivieren Sie dies, um die Verwendung der Modelle zu ermöglichen.",
        "sec2_title": "### 2. Wählen Sie eine Stimme aus, die auf jeden TTS jedes entsprechenden Sprechers angewendet wird, und wenden Sie die Konfigurationen an.",
        "sec2_subtitle": "Je nachdem, wie viele <TTS-Sprecher> Sie verwenden werden, benötigt jeder sein entsprechendes Modell. Außerdem gibt es ein Hilfsmodell, falls der Sprecher aus irgendeinem Grund nicht korrekt erkannt wird.",
        "cv_tts1": "Wählen Sie die Stimme für Sprecher 1 aus.",
        "cv_tts2": "Wählen Sie die Stimme für Sprecher 2 aus.",
        "cv_tts3": "Wählen Sie die Stimme für Sprecher 3 aus.",
        "cv_tts4": "Wählen Sie die Stimme für Sprecher 4 aus.",
        "cv_tts5": "Wählen Sie die Stimme für Sprecher 5 aus.",
        "cv_tts6": "Wählen Sie die Stimme für Sprecher 6 aus.",
        "cv_tts7": "Wählen Sie die Stimme für Sprecher 7 aus.",
        "cv_tts8": "Wählen Sie die Stimme für Sprecher 8 aus.",
        "cv_tts9": "Wählen Sie die Stimme für Sprecher 9 aus.",
        "cv_tts10": "Wählen Sie die Stimme für Sprecher 10 aus.",
        "cv_tts11": "Wählen Sie die Stimme für Sprecher 11 aus.",
        "cv_tts12": "Wählen Sie die Stimme für Sprecher 12 aus.",
        "cv_aux": "- Stimme, die angewendet wird, falls ein Sprecher nicht erfolgreich erkannt wird.",
        "cv_button_apply": "KONFIGURATION ANWENDEN",
        "tab_help": "Hilfe",
    },
    "italian": {
        "description": """
        ### 🎥 **Traduci i video facilmente con SoniTranslate!** 📽️

        Carica un video, un file audio o fornisci un link YouTube. 📽️ **Ottieni il notebook aggiornato dal repository ufficiale: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Consulta la scheda `Aiuto` per istruzioni su come utilizzarlo. Iniziamo a divertirci con la traduzione dei video! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Istruzioni per l'uso:**

        1. 📤 Carica un **video**, un **file audio** o fornisci un 🌐 **link YouTube**.

        2. 🌍 Scegli la lingua in cui desideri **tradurre il video**.

        3. 🗣️ Specifica il **numero di persone che parlano** nel video e **assegna a ciascuna una voce di sintesi vocale** adatta alla lingua di traduzione.

        4. 🚀 Premi il pulsante '**Traduci**' per ottenere i risultati.

        ---

        # 🧩 **SoniTranslate supporta diversi motori TTS (Text-to-Speech), tra cui:**
        - EDGE-TTS → formato `en-AU-WilliamNeural-Male` → Veloce e preciso.
        - FACEBOOK MMS → formato `en-facebook-mms VITS` → La voce è più naturale; al momento utilizza solo la CPU.
        - PIPER TTS → formato `en_US-lessac-high VITS-onnx` → Come il precedente, ma ottimizzato sia per CPU che GPU.
        - BARK → formato `en_speaker_0-Male BARK` → Buona qualità ma lenta e soggetta ad allucinazioni.
        - OpenAI TTS → formato `>alloy OpenAI-TTS` → Multilingue ma richiede una OpenAI API key.
        - Coqui XTTS → formato `_XTTS_/AUTOMATIC.wav` → Disponibile solo per cinese (semplificato), inglese, francese, tedesco, italiano, portoghese, polacco, turco, russo, olandese, ceco, arabo, spagnolo, ungherese, coreano e giapponese.

        ---

        # 🎤 Come utilizzare le voci R.V.C. e R.V.C.2 (Opzionale) 🎶

        L'obiettivo è applicare un R.V.C. al TTS (Text-to-Speech) generato 🎙️

        1. Nella scheda `Custom Voice R.V.C.`, scarica i modelli di cui hai bisogno 📥 Puoi utilizzare link da Hugging Face e Google Drive in formati come zip, pth o indice. Puoi anche scaricare repository completi di spazio HF, ma questa opzione non è molto stabile 😕

        2. Ora, vai su `Sostituisci voce: TTS a R.V.C.` e spunta la casella `abilita` ✅ Dopo questo, puoi scegliere i modelli che desideri applicare a ciascun altoparlante TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Regola il metodo F0 che verrà applicato a tutti i R.V.C. 🎛️

        4. Premi `APPLICA CONFIGURAZIONE` per applicare le modifiche apportate 🔄

        5. Torna alla scheda di traduzione video e clicca su 'Traduci' ▶️ Ora, la traduzione verrà effettuata applicando il R.V.C. 🗣️

        Suggerimento: Puoi utilizzare `Test R.V.C.` per sperimentare e trovare il miglior TTS o configurazioni da applicare al R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Traduzione video",
        "video_source": "Scegli la fonte video",
        "link_label": "Link multimediale.",
        "link_info": "Esempio: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "Inserisci l'URL qui...",
        "dir_label": "Percorso video.",
        "dir_info": "Esempio: /usr/home/mio_video.mp4",
        "dir_ph": "Inserisci il percorso qui...",
        "sl_label": "Lingua di origine",
        "sl_info": "Questa è la lingua originale del video",
        "tat_label": "Traduci l'audio in",
        "tat_info": "Seleziona la lingua di destinazione e assicurati anche di scegliere il TTS corrispondente per quella lingua.",
        "num_speakers": "Seleziona quanti parlano nel video.",
        "min_sk": "Numero minimo di altoparlanti",
        "max_sk": "Numero massimo di altoparlanti",
        "tts_select": "Seleziona la voce desiderata per ogni altoparlante.",
        "sk1": "Altoparlante TTS 1",
        "sk2": "Altoparlante TTS 2",
        "sk3": "Altoparlante TTS 3",
        "sk4": "Altoparlante TTS 4",
        "sk5": "Altoparlante TTS 5",
        "sk6": "Altoparlante TTS 6",
        "sk7": "Altoparlante TTS 7",
        "sk8": "Altoparlante TTS 8",
        "sk9": "Altoparlante TTS 9",
        "sk10": "Altoparlante TTS 10",
        "sk11": "Altoparlante TTS 11",
        "sk12": "Altoparlante TTS 12",
        "vc_title": "Imitazione della voce in diverse lingue",
        "vc_subtitle": """
        ### Replica la voce di una persona in varie lingue.
        Sebbene efficace con la maggior parte delle voci quando usato correttamente, potrebbe non raggiungere la perfezione in ogni caso.
        L'imitazione della voce replica esclusivamente il tono del locutore di riferimento, escludendo accento ed emozione, che sono governati dal modello TTS del locutore di base e non replicati dal convertitore.
        Questo prenderà campioni audio dall'audio principale per ciascun altoparlante e li elaborerà.
        """,
        "vc_active_label": "Imitazione attiva della voce",
        "vc_active_info": "Imitazione attiva della voce: Replica il tono del locutore originale",
        "vc_method_label": "Metodo",
        "vc_method_info": "Seleziona un metodo per il processo di imitazione della voce",
        "vc_segments_label": "Campioni massimi",
        "vc_segments_info": "Campioni massimi: è il numero di campioni audio che verranno generati per il processo, più è meglio ma può aggiungere rumore",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Applica dereverb vocale ai campioni audio.",
        "vc_remove_label": "Rimuovi campioni precedenti",
        "vc_remove_info": "Rimuovi campioni precedenti: Rimuove i campioni precedenti generati, quindi è necessario crearne di nuovi.",
        "xtts_title": "Crea un TTS basato su un audio",
        "xtts_subtitle": "Carica un file audio di massimo 10 secondi con una voce. Utilizzando XTTS, verrà creato un nuovo TTS con una voce simile al file audio fornito.",
        "xtts_file_label": "Carica un breve audio con la voce",
        "xtts_name_label": "Nome per il TTS",
        "xtts_name_info": "Utilizza un nome semplice",
        "xtts_dereverb_label": "Dereverb audio",
        "xtts_dereverb_info": "Dereverb audio: Applica dereverb vocale all'audio",
        "xtts_button": "Elabora l'audio e includilo nel selettore TTS",
        "xtts_footer": "Genera automaticamente XTTS vocale: Puoi usare `_XTTS_/AUTOMATIC.wav` nel selettore TTS per generare automaticamente segmenti per ciascun altoparlante durante la generazione della traduzione.",
        "extra_setting": "Impostazioni avanzate",
        "acc_max_label": "Massima accelerazione audio",
        "acc_max_info": "Massima accelerazione per i segmenti audio tradotti per evitare sovrapposizioni. Un valore di 1,0 rappresenta nessuna accelerazione",
        "acc_rate_label": "Regolazione del tasso di accelerazione",
        "acc_rate_info": "Regolazione del tasso di accelerazione: Regola l'accelerazione per adattarsi ai segmenti che richiedono una velocità inferiore, mantenendo la continuità e considerando il timing di avvio successivo.",
        "or_label": "Riduzione Sovrapposizione",
        "or_info": "Riduzione Sovrapposizione: Assicura che i segmenti non si sovrappongano regolando gli orari di inizio in base agli orari di fine precedenti; potrebbe interrompere la sincronizzazione.",
        "aud_mix_label": "Metodo di mixing audio",
        "aud_mix_info": "Mixa file audio originali e tradotti per creare un output personalizzato e bilanciato con due modalità di mixing disponibili.",
        "vol_ori": "Volume audio originale",
        "vol_tra": "Volume audio tradotto",
        "voiceless_tk_label": "Traccia senza voce",
        "voiceless_tk_info": "Traccia senza voce: Rimuove le voci audio originali prima di combinarle con l'audio tradotto.",
        "sub_type": "Tipo di sottotitolo",
        "soft_subs_label": "Sottotitoli Soft",
        "soft_subs_info": "Sottotitoli Soft: Sottotitoli opzionali che gli spettatori possono attivare o disattivare durante la visione del video.",
        "burn_subs_label": "Incorpora sottotitoli",
        "burn_subs_info": "Incorpora sottotitoli: Incorpora i sottotitoli nel video, rendendoli una parte permanente del contenuto visivo.",
        "whisper_title": "Configura la trascrizione.",
        "lnum_label": "Literalizzare Numeri",
        "lnum_info": "Literalizzare Numeri: Sostituisci le rappresentazioni numeriche con i loro equivalenti scritti nella trascrizione.",
        "scle_label": "Pulizia del Suono",
        "scle_info": "Pulizia del Suono: Migliora le voci, rimuovi il rumore di fondo prima della trascrizione per una massima precisione dei timestamp. Questa operazione può richiedere del tempo, specialmente con file audio lunghi.",
        "sd_limit_label": "Limite Durata Segmento",
        "sd_limit_info": "Specifica la durata massima (in secondi) per ogni segmento. L'audio verrà elaborato utilizzando VAD, limitando la durata per ciascun frammento di segmento.",
        "asr_model_info": "Converte il linguaggio parlato in testo utilizzando il modello 'Whisper' per impostazione predefinita. Utilizza un modello personalizzato, ad esempio, inserendo il nome del repository 'BELLE-2/Belle-whisper-large-v3-zh' nel menu a discesa per utilizzare un modello pre-ottimizzato in cinese. Trova modelli pre-ottimizzati su Hugging Face.",
        "ctype_label": "Tipo di Calcolo",
        "ctype_info": "Scegliere tipi più piccoli come int8 o float16 può migliorare le prestazioni riducendo l'utilizzo della memoria e aumentando il throughput computazionale, ma può sacrificare la precisione rispetto a tipi di dati più grandi come float32.",
        "batchz_label": "Dimensione Batch",
        "batchz_info": "Ridurre la dimensione del batch consente di risparmiare memoria se la tua GPU ha meno VRAM e aiuta a gestire i problemi di memoria esaurita.",
        "tsscale_label": "Scala di Segmentazione del Testo",
        "tsscale_info": "Dividi il testo in segmenti per frasi, parole o caratteri. La segmentazione per parole e caratteri offre una granularità più fine, utile per i sottotitoli; disabilitare la traduzione conserva la struttura originale.",
        "srt_file_label": "Carica un file sottotitoli SRT (verrà utilizzato al posto della trascrizione di Whisper)",
        "divide_text_label": "Ridividi i segmenti di testo per:",
        "divide_text_info": "(Sperimentale) Inserisci un separatore per dividere i segmenti di testo esistenti nella lingua di origine. Lo strumento identificherà le occorrenze e creerà nuovi segmenti di conseguenza. Specifica più separatori usando |, ad esempio: !|?|...|。",
        "diarization_label": "Modello di diarizzazione",
        "tr_process_label": "Processo di traduzione",
        "out_type_label": "Tipo di output",
        "out_name_label": "Nome del file",
        "out_name_info": "Il nome del file di output",
        "task_sound_label": "Suono dello stato del compito",
        "task_sound_info": "Suono dello stato del compito: Riproduce un segnale acustico che indica il completamento del compito o gli errori durante l'esecuzione.",
        "cache_label": "Recupero Progresso",
        "cache_info": "Recupero Progresso: Continua il processo dall'ultimo checkpoint.",
        "preview_info": "La preview taglia il video a soli 10 secondi per scopi di test. Disattivala per ripristinare la durata completa del video.",
        "edit_sub_label": "Modifica i sottotitoli generati",
        "edit_sub_info": "Modifica i sottotitoli generati: Ti consente di eseguire la traduzione in 2 passaggi. Prima con il pulsante 'OTTIENI SOTTOTITOLI E MODIFICA', ottieni i sottotitoli per modificarli, e poi con il pulsante 'TRADUCI', puoi generare il video",
        "button_subs": "OTTIENI SOTTOTITOLI E MODIFICA",
        "editor_sub_label": "Sottotitoli generati",
        "editor_sub_info": "Modifica il testo nei sottotitoli generati qui. Puoi apportare modifiche alle opzioni dell'interfaccia prima di fare clic sul pulsante 'TRADUCI', ad eccezione di 'Lingua di origine', 'Traduci l'audio in' e 'Numero massimo di altoparlanti', per evitare errori. Una volta finito, fai clic sul pulsante 'TRADUCI'.",
        "editor_sub_ph": "Prima premi 'OTTIENI SOTTOTITOLI E MODIFICA' per ottenere i sottotitoli",
        "button_translate": "TRADUCI",
        "output_result_label": "SCARICA VIDEO TRADOTTO",
        "sub_ori": "Sottotitoli",
        "sub_tra": "Sottotitoli tradotti",
        "ht_token_info": "Un passaggio importante è accettare l'accordo di licenza per l'uso di Pyannote. È necessario avere un account su Hugging Face e accettare la licenza per utilizzare i modelli: https://huggingface.co/pyannote/speaker-diarization e https://huggingface.co/pyannote/segmentation. Ottieni il tuo TOKEN CHIAVE qui: https://hf.co/settings/tokens",
        "ht_token_ph": "Inserisci il token qui...",
        "tab_docs": "Traduzione documenti",
        "docs_input_label": "Scegli la fonte del documento",
        "docs_input_info": "Può essere PDF, DOCX, TXT o testo",
        "docs_source_info": "Questa è la lingua originale del testo",
        "chunk_size_label": "Numero massimo di caratteri che il TTS elaborerà per segmento",
        "chunk_size_info": "Un valore di 0 assegna un valore dinamico e più compatibile per il TTS.",
        "docs_button": "Avvia ponte di conversione linguistica",
        "cv_url_info": "Scarica automaticamente i modelli R.V.C. dall'URL. Puoi utilizzare link da HuggingFace o Drive e puoi includere diversi link, ognuno separato da una virgola. Esempio: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Sostituisci voce: TTS a R.V.C.",
        "sec1_title": "### 1. Per abilitarne l'uso, contrassegnalo come abilitato.",
        "enable_replace": "Seleziona questa opzione per abilitare l'uso dei modelli.",
        "sec2_title": "### 2. Seleziona una voce che verrà applicata a ciascun TTS di ciascun altoparlante corrispondente e applica le configurazioni.",
        "sec2_subtitle": "A seconda di quanti <Altoparlante TTS> utilizzerai, ognuno avrà bisogno del proprio modello. Inoltre, c'è un modello ausiliario nel caso in cui il parlante non venga rilevato correttamente.",
        "cv_tts1": "Scegli la voce da applicare per l'Altoparlante 1.",
        "cv_tts2": "Scegli la voce da applicare per l'Altoparlante 2.",
        "cv_tts3": "Scegli la voce da applicare per l'Altoparlante 3.",
        "cv_tts4": "Scegli la voce da applicare per l'Altoparlante 4.",
        "cv_tts5": "Scegli la voce da applicare per l'Altoparlante 5.",
        "cv_tts6": "Scegli la voce da applicare per l'Altoparlante 6.",
        "cv_tts7": "Scegli la voce da applicare per l'Altoparlante 7.",
        "cv_tts8": "Scegli la voce da applicare per l'Altoparlante 8.",
        "cv_tts9": "Scegli la voce da applicare per l'Altoparlante 9.",
        "cv_tts10": "Scegli la voce da applicare per l'Altoparlante 10.",
        "cv_tts11": "Scegli la voce da applicare per l'Altoparlante 11.",
        "cv_tts12": "Scegli la voce da applicare per l'Altoparlante 12.",
        "cv_aux": "- Voce da applicare nel caso in cui un altoparlante non venga rilevato correttamente.",
        "cv_button_apply": "APPLICA CONFIGURAZIONE",
        "tab_help": "Aiuto",
    },
    "japanese": {
        "description": """
        ### 🎥 **SoniTranslateで簡単に動画を翻訳しましょう！** 📽️

        動画、音声ファイルをアップロードするか、YouTubeのリンクを提供してください。📽️ **公式リポジトリから最新のノートブックを入手する: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        使用方法についての指示は`ヘルプ`タブを参照してください。動画翻訳を楽しんでみましょう！ 🚀🎉
        """,
        "tutorial": """
        # 🔰 **使用方法:**

        1. 📤 **動画**、**音声ファイル**をアップロードするか、🌐 **YouTubeのリンク**を提供します。

        2. 🌍 **動画を翻訳する言語**を選択します。

        3. 🗣️ **動画内の話者の数**を指定し、それぞれの話者に翻訳言語に適したテキスト読み上げ音声を割り当てます。

        4. 🚀 '**翻訳**'ボタンを押して結果を取得します。

        ---

        # 🧩 **SoniTranslateはさまざまなTTS（テキスト読み上げ）エンジンをサポートしています。これらは次のとおりです:**
        - EDGE-TTS → 形式 `en-AU-WilliamNeural-Male` → 速く正確です。
        - FACEBOOK MMS → 形式 `en-facebook-mms VITS` → 音声がより自然です。現時点ではCPUのみを使用します。
        - PIPER TTS → 形式 `en_US-lessac-high VITS-onnx` → 前述のものと同じですが、CPUとGPUの両方に最適化されています。
        - BARK → 形式 `en_speaker_0-Male BARK` → 品質は良好ですが、遅く、幻覚に陥りやすいです。
        - OpenAI TTS → フォーマット `>alloy OpenAI-TTS` → 多言語対応ですが、OpenAIのAPIキーが必要です
        - Coqui XTTS → 形式 `_XTTS_/AUTOMATIC.wav` → 中国語（簡体字）、英語、フランス語、ドイツ語、イタリア語、ポルトガル語、ポーランド語、トルコ語、ロシア語、オランダ語、チェコ語、アラビア語、スペイン語、ハンガリー語、韓国語、日本語のみ利用可能です。

        ---

        # 🎤 R.V.C.とR.V.C.2ボイスの使用方法（オプション） 🎶

        目標は、生成されたTTS（テキスト読み上げ）にR.V.C.を適用することです 🎙️

        1. `カスタムボイスR.V.C.`タブで、必要なモデルをダウンロードしてください 📥 Hugging FaceやGoogle Driveからのリンクを使用できます。zip、pth、またはindexなどの形式を使用できます。完全なHFスペースリポジトリをダウンロードすることもできますが、このオプションはあまり安定していません 😕

        2. 今度は、`TTSからR.V.C.への置換`に移動し、`有効`ボックスをチェックします ✅ これ以降、各TTSスピーカーに適用するモデルを選択できます 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. すべてのR.V.C.に適用されるF0メソッドを調整します 🎛️

        4. 変更した設定を適用するには、`設定を適用`を押します 🔄

        5. 動画翻訳タブに戻り、「翻訳」をクリックします ▶️ これで、R.V.C.を適用して翻訳が行われます 🗣️

        ヒント: `テストR.V.C.`を使用して、適用する最適なTTSまたは設定を実験し、見つけることができます 🧪🔍

        ---

        """,
        "tab_translate": "動画翻訳",
        "video_source": "動画ソースを選択",
        "link_label": "メディアリンク。",
        "link_info": "例: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URLをここに入力...",
        "dir_label": "ビデオパス。",
        "dir_info": "例: /usr/home/my_video.mp4",
        "dir_ph": "パスをここに入力...",
        "sl_label": "元の言語",
        "sl_info": "動画の元の言語です",
        "tat_label": "翻訳先の言語",
        "tat_info": "対象言語を選択し、その言語に対応するTTSを選択することも忘れないでください。",
        "num_speakers": "ビデオ内の話者の数を選択してください。",
        "min_sk": "最小スピーカー",
        "max_sk": "最大スピーカー",
        "tts_select": "各スピーカーに適した音声を選択してください。",
        "sk1": "TTSスピーカー1",
        "sk2": "TTSスピーカー2",
        "sk3": "TTSスピーカー3",
        "sk4": "TTSスピーカー4",
        "sk5": "TTSスピーカー5",
        "sk6": "TTSスピーカー6",
        "sk7": "TTSスピーカー7",
        "sk8": "TTSスピーカー8",
        "sk9": "TTSスピーカー9",
        "sk10": "TTSスピーカー10",
        "sk11": "TTSスピーカー11",
        "sk12": "TTSスピーカー12",
        "vc_title": "異なる言語での音声模倣",
        "vc_subtitle": """
        ### さまざまな言語で人の声を再現します。
        適切に使用されるとほとんどの声に効果的ですが、すべての場合に完璧な結果が得られるわけではありません。
        音声模倣は、アクセントや感情を除く参照スピーカーの音色のみを再現し、これらは基本スピーカーTTSモデルによって制御され、変換器によっては再現されません。
        これにより、各話者のメインオーディオからオーディオサンプルを取得し、処理します。
        """,
        "vc_active_label": "アクティブ音声模倣",
        "vc_active_info": "アクティブ音声模倣：元のスピーカーの音色を再現します",
        "vc_method_label": "メソッド",
        "vc_method_info": "音声模倣プロセスのメソッドを選択します",
        "vc_segments_label": "最大サンプル数",
        "vc_segments_info": "最大サンプル数：プロセスに使用されるオーディオサンプルの数。より多いほど良いですが、ノイズが発生する可能性があります",
        "vc_dereverb_label": "リバーブを除去",
        "vc_dereverb_info": "リバーブを除去：オーディオサンプルにボーカルリバーブを適用します。",
        "vc_remove_label": "以前のサンプルを削除",
        "vc_remove_info": "以前のサンプルを削除：以前に生成されたサンプルを削除し、新しいサンプルを作成する必要があります。",
        "xtts_title": "オーディオを基にTTSを作成する",
        "xtts_subtitle": "声が入った最大10秒のオーディオファイルをアップロードします。 XTTSを使用すると、提供されたオーディオファイルに似た声で新しいTTSが作成されます。",
        "xtts_file_label": "声の入った短いオーディオをアップロードしてください",
        "xtts_name_label": "TTSの名前",
        "xtts_name_info": "簡単な名前を使用してください",
        "xtts_dereverb_label": "オーディオのリバーブを除去",
        "xtts_dereverb_info": "オーディオのリバーブを除去：オーディオにボーカルリバーブを適用します",
        "xtts_button": "オーディオを処理してTTSセレクタに含めます",
        "xtts_footer": "音声xttsを自動生成する：翻訳を生成する際に各話者のセグメントを自動生成するために、TTSセレクタで`_XTTS_/AUTOMATIC.wav`を使用できます。",
        "extra_setting": "高度な設定",
        "acc_max_label": "最大オーディオ加速度",
        "acc_max_info": "オーバーラップを回避するための翻訳されたオーディオセグメントの最大加速度。値が1.0の場合、加速度はありません",
        "acc_rate_label": "加速度調整",
        "acc_rate_info": "加速度調整：速度が低いセグメントに適応するために加速度を調整し、連続性を保ち、次の開始時刻を考慮します。",
        "or_label": "重複削減",
        "or_info": "重複削減：前の終了時間に基づいて開始時間を調整してセグメントが重複しないようにします。同期を妨げる可能性があります。",
        "aud_mix_label": "オーディオミキシング方法",
        "aud_mix_info": "オリジナルと翻訳されたオーディオファイルを混合してカスタマイズされたバランスの取れた出力を作成するための2つの利用可能なミキシングモード。",
        "vol_ori": "元のオーディオの音量",
        "vol_tra": "翻訳されたオーディオの音量",
        "voiceless_tk_label": "声なしトラック",
        "voiceless_tk_info": "声なしトラック：翻訳されたオーディオと組み合わせる前に元のオーディオの音声を削除します。",
        "sub_type": "字幕タイプ",
        "soft_subs_label": "ソフトサブタイトル",
        "soft_subs_info": "ソフトサブタイトル：視聴者がビデオを見ながらオンまたはオフにできるオプションの字幕。",
        "burn_subs_label": "字幕を焼く",
        "burn_subs_info": "字幕を焼く：字幕をビデオに埋め込み、それを視覚コンテンツの恒久的な一部にします。",
        "whisper_title": "トランスクリプションの構成。",
        "lnum_label": "数値の表現化",
        "lnum_info": "数値の表現化：トランスクリプト内の数値表現を書き換えて、数値を文字列に変換します。",
        "scle_label": "音声のクリーンアップ",
        "scle_info": "音声のクリーンアップ：トランスクリプトの時間スタンプの精度を最大限に高めるために、ボーカルを強調し、背景ノイズを除去します。この操作には時間がかかる場合があります。特に長時間のオーディオファイルの場合。",
        "sd_limit_label": "セグメントの長さ制限",
        "sd_limit_info": "各セグメントの最大長（秒単位）を指定します。オーディオはVADを使用して処理され、各セグメントチャンクの長さが制限されます。",
        "asr_model_info": "デフォルトでは、「Whisperモデル」を使用して、音声をテキストに変換します。カスタムモデルを使用するには、ドロップダウンでリポジトリ名「BELLE-2/Belle-whisper-large-v3-zh」を入力して、中国語の言語を微調整したモデルを利用します。 Hugging Faceで微調整されたモデルを見つけます。",
        "ctype_label": "計算タイプ",
        "ctype_info": "int8やfloat16などの小さなタイプを選択すると、メモリ使用量が減少し、計算スループットが増加してパフォーマンスが向上しますが、float32などの大きなデータタイプと比較して精度が低下する場合があります。",
        "batchz_label": "バッチサイズ",
        "batchz_info": "バッチサイズを減らすと、GPUのVRAMが少ない場合にメモリを節約し、メモリ不足の問題を管理するのに役立ちます。",
        "tsscale_label": "テキストのセグメンテーションスケール",
        "tsscale_info": "テキストを文、単語、または文字でセグメントに分割します。単語と文字のセグメンテーションは、字幕などの細かい粒度の処理に役立ちます。翻訳を無効にすると、元の構造が保持されます。",
        "srt_file_label": "SRT字幕ファイルをアップロードしてください（Whisperのトランスクリプションの代わりに使用されます）",
        "divide_text_label": "次のようにテキストセグメントを再分割します:",
        "divide_text_info": "(実験的) ソース言語の既存のテキストセグメントを分割するセパレーターを入力します。ツールは出現を識別し、適切な箇所で新しいセグメントを作成します。複数のセパレーターを | を使用して指定します。例: !|?|...|。",
        "diarization_label": "ダイアライゼーションモデル",
        "tr_process_label": "翻訳プロセス",
        "out_type_label": "出力タイプ",
        "out_name_label": "ファイル名",
        "out_name_info": "出力ファイルの名前",
        "task_sound_label": "タスクステータスサウンド",
        "task_sound_info": "タスクステータスサウンド：タスクの完了または実行中のエラーを示す音声アラートを再生します。",
        "cache_label": "進捗を取得",
        "cache_info": "進捗を取得：最後のチェックポイントからプロセスを継続します。",
        "preview_info": "テスト目的でビデオを10秒に切り取ります。完全なビデオの長さを取得するには、これを無効にしてください。",
        "edit_sub_label": "生成された字幕を編集",
        "edit_sub_info": "生成された字幕の翻訳を2段階で実行できます。まず、「字幕を取得して編集」ボタンをクリックして字幕を取得して編集し、次に「翻訳」ボタンをクリックしてビデオを生成できます。",
        "button_subs": "字幕を取得して編集",
        "editor_sub_label": "生成された字幕",
        "editor_sub_info": "ここで生成された字幕のテキストを自由に編集してください。エラーを回避するために、インターフェイスのオプションを変更する前に「元の言語」、「翻訳先の言語」、「最大スピーカー」を除く、[翻訳]ボタンをクリックしてください。編集が完了したら、「翻訳」ボタンをクリックします。",
        "editor_sub_ph": "まず、「字幕を取得して編集」を押して字幕を取得してください",
        "button_translate": "翻訳",
        "output_result_label": "翻訳された動画をダウンロード",
        "sub_ori": "字幕",
        "sub_tra": "翻訳された字幕",
        "ht_token_info": "重要なステップの1つは、Pyannoteのライセンス契約を受諾することです。これには、Hugging Faceにアカウントを持ち、モデルの使用許可を受け入れる必要があります: https://huggingface.co/pyannote/speaker-diarization および https://huggingface.co/pyannote/segmentation. ここでキー トークンを取得します: https://hf.co/settings/tokens",
        "ht_token_ph": "トークンをここに入力...",
        "tab_docs": "ドキュメント翻訳",
        "docs_input_label": "ドキュメントソースを選択",
        "docs_input_info": "PDF、DOCX、TXT、またはテキストである可能性があります",
        "docs_source_info": "これはテキストの元の言語です",
        "chunk_size_label": "TTSがセグメントごとに処理する最大文字数",
        "chunk_size_info": "値が0の場合、TTSに動的で互換性のある値が割り当てられます。",
        "docs_button": "言語変換ブリッジを開始",
        "cv_url_info": "URLからR.V.C.モデルを自動的にダウンロードします。HuggingFaceまたはドライブからのリンクを使用でき、各リンクをコンマで区切って複数のリンクを含めることができます。例: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "音声を置換: TTSからR.V.C.へ。",
        "sec1_title": "### 1. 使用を有効にするには、それを有効にします。",
        "enable_replace": "このオプションをチェックして、モデルの使用を有効にします。",
        "sec2_title": "### 2. 各対応する話者のTTSに適用される音声を選択し、設定を適用します。",
        "sec2_subtitle": "使用する<TTSスピーカー>の数に応じて、それぞれに対応するモデルが必要です。また、スピーカーが正しく検出されない場合のために補助的なモデルもあります。",
        "cv_tts1": "スピーカー1に適用する音声を選択してください。",
        "cv_tts2": "スピーカー2に適用する音声を選択してください。",
        "cv_tts3": "スピーカー3に適用する音声を選択してください。",
        "cv_tts4": "スピーカー4に適用する音声を選択してください。",
        "cv_tts5": "スピーカー5に適用する音声を選択してください。",
        "cv_tts6": "スピーカー6に適用する音声を選択してください。",
        "cv_tts7": "スピーカー7に適用する音声を選択してください。",
        "cv_tts8": "スピーカー8に適用する音声を選択してください。",
        "cv_tts9": "スピーカー9に適用する音声を選択してください。",
        "cv_tts10": "スピーカー10に適用する音声を選択してください。",
        "cv_tts11": "スピーカー11に適用する音声を選択してください。",
        "cv_tts12": "スピーカー12に適用する音声を選択してください。",
        "cv_aux": "- スピーカーが正常に検出されない場合に適用する音声。",
        "cv_button_apply": "設定を適用",
        "tab_help": "ヘルプ",
    },
    "chinese_zh_cn": {
        "description": """
          ### 🎥 **使用SoniTranslate轻松翻译视频！** 📽️

          上传视频、音频文件或提供YouTube链接。 📽️ **从官方存储库获取更新的笔记本：[SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

          查看`帮助`标签以获取如何使用的说明。让我们开始享受视频翻译的乐趣吧！ 🚀🎉
          """,
        "tutorial": """
          # 🔰 **使用说明:**

          1. 📤 上传**视频**、**音频文件**或提供🌐 **YouTube链接**。

          2. 🌍 选择您要**翻译视频**的语言。

          3. 🗣️ 指定视频中**发言人数量**并为每个人分配适合翻译语言的文本到语音（TTS）声音。

          4. 🚀 按下 '**翻译**' 按钮获取结果。

          ---

          # 🧩 **SoniTranslate支持不同的TTS（文本到语音）引擎，包括:**
          - EDGE-TTS → 格式 `en-AU-WilliamNeural-Male` → 快速而准确。
          - FACEBOOK MMS → 格式 `en-facebook-mms VITS` → 声音更自然；目前仅使用CPU。
          - PIPER TTS → 格式 `en_US-lessac-high VITS-onnx` → 与前一款相同，但针对CPU和GPU进行了优化。
          - BARK → 格式 `en_speaker_0-Male BARK` → 质量良好但速度较慢，易产生幻觉。
          - OpenAI TTS → 格式 `>alloy OpenAI-TTS` → 多语言但需要 OpenAI API key
          - Coqui XTTS → 格式 `_XTTS_/AUTOMATIC.wav` → 仅支持简体中文、英文、法文、德文、意大利文、葡萄牙文、波兰文、土耳其文、俄文、荷兰文、捷克文、阿拉伯文、西班牙文、匈牙利文、韩文和日文。

          ---

          # 🎤 如何使用R.V.C.和R.V.C.2语音（可选）🎶

          目标是将R.V.C.应用于生成的TTS（文本到语音）🎙️

          1. 在`自定义语音R.V.C.`标签中，下载您需要的模型📥 您可以使用Hugging Face和Google Drive的链接，格式如zip、pth或index。您还可以下载完整的HF空间存储库，但此选项不太稳定😕

          2. 现在，转到`替换语音：TTS到R.V.C.`并选中`启用`框✅ 然后，您可以选择要应用于每个TTS发言者的模型👩‍🦰👨‍🦱👩‍🦳👨‍🦲

          3. 调整将应用于所有R.V.C.的F0方法🎛️

          4. 按下`应用配置`以应用所做的更改🔄

          5. 返回视频翻译标签，单击 '翻译' ▶️ 现在，将应用R.V.C.进行翻译。🗣️

          提示：您可以使用`测试R.V.C.`来进行实验，找到要应用于R.V.C.的最佳TTS或配置🧪🔍

          ---

          """,
        "tab_translate": "视频翻译",
        "video_source": "选择视频来源",
        "link_label": "媒体链接。",
        "link_info": "示例：www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL放这里...",
        "dir_label": "视频路径。",
        "dir_info": "示例：/usr/home/my_video.mp4",
        "dir_ph": "路径放这里...",
        "sl_label": "源语言",
        "sl_info": "这是视频的原始语言",
        "tat_label": "翻译成",
        "tat_info": "选择目标语言，同时确保选择该语言对应的TTS。",
        "num_speakers": "选择视频中有多少个人在说话。",
        "min_sk": "最少发言者",
        "max_sk": "最多发言者",
        "tts_select": "为每个发言者选择您想要的语音。",
        "sk1": "TTS发言者 1",
        "sk2": "TTS发言者 2",
        "sk3": "TTS发言者 3",
        "sk4": "TTS发言者 4",
        "sk5": "TTS发言者 5",
        "sk6": "TTS发言者 6",
        "sk7": "TTS发言者 7",
        "sk8": "TTS发言者 8",
        "sk9": "TTS发言者 9",
        "sk10": "TTS发言者 10",
        "sk11": "TTS发言者 11",
        "sk12": "TTS发言者 12",
        "vc_title": "不同语言的语音模仿",
        "vc_subtitle": """
          ### 在各种语言中复制一个人的声音。
          当适当使用时，大多数声音都很有效，但并不是每种情况都能达到完美。
          语音模仿仅复制参考发言者的音调，不包括口音和情感，这些由基础发言者TTS模型控制，并且不会被转换器复制。
          这将从主音频中获取每个发言者的音频样本并处理它们。
          """,
        "vc_active_label": "激活语音模仿",
        "vc_active_info": "激活语音模仿：复制原始发言者的音调",
        "vc_method_label": "方法",
        "vc_method_info": "选择语音模仿过程的方法",
        "vc_segments_label": "最大样本数",
        "vc_segments_info": "最大样本数：是将用于处理的音频样本数量，越多越好，但可能会添加噪音",
        "vc_dereverb_label": "去混响",
        "vc_dereverb_info": "去混响：将声音去除混响应用于音频样本。",
        "vc_remove_label": "删除先前的样本",
        "vc_remove_info": "删除先前的样本：删除先前生成的样本，因此需要创建新样本。",
        "xtts_title": "基于音频创建TTS",
        "xtts_subtitle": "上传最长10秒的带有声音的音频文件。使用XTTS，将创建一个与提供的音频文件类似的新TTS。",
        "xtts_file_label": "上传具有声音的短音频",
        "xtts_name_label": "TTS的名称",
        "xtts_name_info": "使用简单的名称",
        "xtts_dereverb_label": "去混响音频",
        "xtts_dereverb_info": "去混响音频：将声音去除混响应用于音频",
        "xtts_button": "处理音频并将其包含在TTS选择器中",
        "xtts_footer": "自动生成语音xtts：您可以在TTS选择器中使用 `_XTTS_/AUTOMATIC.wav` 来为每个发言者自动生成片段，以用于生成翻译时。",
        "extra_setting": "高级设置",
        "acc_max_label": "最大音频加速度",
        "acc_max_info": "翻译音频段的最大加速度，以避免重叠。值为1.0表示无加速度",
        "acc_rate_label": "加速度调节",
        "acc_rate_info": "加速度调节：调整加速度以适应需要较低速度的片段，保持连续性并考虑下一个开始的时机。",
        "or_label": "重叠减少",
        "or_info": "重叠减少：通过根据先前的结束时间调整开始时间来确保片段不重叠；可能会干扰同步。",
        "aud_mix_label": "音频混合方法",
        "aud_mix_info": "混合原始和翻译音频文件，以创建平衡的定制输出，提供两种可用的混合模式。",
        "vol_ori": "原始音频音量",
        "vol_tra": "翻译音频音量",
        "voiceless_tk_label": "无声音轨",
        "voiceless_tk_info": "无声音轨：在将其与翻译音频结合之前删除原始音频声音。",
        "sub_type": "字幕类型",
        "soft_subs_label": "软字幕",
        "soft_subs_info": "软字幕：观众在观看视频时可以选择打开或关闭的可选字幕。",
        "burn_subs_label": "烧录字幕",
        "burn_subs_info": "烧录字幕：将字幕嵌入视频中，使其成为视觉内容的永久部分。",
        "whisper_title": "配置转录。",
        "lnum_label": "数字文字化",
        "lnum_info": "数字文字化：将数字表示替换为其在转录中的书面等价物。",
        "scle_label": "声音清理",
        "scle_info": "声音清理：增强语音，消除转录之前的背景噪音，以实现最大的时间戳精度。此操作可能需要一些时间，特别是对于较长的音频文件。",
        "sd_limit_label": "段落时长限制",
        "sd_limit_info": "指定每个段落的最大持续时间（以秒为单位）。将使用VAD处理音频，以限制每个段落块的持续时间。",
        "asr_model_info": "默认情况下，它使用“Whisper模型”将口语转换为文本。使用自定义模型，例如，在下拉菜单中输入存储库名称“BELLE-2/Belle-whisper-large-v3-zh”以使用经过中文语言微调的模型。在Hugging Face上找到微调模型。",
        "ctype_label": "计算类型",
        "ctype_info": "选择较小的类型，如int8或float16，可以通过减少内存使用量和增加计算吞吐量来提高性能，但可能会牺牲与float32等较大数据类型相比的精度。",
        "batchz_label": "批处理大小",
        "batchz_info": "如果您的GPU的VRAM较少，则减小批处理大小可以节省内存，并有助于管理内存不足问题。",
        "tsscale_label": "文本分段比例",
        "tsscale_info": "按句子、单词或字符将文本分成段。按单词和字符进行分段可提供更精细的粒度，适用于字幕等用途；禁用翻译将保留原始结构。",
        "srt_file_label": "上传SRT字幕文件（将用于替代Whisper的转录）",
        "divide_text_label": "通过以下方式重新划分文本段：",
        "divide_text_info": "（实验性）输入用于拆分源语言中现有文本段的分隔符。该工具将识别出现并相应地创建新段。使用|指定多个分隔符，例如：!|?|...|。",
        "diarization_label": "辨识模型",
        "tr_process_label": "翻译过程",
        "out_type_label": "输出类型",
        "out_name_label": "文件名",
        "out_name_info": "输出文件的名称",
        "task_sound_label": "任务状态声音",
        "task_sound_info": "任务状态声音：播放指示任务完成或执行过程中错误的声音警报。",
        "cache_label": "恢复进度",
        "cache_info": "恢复进度：从上一个检查点继续进行流程。",
        "preview_info": "预览将视频裁剪为仅10秒以进行测试。请在检索完整视频持续时间之前停用它。",
        "edit_sub_label": "编辑生成的字幕",
        "edit_sub_info": "编辑生成的字幕：允许您分两步运行翻译。首先使用 '获取字幕并编辑' 按钮获取字幕以编辑它们，然后使用 '翻译' 按钮生成视频",
        "button_subs": "获取字幕并编辑",
        "editor_sub_label": "生成的字幕",
        "editor_sub_info": "请在此处编辑生成的字幕中的文本。您可以在点击 '翻译' 按钮之前更改界面选项，但不能更改 '源语言'、'翻译成' 和 '最多发言者'，以避免错误。编辑完成后，点击 '翻译' 按钮。",
        "editor_sub_ph": "首先点击 '获取字幕并编辑' 获取字幕",
        "button_translate": "翻译",
        "output_result_label": "下载翻译视频",
        "sub_ori": "字幕",
        "sub_tra": "翻译字幕",
        "ht_token_info": "一个重要步骤是接受使用Pyannote的许可协议。您需要在Hugging Face上拥有一个帐户，并接受使用模型的许可：https://huggingface.co/pyannote/speaker-diarization 和 https://huggingface.co/pyannote/segmentation。在此处获取您的密钥令牌：https://hf.co/settings/tokens",
        "ht_token_ph": "令牌放这里...",
        "tab_docs": "文档翻译",
        "docs_input_label": "选择文档来源",
        "docs_input_info": "可以是PDF、DOCX、TXT或文本",
        "docs_source_info": "这是文本的原始语言",
        "chunk_size_label": "TTS每个段处理的最大字符数",
        "chunk_size_info": "值为0分配了一个动态且更兼容的值给TTS。",
        "docs_button": "开始语言转换桥",
        "cv_url_info": "从URL自动下载R.V.C.模型。您可以使用HuggingFace或Drive的链接，您可以包括多个链接，每个链接用逗号分隔。示例：https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "替换语音：TTS到R.V.C.",
        "sec1_title": "### 1. 要启用其使用，请将其标记为启用。",
        "enable_replace": "选中此框以启用模型的使用。",
        "sec2_title": "### 2. 选择将应用于每个相应发言者的TTS的声音，并应用配置。",
        "sec2_subtitle": "根据您将使用的<TTS发言者>的数量，每个都需要其各自的模型。此外，如果某种原因未正确检测到发言者，则还有一个辅助模型。",
        "cv_tts1": "选择要为发言者 1 应用的声音。",
        "cv_tts2": "选择要为发言者 2 应用的声音。",
        "cv_tts3": "选择要为发言者 3 应用的声音。",
        "cv_tts4": "选择要为发言者 4 应用的声音。",
        "cv_tts5": "选择要为发言者 5 应用的声音。",
        "cv_tts6": "选择要为发言者 6 应用的声音。",
        "cv_tts7": "选择要为发言者 7 应用的声音。",
        "cv_tts8": "选择要为发言者 8 应用的声音。",
        "cv_tts9": "选择要为发言者 9 应用的声音。",
        "cv_tts10": "选择要为发言者 10 应用的声音。",
        "cv_tts11": "选择要为发言者 11 应用的声音。",
        "cv_tts12": "选择要为发言者 12 应用的声音。",
        "cv_aux": "- 在某种原因下未成功检测到发言者时应用的声音。",
        "cv_button_apply": "应用配置",
        "tab_help": "帮助",
    },
    "ukrainian": {
        "description": """
        ### 🎥 **Перекладайте відео легко з SoniTranslate!** 📽️

        Завантажте відео, аудіофайл або надайте посилання на YouTube. 📽️ **Отримайте оновлений ноутбук з офіційного репозиторію: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Дивіться вкладку `Довідка` за інструкціями, як цим користуватися. Давайте почнемо веселощі з перекладу відео! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Інструкції з використання:**

        1. 📤 Завантажте **відео**, **аудіофайл** або надайте 🌐 **посилання на YouTube**.

        2. 🌍 Виберіть мову, на яку ви хочете **перекласти відео**.

        3. 🗣️ Вкажіть **кількість людей, які говорять** у відео і **призначте кожному голосу для синтезу мовлення тексту**, що відповідає мові перекладу.

        4. 🚀 Натисніть кнопку '**Переклад**', щоб отримати результати.

        ---

        # 🧩 **SoniTranslate підтримує різні двигуни TTS (текст-у-мову), які є:**
        - EDGE-TTS → формат `en-AU-WilliamNeural-Male` → Швидкий та точний.
        - FACEBOOK MMS → формат `en-facebook-mms VITS` → Голос більш натуральний; наразі використовується лише ЦП.
        - PIPER TTS → формат `en_US-lessac-high VITS-onnx` → Те ж саме, що й попередній, але оптимізований як для ЦП, так і для ГПУ.
        - BARK → формат `en_speaker_0-Male BARK` → Хороша якість, але повільна, і вона схильна до галюцинацій.
        - OpenAI TTS → формат `>alloy OpenAI-TTS` → Мультиязычный, але потребує OpenAI API key
        - Coqui XTTS → формат `_XTTS_/AUTOMATIC.wav` → Доступний лише для китайської (спрощеної), англійської, французької, німецької, італійської, португальської, польської, турецької, російської, голландської, чеської, арабської, іспанської, угорської, корейської та японської.

        ---

        # 🎤 Як використовувати голоси R.V.C. та R.V.C.2 (Необов'язково) 🎶

        Мета - застосувати R.V.C. до створеного TTS (текст-у-мову) 🎙️

        1. У вкладці `Корист. голос R.V.C.` завантажте необхідні моделі 📥 Ви можете використовувати посилання з Hugging Face та Google Drive у форматах, таких як zip, pth або index. Ви також можете завантажити повні репозиторії просторів HF, але ця опція не дуже стабільна 😕

        2. Тепер перейдіть до `Заміна голосу: TTS на R.V.C.` та позначте поле `enable` ✅ Після цього ви можете вибрати моделі, які ви хочете застосувати до кожного говорця TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Налаштуйте метод F0, який буде застосовуватися до всіх R.V.C. 🎛️

        4. Натисніть `ЗАСТОСУВАТИ КОНФІГУРАЦІЮ`, щоб застосувати зроблені зміни 🔄

        5. Поверніться до вкладки перекладу відео та натисніть на 'Переклад' ▶️ Тепер переклад буде виконаний з використанням R.V.C. 🗣️

        Порада: Ви можете використовувати `Тест R.V.C.` для експериментування та знаходження найкращих TTS або конфігурацій для застосування до R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Переклад відео",
        "video_source": "Виберіть джерело відео",
        "link_label": "Посилання на медіа.",
        "link_info": "Приклад: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "Тут введіть URL...",
        "dir_label": "Шлях до відео.",
        "dir_info": "Приклад: /usr/home/my_video.mp4",
        "dir_ph": "Тут введіть шлях...",
        "sl_label": "Мова джерела",
        "sl_info": "Це оригінальна мова відео",
        "tat_label": "Переклад аудіо на",
        "tat_info": "Виберіть цільову мову і також переконайтеся, що вибрали відповідний TTS для цієї мови.",
        "num_speakers": "Виберіть, скільки людей говорить у відео.",
        "min_sk": "Мін. говорці",
        "max_sk": "Макс. говорці",
        "tts_select": "Виберіть голос для кожного говорця.",
        "sk1": "Говорець TTS 1",
        "sk2": "Говорець TTS 2",
        "sk3": "Говорець TTS 3",
        "sk4": "Говорець TTS 4",
        "sk5": "Говорець TTS 5",
        "sk6": "Говорець TTS 6",
        "sk7": "Говорець TTS 7",
        "sk8": "Говорець TTS 8",
        "sk9": "Говорець TTS 9",
        "sk10": "Говорець TTS 10",
        "sk11": "Говорець TTS 11",
        "sk12": "Говорець TTS 12",
        "vc_title": "Імітація голосу на різних мовах",
        "vc_subtitle": """
        ### Відтворення голосу людини на різних мовах.
        Хоча це ефективно з більшістю голосів при відповідному використанні, воно може не досягти ідеальності в кожному випадку.
        Імітація голосу виключно відтворює тон джерела, не включаючи акцент і емоції, які контролюються базовою моделлю TTS говорця і не реплікуються конвертером.
        Це займе аудіопроби з основного аудіо для кожного говорця та обробить їх.
        """,
        "vc_active_label": "Активна імітація голосу",
        "vc_active_info": "Активна імітація голосу: Відтворює тон оригінального говорця",
        "vc_method_label": "Метод",
        "vc_method_info": "Виберіть метод для процесу імітації голосу",
        "vc_segments_label": "Макс. проби",
        "vc_segments_info": "Макс. проби: Кількість аудіопроб, які будуть згенеровані для процесу, більше - краще, але це може додати шум",
        "vc_dereverb_label": "Прибрати реверберацію",
        "vc_dereverb_info": "Прибрати реверберацію: Застосовує вокальну реверберацію до аудіопроб.",
        "vc_remove_label": "Видалити попередні проби",
        "vc_remove_info": "Видалити попередні проби: Видаляє попередні згенеровані проби, тому потрібно створити нові.",
        "xtts_title": "Створити TTS на основі аудіо",
        "xtts_subtitle": "Завантажте короткий аудіофайл максимум 10 секунд з голосом. Використовуючи XTTS, буде створений новий TTS з голосом, схожим на вказаний аудіофайл.",
        "xtts_file_label": "Завантажте короткий аудіофайл з голосом",
        "xtts_name_label": "Назва для TTS",
        "xtts_name_info": "Використовуйте просту назву",
        "xtts_dereverb_label": "Прибрати реверберацію з аудіо",
        "xtts_dereverb_info": "Прибрати реверберацію з аудіо: Застосовує вокальну реверберацію до аудіо",
        "xtts_button": "Обробити аудіо та включити його в селектор TTS",
        "xtts_footer": "Автоматично генеруйте голосовий xtts: Ви можете використовувати `_XTTS_/AUTOMATIC.wav` у селекторі TTS, щоб автоматично генерувати сегменти для кожного говорця при генерації перекладу.",
        "extra_setting": "Додаткові налаштування",
        "acc_max_label": "Макс. прискорення аудіо",
        "acc_max_info": "Максимальне прискорення для перекладених аудіосегментів для уникнення перекриття. Значення 1,0 означає відсутність прискорення",
        "acc_rate_label": "Регулювання швидкості прискорення",
        "acc_rate_info": "Регулювання швидкості прискорення: Налаштовує прискорення, щоб пристосуватися до сегментів, які потребують меншої швидкості, зберігаючи послідовність та враховуючи час наступного запуску.",
        "or_label": "Зменшення перекриття",
        "or_info": "Зменшення перекриття: Забезпечує відсутність перекриття сегментів за допомогою налаштування часу початку на основі попередніх часів завершення; може порушити синхронізацію.",
        "aud_mix_label": "Метод мікшування аудіо",
        "aud_mix_info": "Змішуйте оригінальні та перекладені аудіофайли, щоб створити налаштований, збалансований вихід з двома доступними режимами мікшування.",
        "vol_ori": "Гучність оригінального аудіо",
        "vol_tra": "Гучність перекладеного аудіо",
        "voiceless_tk_label": "Безголосий трек",
        "voiceless_tk_info": "Безголосий трек: Прибрати голоси оригінального аудіо перед його поєднанням з перекладеним аудіо.",
        "sub_type": "Тип субтитрів",
        "soft_subs_label": "М'які субтитри",
        "soft_subs_info": "М'які субтитри: Додаткові субтитри, які глядачі можуть увімкнути або вимкнути під час перегляду відео.",
        "burn_subs_label": "Підпалити субтитри",
        "burn_subs_info": "Підпалити субтитри: Вбудувати субтитри у відео, зробивши їх постійною частиною візуального змісту.",
        "whisper_title": "Налаштування транскрипції.",
        "lnum_label": "Літералізація Чисел",
        "lnum_info": "Літералізація Чисел: Заміна числових представлень на їх письмові еквіваленти в транскрипції.",
        "scle_label": "Очищення Звуку",
        "scle_info": "Очищення Звуку: Покращення голосів, видалення фонового шуму перед транскрипцією для максимальної точності відміток часу. Ця операція може зайняти час, особливо з довгими аудіофайлами.",
        "sd_limit_label": "Обмеження тривалості сегменту",
        "sd_limit_info": "Вкажіть максимальну тривалість (у секундах) для кожного сегменту. Аудіо буде оброблено за допомогою VAD, обмежуючи тривалість для кожного фрагменту сегменту.",
        "asr_model_info": "Він перетворює усну мову на текст за допомогою моделі 'Whisper' за замовчуванням. Використовуйте власну модель, наприклад, введіть ім'я репозиторію 'BELLE-2/Belle-whisper-large-v3-zh' у розкривному списку, щоб використовувати китайську мову з налаштованою моделлю. Знайдіть налаштовані моделі на Hugging Face.",
        "ctype_label": "Тип обчислення",
        "ctype_info": "Вибір менших типів, таких як int8 або float16, може покращити продуктивність, зменшивши використання пам'яті та збільшивши обчислювальну пропускну здатність, але може пожертвувати точністю порівняно з більшими типами даних, такими як float32.",
        "batchz_label": "Розмір пакету",
        "batchz_info": "Зменшення розміру пакета заощаджує пам'ять, якщо у вашої GPU менше VRAM, і допомагає керувати проблемами нестачі пам'яті.",
        "tsscale_label": "Масштаб сегментації тексту",
        "tsscale_info": "Розділіть текст на сегменти за допомогою речень, слів або символів. Сегментація за словами та символами надає більшу деталізацію, корисну для субтитрів; вимкнення перекладу зберігає вихідну структуру.",
        "srt_file_label": "Завантажте файл субтитрів SRT (використовуватиметься замість транскрипції Whisper)",
        "divide_text_label": "Розділити текстові сегменти за допомогою:",
        "divide_text_info": "(Експериментально) Введіть роздільник для розділення існуючих текстових сегментів на мові джерела. Інструмент ідентифікує випадки та створює нові сегменти відповідно. Вказуйте кілька роздільників, використовуючи |, наприклад: !|?|...|。",
        "diarization_label": "Модель діаризації",
        "tr_process_label": "Процес перекладу",
        "out_type_label": "Тип виводу",
        "out_name_label": "Ім'я файлу",
        "out_name_info": "Назва вихідного файлу",
        "task_sound_label": "Звук статусу завдання",
        "task_sound_info": "Звук статусу завдання: Відтворює звукове сповіщення про завершення завдання або помилки під час виконання.",
        "cache_label": "Отримати Прогрес",
        "cache_info": "Отримати Прогрес: Продовжити процес з останньої контрольної точки.",
        "preview_info": "Перегляд обрізає відео лише до 10 секунд для тестування. Будь ласка, деактивуйте його, щоб отримати повну тривалість відео.",
        "edit_sub_label": "Редагувати згенеровані субтитри",
        "edit_sub_info": "Редагувати згенеровані субтитри: Дозволяє виконувати переклад у 2 етапи. Спочатку за допомогою кнопки 'ОТРИМАТИ СУБТИТРИ ТА РЕДАГУВАТИ' ви отримуєте субтитри, щоб ви могли їх відредагувати, а потім за допомогою кнопки 'ПЕРЕКЛАСТИ' ви можете створити відео",
        "button_subs": "ОТРИМАТИ СУБТИТРИ ТА РЕДАГУВАТИ",
        "editor_sub_label": "Згенеровані субтитри",
        "editor_sub_info": "Вільно редагуйте текст в згенерованих субтитрах тут. Ви можете вносити зміни в параметри інтерфейсу перед тим, як натиснути кнопку 'ПЕРЕКЛАСТИ', за винятком 'Мови джерела', 'Переклад аудіо на' та 'Макс. говорці', щоб уникнути помилок. Як тільки ви закінчите, натисніть кнопку 'ПЕРЕКЛАСТИ'.",
        "editor_sub_ph": "Спочатку натисніть 'ОТРИМАТИ СУБТИТРИ ТА РЕДАГУВАТИ', щоб отримати субтитри",
        "button_translate": "ПЕРЕКЛАСТИ",
        "output_result_label": "ЗАВАНТАЖИТИ ПЕРЕКЛАДЕНЕ ВІДЕО",
        "sub_ori": "Субтитри",
        "sub_tra": "Перекладені субтитри",
        "ht_token_info": "Один із важливих кроків - прийняти ліцензійну угоду для використання Pyannote. Вам потрібно мати обліковий запис на Hugging Face та прийняти ліцензію для використання моделей: https://huggingface.co/pyannote/speaker-diarization та https://huggingface.co/pyannote/segmentation. Отримайте свій КЛЮЧОВИЙ ТОКЕН тут: https://hf.co/settings/tokens",
        "ht_token_ph": "Токен вставляється тут...",
        "tab_docs": "Переклад документів",
        "docs_input_label": "Виберіть джерело документа",
        "docs_input_info": "Це може бути PDF, DOCX, TXT або текст",
        "docs_source_info": "Це початкова мова тексту",
        "chunk_size_label": "Максимальна кількість символів, яку оброблятиме TTS на кожному сегменті",
        "chunk_size_info": "Значення 0 призначає динамічне і більш сумісне значення для TTS.",
        "docs_button": "Почати місткування мови",
        "cv_url_info": "Автоматично завантажте моделі R.V.C. за URL-адресою. Ви можете використовувати посилання з HuggingFace або Drive, а також включати кілька посилань, кожне з яких відокремлене комою. Приклад: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Замінити голос: TTS на R.V.C.",
        "sec1_title": "### 1. Для включення його використання відмітьте його як enable.",
        "enable_replace": "Позначте це, щоб увімкнути використання моделей.",
        "sec2_title": "### 2. Виберіть голос, який буде застосований до кожного TTS кожного відповідного говорця та застосуйте конфігурації.",
        "sec2_subtitle": "Залежно від того, скільки <TTS Speaker> ви будете використовувати, кожен з них потребує відповідної моделі. Крім того, є допоміжна, якщо з якихось причин говорець не розпізнається правильно.",
        "cv_tts1": "Виберіть голос для застосування до говорця 1.",
        "cv_tts2": "Виберіть голос для застосування до говорця 2.",
        "cv_tts3": "Виберіть голос для застосування до говорця 3.",
        "cv_tts4": "Виберіть голос для застосування до говорця 4.",
        "cv_tts5": "Виберіть голос для застосування до говорця 5.",
        "cv_tts6": "Виберіть голос для застосування до говорця 6.",
        "cv_tts7": "Виберіть голос для застосування до говорця 7.",
        "cv_tts8": "Виберіть голос для застосування до говорця 8.",
        "cv_tts9": "Виберіть голос для застосування до говорця 9.",
        "cv_tts10": "Виберіть голос для застосування до говорця 10.",
        "cv_tts11": "Виберіть голос для застосування до говорця 11.",
        "cv_tts12": "Виберіть голос для застосування до говорця 12.",
        "cv_aux": "- Голос, який застосовується у разі невдалого розпізнавання говорця.",
        "cv_button_apply": "ЗАСТОСУВАТИ КОНФІГУРАЦІЮ",
        "tab_help": "Довідка",
    },
    "arabic": {
        "description": """
          ### 🎥 **ترجمة مقاطع الفيديو بسهولة مع SoniTranslate!** 📽️

          قم بتحميل ملف فيديو أو صوتي أو قدم رابطًا لفيديو YouTube. 📽️ **احصل على الدفتر المحدث من المستودع الرسمي: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

          انظر إلى علامة التبويب "المساعدة" للحصول على تعليمات حول كيفية استخدامه. لنبدأ بالمرح مع ترجمة الفيديو! 🚀🎉
          """,
        "tutorial": """
          # 🔰 **تعليمات الاستخدام:**

          1. 📤 قم بتحميل **فيديو** أو ملف **صوتي** أو قم بتقديم 🌐 **رابط YouTube.**

          2. 🌍 اختر اللغة التي ترغب في **ترجمة الفيديو** إليها.

          3. 🗣️ حدد **عدد الأشخاص الذين يتحدثون** في الفيديو و **تعيين كل واحد منهم صوتًا للنص إلى الكلام** مناسبًا للغة الترجمة.

          4. 🚀 اضغط على زر '**ترجمة**' للحصول على النتائج.

          ---

          # 🧩 **يدعم SoniTranslate محركات TTS (نص إلى كلام) مختلفة، وهي:**
          - EDGE-TTS → الصيغة `en-AU-WilliamNeural-Male` → سريع ودقيق.
          - FACEBOOK MMS → الصيغة `en-facebook-mms VITS` → الصوت أكثر طبيعية؛ في الوقت الحالي، يستخدم فقط وحدة المعالجة المركزية.
          - PIPER TTS → الصيغة `en_US-lessac-high VITS-onnx` → نفس الشيء كما السابق، ولكنه محسّن لكل من وحدة المعالجة المركزية ووحدة معالجة الرسومات.
          - BARK → الصيغة `en_speaker_0-Male BARK` → جودة جيدة ولكن بطيء، ويميل إلى التهليل.
          - OpenAI TTS → الصيغة `>alloy OpenAI-TTS` → متعدد اللغات ولكن يتطلب OpenAI API key
          - Coqui XTTS → الصيغة `_XTTS_/AUTOMATIC.wav` → متاحة فقط للصينية (المبسطة)، الإنجليزية، الفرنسية، الألمانية، الإيطالية، البرتغالية، البولندية، التركية، الروسية، الهولندية، التشيكية، العربية، الإسبانية، الهنغارية، الكورية واليابانية.

          ---

          # 🎤 كيفية استخدام أصوات R.V.C. و R.V.C.2 (اختياري) 🎶

          الهدف هو تطبيق صوت R.V.C. على TTS المولد (نص إلى كلام) 🎙️

          1. في علامة التبويب "الصوت المخصص R.V.C."، قم بتنزيل النماذج التي تحتاجها 📥 يمكنك استخدام روابط من Hugging Face وGoogle Drive بتنسيقات مثل zip أو pth أو index. يمكنك أيضًا تنزيل مستودعات مساحة HF الكاملة، ولكن هذا الخيار غير مستقر جدًا 😕

          2. الآن، انتقل إلى "Replace voice: TTS to R.V.C." وحدد مربع "تمكين" ✅ بعد ذلك، يمكنك اختيار النماذج التي تريد تطبيقها على كل متحدث TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

          3. ضبط طريقة F0 التي ستُطبَّق على جميع R.V.C. 🎛️

          4. اضغط على `APPLY CONFIGURATION` لتطبيق التغييرات التي قمت بها 🔄

          5. ارجع إلى علامة التبويب لترجمة الفيديو وانقر فوق 'ترجمة' ▶️ الآن، سيتم إجراء الترجمة بتطبيق R.V.C. 🗣️

          نصيحة: يمكنك استخدام `Test R.V.C.` لتجربة والعثور على أفضل TTS أو التكوينات لتطبيق R.V.C. 🧪🔍

          ---

          """,
        "tab_translate": "ترجمة الفيديو",
        "video_source": "اختر مصدر الفيديو",
        "link_label": "رابط الوسائط.",
        "link_info": "مثال: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "يتم إدخال الرابط هنا...",
        "dir_label": "مسار الفيديو.",
        "dir_info": "مثال: /usr/home/my_video.mp4",
        "dir_ph": "يتم إدخال المسار هنا...",
        "sl_label": "اللغة المصدر",
        "sl_info": "هذه هي اللغة الأصلية للفيديو",
        "tat_label": "ترجمة الصوت إلى",
        "tat_info": "حدد اللغة المستهدفة وتأكد أيضًا من اختيار TTS المقابل لتلك اللغة.",
        "num_speakers": "حدد كم عدد الأشخاص الذين يتحدثون في الفيديو.",
        "min_sk": "الحد الأدنى من الأشخاص",
        "max_sk": "الحد الأقصى من الأشخاص",
        "tts_select": "اختر الصوت الذي تريده لكل متحدث.",
        "sk1": "متحدث TTS 1",
        "sk2": "متحدث TTS 2",
        "sk3": "متحدث TTS 3",
        "sk4": "متحدث TTS 4",
        "sk5": "متحدث TTS 5",
        "sk6": "متحدث TTS 6",
        "sk7": "متحدث TTS 7",
        "sk8": "متحدث TTS 8",
        "sk9": "متحدث TTS 9",
        "sk10": "متحدث TTS 10",
        "sk11": "متحدث TTS 11",
        "sk12": "متحدث TTS 12",
        "vc_title": "تقليد صوت في لغات مختلفة",
        "vc_subtitle": """
          ### استنساخ صوت الشخص عبر لغات متعددة.
          على الرغم من كفاءته مع معظم الأصوات عند استخدامه بشكل مناسب، قد لا يتم التمام في كل حالة.
          يقوم تقليد الصوت بالتمثيل فقط لنغمة المتحدث الأصلي، باستثناء اللكنة والعاطفة، التي تحكمها نموذج TTS الأصلي ولا يقوم المحول بتكرارها.
          سيتم أخذ عينات الصوت من الصوت الرئيسي لكل متحدث ومعالجتها.
          """,
        "vc_active_label": "تقليد صوت نشط",
        "vc_active_info": "تقليد صوت نشط: يقوم بتمثيل نغمة المتحدث الأصلي",
        "vc_method_label": "الطريقة",
        "vc_method_info": "حدد طريقة لعملية تقليد الصوت",
        "vc_segments_label": "الحد الأقصى للعينات",
        "vc_segments_info": "الحد الأقصى للعينات: هو عدد عينات الصوت التي سيتم إنشاؤها للعملية، كلما كانت أكثر كانت أفضل ولكن يمكن أن تضيف ضوضاء",
        "vc_dereverb_label": "إزالة الصدى",
        "vc_dereverb_info": "إزالة الصدى: يُطبَّق تقنية إزالة الصدى الصوتي على عينات الصوت.",
        "vc_remove_label": "إزالة العينات السابقة",
        "vc_remove_info": "إزالة العينات السابقة: قم بإزالة العينات السابقة التي تم إنشاؤها، لذلك يجب إنشاء عينات جديدة.",
        "xtts_title": "إنشاء TTS استنادًا إلى صوت",
        "xtts_subtitle": "قم بتحميل ملف صوتي لمدة 10 ثوانٍ كحد أقصى بصوت. باستخدام XTTS، سيتم إنشاء TTS جديد بصوت مشابه للملف الصوتي المقدم.",
        "xtts_file_label": "قم بتحميل ملف صوتي قصير بالصوت",
        "xtts_name_label": "اسم لـ TTS",
        "xtts_name_info": "استخدم اسمًا بسيطًا",
        "xtts_dereverb_label": "إزالة صدى الصوت",
        "xtts_dereverb_info": "إزالة صدى الصوت: يُطبَّق تقنية إزالة صدى الصوت على الصوت",
        "xtts_button": "معالجة الصوت وتضمينه في محدد TTS",
        "xtts_footer": "توليد صوت xtts تلقائيًا: يمكنك استخدام `_XTTS_/AUTOMATIC.wav` في محدد TTS لتوليد تقاطعات لكل متحدث تلقائيًا عند إنشاء الترجمة.",
        "extra_setting": "إعدادات متقدمة",
        "acc_max_label": "التسارع الصوتي الأقصى",
        "acc_max_info": "التسارع الأقصى لقطع الصوت المترجم لتجنب التداخل. قيمة 1.0 تمثل عدم وجود تسارع",
        "acc_rate_label": "تنظيم معدل التسارع",
        "acc_rate_info": "تنظيم معدل التسارع: يعدل التسارع لتوفير مقاطع تتطلب سرعة أقل، مع الحفاظ على الاستمرارية واعتبار توقيت البدء التالي.",
        "or_label": "تقليل التداخل",
        "or_info": "تقليل التداخل: يضمن عدم تداخل الشرائح عن طريق ضبط أوقات البدء استنادًا إلى الأوقات السابقة للنهاية ؛ قد يؤدي إلى إختلال التزامن.",
        "aud_mix_label": "طريقة مزج الصوت",
        "aud_mix_info": "مزج ملفات الصوت الأصلية والمترجمة لإنشاء إخراج مخصص ومتوازن بوجود طريقتي مزج متاحتين.",
        "vol_ori": "مستوى صوت الصوت الأصلي",
        "vol_tra": "مستوى صوت الصوت المترجم",
        "voiceless_tk_label": "مسار بدون صوت",
        "voiceless_tk_info": "مسار بدون صوت: قم بإزالة الأصوات الصوتية الأصلية قبل دمجها مع الصوت المترجم.",
        "sub_type": "نوع العنوان الفرعي",
        "soft_subs_label": "ترجمة نصية ناعمة",
        "soft_subs_info": "ترجمة نصية ناعمة: ترجمات نصية اختيارية يمكن للمشاهدين تشغيلها أو إيقافها أثناء مشاهدة الفيديو.",
        "burn_subs_label": "حرق الترجمة الفرعية",
        "burn_subs_info": "حرق الترجمة الفرعية: تضمين الترجمة الفرعية في الفيديو، مما يجعلها جزءًا دائمًا من المحتوى البصري.",
        "whisper_title": "تكوين النص السريع.",
        "lnum_label": "تحويل الأرقام إلى كلمات",
        "lnum_info": "تحويل الأرقام إلى كلمات: استبدال التمثيلات الرقمية بمكافآتها المكتوبة في النص المكتوب.",
        "scle_label": "تنظيف الصوت",
        "scle_info": "تنظيف الصوت: تعزيز الأصوات، إزالة الضجيج الخلفي قبل التفريغ للحصول على أقصى دقة في الطابع الزمني. قد تستغرق هذه العملية وقتًا، خاصة مع ملفات الصوت الطويلة.",
        "sd_limit_label": "حد مدة القطعة",
        "sd_limit_info": "حدد المدة القصوى (بالثواني) لكل قطعة. سيتم معالجة الصوت باستخدام VAD، محددة مدة كل قطعة.",
        "asr_model_info": "يحول اللغة الحية إلى نص باستخدام نموذج 'الهمس' افتراضيًا. استخدم نموذجًا مخصصًا، على سبيل المثال، عن طريق إدخال اسم المستودع 'BELLE-2/Belle-whisper-large-v3-zh' في القائمة المنسدلة لاستخدام نموذج معدل باللغة الصينية. العثور على النماذج المعدلة على Hugging Face.",
        "ctype_label": "نوع الحساب",
        "ctype_info": "اختيار أنواع أصغر مثل int8 أو float16 يمكن أن يحسن الأداء من خلال تقليل استخدام الذاكرة وزيادة الإخراج الحسابي، ولكن قد يضحي بالدقة مقارنة بأنواع البيانات الأكبر مثل float32.",
        "batchz_label": "حجم الدفعة",
        "batchz_info": "توفير الذاكرة عن طريق تقليل حجم الدفعة إذا كان لديك بطاقة رسومات GPU تحتوي على VRAM أقل وتساعد في إدارة مشكلات الذاكرة النفاد.",
        "tsscale_label": "مقياس تقسيم النص",
        "tsscale_info": "تقسيم النص إلى قطع حسب الجمل أو الكلمات أو الأحرف. يوفر تقسيم الكلمات والأحرف دقة أكبر، وهو مفيد للترجمات الفورية؛ يحافظ تعطيل الترجمة على الهيكل الأصلي.",
        "srt_file_label": "قم بتحميل ملف عنوان فرعي SRT (سيُستخدم بدلاً من النص السريع)",
        "divide_text_label": "إعادة تقسيم شرائح النص بواسطة:",
        "divide_text_info": "(تجريبي) أدخل فاصل لتقسيم شرائح النص الحالية في اللغة المصدر. ستحدد الأداة حدوث الحالات وإنشاء شرائح جديدة وفقًا لذلك. حدد علامات فاصلة متعددة باستخدام |، على سبيل المثال: !|؟|...|。",
        "diarization_label": "نموذج توثيق الصوت",
        "tr_process_label": "عملية الترجمة",
        "out_type_label": "نوع الإخراج",
        "out_name_label": "اسم الملف",
        "out_name_info": "اسم الملف الناتج",
        "task_sound_label": "صوت حالة المهمة",
        "task_sound_info": "صوت حالة المهمة: يشغل تنبيه صوتي يشير إلى اكتمال المهمة أو الأخطاء أثناء التنفيذ.",
        "cache_label": "استعادة التقدم",
        "cache_info": "استعادة التقدم: متابعة العملية من نقطة التفتيش الأخيرة.",
        "preview_info": "يقوم المعاينة بتقطيع الفيديو لمدة 10 ثوانٍ فقط لأغراض الاختبار. يرجى إلغاء تنشيطه لاسترداد مدة الفيديو الكاملة.",
        "edit_sub_label": "تحرير العناوين الفرعية المولدة",
        "edit_sub_info": "تحرير العناوين الفرعية المولدة: يتيح لك تشغيل الترجمة في 2 خطوة. أولاً بزر 'GET SUBTITLES AND EDIT'، يتم الحصول على العناوين الفرعية لتحريرها، ومن ثم بزر 'TRANSLATE'، يمكنك إنشاء الفيديو",
        "button_subs": "GET SUBTITLES AND EDIT",
        "editor_sub_label": "العناوين الفرعية المولدة",
        "editor_sub_info": "لا تتردد في تحرير النص في العناوين الفرعية المولدة هنا. يمكنك إجراء تغييرات على خيارات الواجهة قبل النقر على زر 'TRANSLATE'، باستثناء 'اللغة المصدر' و 'ترجمة الصوت إلى' و 'الحد الأقصى للأشخاص'، لتجنب الأخطاء. بمجرد الانتهاء، انقر فوق الزر 'TRANSLATE'.",
        "editor_sub_ph": "اضغط أولاً على 'GET SUBTITLES AND EDIT' للحصول على العناوين الفرعية",
        "button_translate": "TRANSLATE",
        "output_result_label": "تنزيل الفيديو المترجم",
        "sub_ori": "العناوين الفرعية",
        "sub_tra": "العناوين الفرعية المترجمة",
        "ht_token_info": "خطوة مهمة هي قبول اتفاقية الترخيص لاستخدام Pyannote. يجب أن تكون لديك حساب على Hugging Face وقبول الترخيص لاستخدام النماذج: https://huggingface.co/pyannote/speaker-diarization و https://huggingface.co/pyannote/segmentation. احصل على مفتاحك الخاص هنا: https://hf.co/settings/tokens",
        "ht_token_ph": "يتم إدخال المفتاح هنا...",
        "tab_docs": "ترجمة المستندات",
        "docs_input_label": "اختر مصدر المستند",
        "docs_input_info": "يمكن أن يكون PDF، DOCX، TXT، أو نص",
        "docs_source_info": "هذه هي اللغة الأصلية للنص",
        "chunk_size_label": "الحد الأقصى لعدد الأحرف التي سيعالجها TTS في كل شريحة",
        "chunk_size_info": "تُخصص قيمة 0 قيمة ديناميكية وأكثر توافقًا لـ TTS.",
        "docs_button": "بدء جسر تحويل اللغة",
        "cv_url_info": "قم بتنزيل نماذج R.V.C. تلقائيًا من الرابط. يمكنك استخدام روابط من HuggingFace أو Drive، ويمكنك تضمين عدة روابط، مفصولة بفاصلة. على سبيل المثال: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth، https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "استبدال الصوت: TTS إلى R.V.C.",
        "sec1_title": "### 1. لتمكين استخدامه، ضع علامة على تمكينه.",
        "enable_replace": "تحقق من ذلك لتمكين استخدام النماذج.",
        "sec2_title": "### 2. اختر صوتًا سيتم تطبيقه على كل TTS لكل متحدث مقابل وطبق التكوينات.",
        "sec2_subtitle": "يعتمد ذلك على عدد <متحدث TTS> الذي ستستخدمه، ويحتاج كل منها إلى نموذجه الخاص. بالإضافة إلى ذلك، هناك واحدة مساعدة في حالة عدم اكتشاف المتحدث بشكل صحيح لأي سبب ما.",
        "cv_tts1": "اختر الصوت المراد تطبيقه على المتحدث 1.",
        "cv_tts2": "اختر الصوت المراد تطبيقه على المتحدث 2.",
        "cv_tts3": "اختر الصوت المراد تطبيقه على المتحدث 3.",
        "cv_tts4": "اختر الصوت المراد تطبيقه على المتحدث 4.",
        "cv_tts5": "اختر الصوت المراد تطبيقه على المتحدث 5.",
        "cv_tts6": "اختر الصوت المراد تطبيقه على المتحدث 6.",
        "cv_tts7": "اختر الصوت المراد تطبيقه على المتحدث 7.",
        "cv_tts8": "اختر الصوت المراد تطبيقه على المتحدث 8.",
        "cv_tts9": "اختر الصوت المراد تطبيقه على المتحدث 9.",
        "cv_tts10": "اختر الصوت المراد تطبيقه على المتحدث 10.",
        "cv_tts11": "اختر الصوت المراد تطبيقه على المتحدث 11.",
        "cv_tts12": "اختر الصوت المراد تطبيقه على المتحدث 12.",
        "cv_aux": "- الصوت المراد تطبيقه في حالة عدم اكتشاف المتحدث بنجاح.",
        "cv_button_apply": "تطبيق التكوين",
        "tab_help": "مساعدة",
    },
    "russian": {
        "description": """
        ### 🎥 **Перевод видео легко с SoniTranslate!** 📽️

        Загрузите видео, аудиофайл или предоставьте ссылку на YouTube. 📽️ **Получите обновленный блокнот из официального репозитория.: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Посмотрите вкладку `Помощь` для инструкций о том, как это использовать. Давайте начнем веселиться с переводом видео! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Инструкции по использованию:**

        1. 📤 Загрузите **видео**, **аудиофайл** или предоставьте 🌐 **ссылку на YouTube**.

        2. 🌍 Выберите язык, на который вы хотите **перевести видео**.

        3. 🗣️ Укажите **количество говорящих** в видео и **назначьте каждому голос синтеза речи** подходящий для языка перевода.

        4. 🚀 Нажмите кнопку '**Перевести**', чтобы получить результаты.

        ---

        # 🧩 **SoniTranslate поддерживает различные движки TTS (текст в речь), которые включают:**
        - EDGE-TTS → формат `en-AU-WilliamNeural-Male` → Быстро и точно.
        - FACEBOOK MMS → формат `en-facebook-mms VITS` → Голос более естественный; на данный момент используется только процессор.
        - PIPER TTS → формат `en_US-lessac-high VITS-onnx` → То же самое, что и предыдущее, но оптимизировано как для CPU, так и для GPU.
        - BARK → формат `en_speaker_0-Male BARK` → Хорошее качество, но медленное, и оно подвержено галлюцинациям.
        - OpenAI TTS → формат `>alloy OpenAI-TTS` → Многоязычный, но требуется OpenAI API key
        - Coqui XTTS → формат `_XTTS_/AUTOMATIC.wav` → Доступен только для китайского (упрощенного), английского, французского, немецкого, итальянского, португальского, польского, турецкого, русского, голландского, чешского, арабского, испанского, венгерского, корейского и японского языков.

        ---

        # 🎤 Как использовать голоса R.V.C. и R.V.C.2 (необязательно) 🎶

        Цель - применить R.V.C. к созданному TTS (текст в речь) 🎙️

        1. На вкладке `Настройка пользовательского голоса R.V.C.` загрузите необходимые модели 📥 Можно использовать ссылки из Hugging Face и Google Drive в форматах zip, pth или index. Вы также можете загрузить полные репозитории HF space, но эта опция не очень стабильна 😕

        2. Теперь перейдите в раздел `Заменить голос: TTS на R.V.C.` и установите флажок `включить` ✅ После этого вы сможете выбрать модели, которые хотите применить к каждому говорителю TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Настройте метод F0, который будет применен ко всем R.V.C. 🎛️

        4. Нажмите `ПРИМЕНИТЬ КОНФИГУРАЦИЮ`, чтобы применить внесенные вами изменения 🔄

        5. Вернитесь на вкладку перевода видео и нажмите 'Перевести' ▶️ Теперь перевод будет выполнен с применением R.V.C. 🗣️

        Совет: Вы можете использовать `Тест R.V.C.` для экспериментов и поиска лучших TTS или конфигураций для применения к R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Перевод видео",
        "video_source": "Выберите источник видео",
        "link_label": "Ссылка на медиа.",
        "link_info": "Пример: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "Сюда вставьте URL...",
        "dir_label": "Путь к видео.",
        "dir_info": "Пример: /usr/home/my_video.mp4",
        "dir_ph": "Сюда вставьте путь...",
        "sl_label": "Исходный язык",
        "sl_info": "Это оригинальный язык видео",
        "tat_label": "Перевести аудио на",
        "tat_info": "Выберите целевой язык и также убедитесь, что выбран соответствующий TTS для этого языка.",
        "num_speakers": "Выберите, сколько людей говорят в видео.",
        "min_sk": "Мин. количество говорящих",
        "max_sk": "Макс. количество говорящих",
        "tts_select": "Выберите голос для каждого говорящего.",
        "sk1": "Говорящий 1 (TTS)",
        "sk2": "Говорящий 2 (TTS)",
        "sk3": "Говорящий 3 (TTS)",
        "sk4": "Говорящий 4 (TTS)",
        "sk5": "Говорящий 5 (TTS)",
        "sk6": "Говорящий 6 (TTS)",
        "sk7": "Говорящий 7 (TTS)",
        "sk8": "Говорящий 8 (TTS)",
        "sk9": "Говорящий 9 (TTS)",
        "sk10": "Говорящий 10 (TTS)",
        "sk11": "Говорящий 11 (TTS)",
        "sk12": "Говорящий 12 (TTS)",
        "vc_title": "Имитация голоса на разных языках",
        "vc_subtitle": """
        ### Воспроизведение голоса человека на разных языках.
        Несмотря на то, что оно эффективно с большинством голосов при правильном использовании, в некоторых случаях оно может не достигать идеальности.
        Имитация голоса полностью воспроизводит тон референсного диктора, исключая акцент и эмоции, которые контролируются базовой моделью TTS диктора и не воспроизводятся конвертером.
        Это займет аудиосэмплы из основного аудио для каждого говорящего и обработает их.
        """,
        "vc_active_label": "Активировать имитацию голоса",
        "vc_active_info": "Активировать имитацию голоса: Воспроизводит тон оригинального говорящего",
        "vc_method_label": "Метод",
        "vc_method_info": "Выберите метод для процесса имитации голоса",
        "vc_segments_label": "Макс. количество сэмплов",
        "vc_segments_info": "Максимальное количество сэмплов: это количество аудиосэмплов, которые будут сгенерированы для процесса, чем их больше, тем лучше, но это может добавить шум",
        "vc_dereverb_label": "Удалить реверберацию",
        "vc_dereverb_info": "Удалить реверберацию: Применяет вокальную реверберацию к аудиосэмплам.",
        "vc_remove_label": "Удалить предыдущие сэмплы",
        "vc_remove_info": "Удалить предыдущие сэмплы: Удаляет предыдущие сгенерированные сэмплы, поэтому нужно создавать новые.",
        "xtts_title": "Создание TTS на основе аудио",
        "xtts_subtitle": "Загрузите аудиофайл максимум на 10 секунд с голосом. Используя XTTS, будет создан новый TTS с голосом, аналогичным предоставленному аудиофайлу.",
        "xtts_file_label": "Загрузить короткое аудио с голосом",
        "xtts_name_label": "Название для TTS",
        "xtts_name_info": "Используйте простое название",
        "xtts_dereverb_label": "Удалить реверберацию аудио",
        "xtts_dereverb_info": "Удалить реверберацию аудио: Применяет вокальную реверберацию к аудио",
        "xtts_button": "Обработать аудио и включить его в селектор TTS",
        "xtts_footer": "Генерировать голосовой XTTS автоматически: Вы можете использовать `_XTTS_/AUTOMATIC.wav` в селекторе TTS для автоматической генерации сегментов для каждого говорящего при создании перевода.",
        "extra_setting": "Дополнительные настройки",
        "acc_max_label": "Макс. ускорение аудио",
        "acc_max_info": "Максимальное ускорение для переведенных аудиосегментов для избежания их перекрытия. Значение 1.0 означает отсутствие ускорения",
        "acc_rate_label": "Регулирование уровня ускорения",
        "acc_rate_info": "Регулирование уровня ускорения: Регулирует ускорение для адаптации к сегментам, требующим меньшей скорости, сохраняя непрерывность и учитывая временные параметры следующего запуска.",
        "or_label": "Сокращение перекрытий",
        "or_info": "Сокращение перекрытий: Обеспечивает отсутствие перекрытия сегментов путем корректировки времени начала на основе предыдущих времен завершения; может нарушить синхронизацию.",
        "aud_mix_label": "Метод смешивания аудио",
        "aud_mix_info": "Смешивание оригинальных и переведенных аудиофайлов для создания настраиваемого, сбалансированного вывода с двумя доступными режимами смешивания.",
        "vol_ori": "Громкость оригинального аудио",
        "vol_tra": "Громкость переведенного аудио",
        "voiceless_tk_label": "Безголосовая дорожка",
        "voiceless_tk_info": "Безголосовая дорожка: Удалить голоса оригинального аудио перед его смешиванием с переведенным аудио.",
        "sub_type": "Тип субтитров",
        "soft_subs_label": "Мягкие субтитры",
        "soft_subs_info": "Мягкие субтитры: Дополнительные субтитры, которые зрители могут включать или выключать во время просмотра видео.",
        "burn_subs_label": "Вжечь субтитры",
        "burn_subs_info": "Вжечь субтитры: Внедрить субтитры в видео, сделав их постоянной частью визуального контента.",
        "whisper_title": "Конфигурация транскрипции.",
        "lnum_label": "Литерализация Чисел",
        "lnum_info": "Литерализация Чисел: Замена числовых представлений их письменными эквивалентами в транскрипции.",
        "scle_label": "Очистка Звука",
        "scle_info": "Очистка Звука: Улучшение голосов, удаление фонового шума перед транскрипцией для максимальной точности временных меток. Эта операция может занять время, особенно с длинными аудиофайлами.",
        "sd_limit_label": "Ограничение Длительности Сегмента",
        "sd_limit_info": "Укажите максимальную длительность (в секундах) для каждого сегмента. Аудио будет обработано с использованием VAD, ограничивая длительность для каждого фрагмента сегмента.",
        "asr_model_info": "Он преобразует устную речь в текст с использованием модели 'Whisper' по умолчанию. Используйте пользовательскую модель, например, введите имя репозитория 'BELLE-2/Belle-whisper-large-v3-zh' в выпадающем списке, чтобы использовать китайскую модель. Найдите настроенные модели на Hugging Face.",
        "ctype_label": "Тип вычисления",
        "ctype_info": "Выбор меньших типов, таких как int8 или float16, может улучшить производительность за счет уменьшения использования памяти и увеличения вычислительного потока, но может пожертвовать точностью по сравнению с более крупными типами данных, такими как float32.",
        "batchz_label": "Размер Пакета",
        "batchz_info": "Уменьшение размера пакета экономит память, если у вашей GPU меньше VRAM, и помогает управлять проблемами с памятью.",
        "tsscale_label": "Масштабирование сегментации текста",
        "tsscale_info": "Разделите текст на сегменты по предложениям, словам или символам. Сегментация по словам и символам обеспечивает более точную гранулярность, полезную для субтитров; отключение перевода сохраняет исходную структуру.",
        "srt_file_label": "Загрузить файл субтитров в формате SRT (будет использоваться вместо транскрипции Whisper)",
        "divide_text_label": "Разделить текстовые сегменты по:",
        "divide_text_info": "(Экспериментально) Введите разделитель для разделения существующих текстовых сегментов на исходном языке. Инструмент определит вхождения и создаст новые сегменты в соответствии с ними. Укажите несколько разделителей, используя |, например: !|?|...|。",
        "diarization_label": "Модель диаризации",
        "tr_process_label": "Процесс перевода",
        "out_type_label": "Тип вывода",
        "out_name_label": "Имя файла",
        "out_name_info": "Название выходного файла",
        "task_sound_label": "Звук статуса задачи",
        "task_sound_info": "Звук статуса задачи: Воспроизводит звуковой сигнал, указывающий на завершение задачи или ошибки во время выполнения.",
        "cache_label": "Восстановление прогресса",
        "cache_info": "Восстановление прогресса: Продолжить процесс с последней контрольной точки.",
        "preview_info": "Предпросмотр обрезает видео до 10 секунд только для тестовых целей. Пожалуйста, отключите его, чтобы получить полную продолжительность видео.",
        "edit_sub_label": "Редактировать сгенерированные субтитры",
        "edit_sub_info": "Редактировать сгенерированные субтитры: Позволяет выполнять перевод в 2 этапа. Сначала нажмите кнопку 'ПОЛУЧИТЬ СУБТИТРЫ И РЕДАКТИРОВАТЬ', чтобы получить субтитры и отредактировать их, а затем с помощью кнопки 'ПЕРЕВЕСТИ' вы можете сгенерировать видео",
        "button_subs": "ПОЛУЧИТЬ СУБТИТРЫ И РЕДАКТИРОВАТЬ",
        "editor_sub_label": "Сгенерированные субтитры",
        "editor_sub_info": "Не стесняйтесь редактировать текст в сгенерированных субтитрах здесь. Вы можете вносить изменения в параметры интерфейса перед нажатием кнопки 'ПЕРЕВЕСТИ', за исключением 'Исходный язык', 'Перевести аудио на' и 'Макс. количество говорящих', чтобы избежать ошибок. Как только закончите, нажмите кнопку 'ПЕРЕВЕСТИ'.",
        "editor_sub_ph": "Сначала нажмите 'ПОЛУЧИТЬ СУБТИТРЫ И РЕДАКТИРОВАТЬ', чтобы получить субтитры",
        "button_translate": "ПЕРЕВЕСТИ",
        "output_result_label": "СКАЧАТЬ ПЕРЕВЕДЕННОЕ ВИДЕО",
        "sub_ori": "Субтитры",
        "sub_tra": "Переведенные субтитры",
        "ht_token_info": "Один из важных шагов - принятие лицензионного соглашения на использование Pyannote. Вам нужно иметь учетную запись на Hugging Face и принять лицензию, чтобы использовать модели: https://huggingface.co/pyannote/speaker-diarization и https://huggingface.co/pyannote/segmentation. Получите свой КЛЮЧ ТОКЕН здесь: https://hf.co/settings/tokens",
        "ht_token_ph": "Сюда вставьте токен...",
        "tab_docs": "Перевод документов",
        "docs_input_label": "Выберите источник документа",
        "docs_input_info": "Это может быть PDF, DOCX, TXT или текст",
        "docs_source_info": "Это оригинальный язык текста",
        "chunk_size_label": "Макс. количество символов, которые будет обрабатывать TTS для каждого сегмента",
        "chunk_size_info": "Значение 0 назначает динамическое и более совместимое значение для TTS.",
        "docs_button": "Запустить мост перевода языка",
        "cv_url_info": "Автоматическая загрузка моделей R.V.C. по URL. Можно использовать ссылки из HuggingFace или Drive, и можно включить несколько ссылок, каждую разделенную запятой. Пример: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Заменить голос: TTS на R.V.C.",
        "sec1_title": "### 1. Чтобы активировать его использование, укажите его как включенный.",
        "enable_replace": "Установите флажок, чтобы включить использование моделей.",
        "sec2_title": "### 2. Выберите голос, который будет применен к каждому TTS каждого соответствующего говорящего и примените конфигурации.",
        "sec2_subtitle": "В зависимости от того, сколько <TTS говорящего> вы будете использовать, каждый из них нуждается в своей соответствующей модели. Кроме того, есть вспомогательная, если по какой-то причине говорящий не был определен правильно.",
        "cv_tts1": "Выберите голос для применения для Говорящего 1.",
        "cv_tts2": "Выберите голос для применения для Говорящего 2.",
        "cv_tts3": "Выберите голос для применения для Говорящего 3.",
        "cv_tts4": "Выберите голос для применения для Говорящего 4.",
        "cv_tts5": "Выберите голос для применения для Говорящего 5.",
        "cv_tts6": "Выберите голос для применения для Говорящего 6.",
        "cv_tts7": "Выберите голос для применения для Говорящего 7.",
        "cv_tts8": "Выберите голос для применения для Говорящего 8.",
        "cv_tts9": "Выберите голос для применения для Говорящего 9.",
        "cv_tts10": "Выберите голос для применения для Говорящего 10.",
        "cv_tts11": "Выберите голос для применения для Говорящего 11.",
        "cv_tts12": "Выберите голос для применения для Говорящего 12.",
        "cv_aux": "- Голос, который будет применен в случае успешного неопределения говорящего.",
        "cv_button_apply": "ПРИМЕНИТЬ КОНФИГУРАЦИЮ",
        "tab_help": "Помощь",
    },
    "turkish": {
        "description": """
        ### 🎥 **SoniTranslate ile videoları kolayca çevirin!** 📽️

        Bir video yükleyin, ses dosyası ekleyin veya bir YouTube bağlantısı sağlayın. 📽️ **Güncellenmiş notebook'ı resmi depodan alın: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Kullanım talimatları için 'Yardım' sekmesine bakın. Video çevirisi yapmaya başlayalım! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Kullanım Talimatları:**

        1. 📤 Bir **video**, **ses dosyası** yükleyin veya bir 🌐 **YouTube bağlantısı sağlayın.**

        2. 🌍 **Videodaki metni çevirmek istediğiniz dili seçin.**

        3. 🗣️ Videodaki **konuşan kişi sayısını belirtin** ve her birine çeviri dili için uygun bir metin-okuma-sesini atayın.

        4. 🚀 Sonuçları elde etmek için '**Çevir**' düğmesine basın.

        ---

        # 🧩 **SoniTranslate, farklı TTS (Metin-okuma-sesi) motorlarını destekler, bunlar:**
        - EDGE-TTS → biçim `tr-TR-ZeynepNeural-Kadın` → Hızlı ve doğru.
        - FACEBOOK MMS → biçim `tr-facebook-mms VITS` → Ses daha doğal; şu anda yalnızca CPU kullanıyor.
        - PIPER TTS → biçim `tr_TR-lessac-high VITS-onnx` → Öncekiyle aynı, ancak hem CPU hem de GPU için optimize edilmiştir.
        - BARK → biçim `tr_speaker_0-Kadın BARK` → İyi kalite ancak yavaş ve halüsinasyonlara eğilimli.
        - OpenAI TTS → biçim `>alloy OpenAI-TTS` → Çok dilli ancak bir OpenAI API key gerektirir
        - Coqui XTTS → biçim `_XTTS_/AUTOMATIC.wav` → Sadece Çince (Basitleştirilmiş), İngilizce, Fransızca, Almanca, İtalyanca, Portekizce, Lehçe, Türkçe, Rusça, Hollandaca, Çekçe, Arapça, İspanyolca, Macarca, Korece ve Japonca için mevcut.

        ---

        # 🎤 R.V.C. ve R.V.C.2 Seslerini Nasıl Kullanılır (İsteğe Bağlı) 🎶

        Amaç, oluşturulan TTS'ye bir R.V.C. uygulamaktır (Metin-okuma-sesi) 🎙️

        1. 'Özel Ses R.V.C.' sekmesinde, ihtiyacınız olan modelleri indirin 📥 Hugging Face ve Google Drive gibi bağlantıları, zip, pth veya index gibi formatlarda kullanabilirsiniz. Tam HF alanı depolarını da indirebilirsiniz, ancak bu seçenek çok kararlı değil 😕

        2. Şimdi, 'TTS'den R.V.C.'yi değiştirin' seçeneğini işaretleyin ✅ Bundan sonra, her TTS konuşucusuna uygulamak istediğiniz modelleri seçebilirsiniz 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Tüm R.V.C.'lere uygulanacak F0 yöntemini ayarlayın 🎛️

        4. Yaptığınız değişiklikleri uygulamak için 'YAPILAN AYARLARI UYGULA' düğmesine basın 🔄

        5. Video çevirisi sekmesine geri dönün ve 'Çevir' düğmesine tıklayın ▶️ Artık çeviri, R.V.C. uygulanarak yapılacaktır 🗣️

        İpucu: En iyi TTS'leri veya yapılandırmaları R.V.C.'ye uygulamak için 'Test R.V.C.'yi kullanabilirsiniz 🧪🔍

        ---

        """,
        "tab_translate": "Video çevirisi",
        "video_source": "Video Kaynağını Seçin",
        "link_label": "Medya bağlantısı.",
        "link_info": "Örnek: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL buraya girin...",
        "dir_label": "Video Yolu.",
        "dir_info": "Örnek: /usr/home/my_video.mp4",
        "dir_ph": "Yol buraya girin...",
        "sl_label": "Kaynak dil",
        "sl_info": "Videoyun orijinal dilidir",
        "tat_label": "Şuna çevir",
        "tat_info": "Hedef dili seçin ve ayrıca o dil için uygun metin-okuma-sesini seçtiğinizden emin olun.",
        "num_speakers": "Videoda kaç kişi konuşuyor seçin.",
        "min_sk": "Min konuşmacılar",
        "max_sk": "Max konuşmacılar",
        "tts_select": "Her konuşmacı için istediğiniz sesi seçin.",
        "sk1": "TTS Konuşmacı 1",
        "sk2": "TTS Konuşmacı 2",
        "sk3": "TTS Konuşmacı 3",
        "sk4": "TTS Konuşmacı 4",
        "sk5": "TTS Konuşmacı 5",
        "sk6": "TTS Konuşmacı 6",
        "sk7": "TTS Konuşmacı 7",
        "sk8": "TTS Konuşmacı 8",
        "sk9": "TTS Konuşmacı 9",
        "sk10": "TTS Konuşmacı 10",
        "sk11": "TTS Konuşmacı 11",
        "sk12": "TTS Konuşmacı 12",
        "vc_title": "Farklı Dillerde Ses Taklidi",
        "vc_subtitle": """
        ### Bir kişinin sesini çeşitli dillere yayın.
        Uygun şekilde kullanıldığında çoğu sesle etkili olsa da, her durumda mükemmelliği elde etmeyebilir.
        Ses Taklidi yalnızca referans konuşucunun tonunu çoğaltır, aksan ve duygu dışında,
        temel konuşucu TTS modeli tarafından yönetilen ve dönüştürücü tarafından çoğaltılmayanlar hariç.
        Bu, her konuşmacı için ana ses kaydından ses örnekleri alır ve işler.
        """,
        "vc_active_label": "Aktif Ses Taklidi",
        "vc_active_info": "Aktif Ses Taklidi: Orijinal konuşmacının tonunu çoğaltır",
        "vc_method_label": "Yöntem",
        "vc_method_info": "Ses Taklidi işlemi için bir yöntem seçin",
        "vc_segments_label": "Maksimum örnekler",
        "vc_segments_info": "Maksimum örnekler: İşlem için üretilecek ses örneklerinin sayısıdır, daha fazlası daha iyidir ancak gürültü ekleyebilir",
        "vc_dereverb_label": "Yankıyı Azalt",
        "vc_dereverb_info": "Yankıyı Azalt: Ses örneklerine yankı azaltma uygular.",
        "vc_remove_label": "Önceki örnekleri Kaldır",
        "vc_remove_info": "Önceki örnekleri Kaldır: Önceki üretilen örnekleri kaldırır, bu nedenle yeni olanları oluşturmak gerekir.",
        "xtts_title": "Bir ses tabanlı TTS oluştur",
        "xtts_subtitle": "Sesli bir sesle en fazla 10 saniyelik bir ses dosyası yükleyin. XTTS kullanarak, sağlanan ses dosyasına benzer bir sesle yeni bir TTS oluşturulur.",
        "xtts_file_label": "Sesli bir sesle kısa bir ses dosyası yükleyin",
        "xtts_name_label": "TTS için bir isim belirleyin",
        "xtts_name_info": "Basit bir isim kullanın",
        "xtts_dereverb_label": "Sesi Yankıdan Temizle",
        "xtts_dereverb_info": "Sesi Yankıdan Temizle: Sese yankı azaltma uygular",
        "xtts_button": "Ses işleme ve TTS seçimine dahil et",
        "xtts_footer": "Ses xtts otomatik olarak oluştur: TTS seçicisinde `_XTTS_/AUTOMATIC.wav`ı kullanarak, çeviri oluştururken her konuşmacı için otomatik olarak bölümler oluşturabilirsiniz.",
        "extra_setting": "Gelişmiş Ayarlar",
        "acc_max_label": "Maksimum Ses Hızlandırması",
        "acc_max_info": "Çakışmayı önlemek için çevrilen ses segmentlerinin maksimum hızlandırması. 1.0 değeri hiçbir hızlandırmayı temsil eder",
        "acc_rate_label": "Hızlanma Oranı Düzenlemesi",
        "acc_rate_info": "Hızlanma Oranı Düzenlemesi: Daha az hız gerektiren segmentlere uyum sağlamak için hızlanmayı ayarlar, sürekliliği korur ve sonraki başlangıç zamanını dikkate alır.",
        "or_label": "Örtüşme Azaltma",
        "or_info": "Örtüşme Azaltma: Önceki bitiş zamanlarına dayanarak başlangıç zamanlarını ayarlayarak segmentlerin örtüşmesini engeller; senkronizasyonu bozabilir.",
        "aud_mix_label": "Ses Karıştırma Yöntemi",
        "aud_mix_info": "Özgün ve çevrilmiş ses dosyalarını karıştırarak iki kullanılabilir karıştırma moduyla özelleştirilmiş, dengeli bir çıkış oluşturun.",
        "vol_ori": "Özgün ses seviyesi",
        "vol_tra": "Çevrilmiş ses seviyesi",
        "voiceless_tk_label": "Sessiz Parça",
        "voiceless_tk_info": "Sessiz Parça: Çevrilmiş sesle birleştirilmeden önce özgün sesleri kaldırır.",
        "sub_type": "Altyazı türü",
        "soft_subs_label": "Yumuşak Altyazılar",
        "soft_subs_info": "Yumuşak Altyazılar: İzleyicilerin video izlerken açıp kapatabileceği isteğe bağlı altyazılar.",
        "burn_subs_label": "Altyazıyı Yak",
        "burn_subs_info": "Altyazıyı Yak: Altyazıları videoya gömerek, bunları görsel içeriğin kalıcı bir parçası haline getirir.",
        "whisper_title": "Transkripsiyonu yapılandır.",
        "lnum_label": "Sayıları Metinleştir",
        "lnum_info": "Sayıları Metinleştir: Transkript içindeki sayısal temsilleri yazılı eşdeğerleriyle değiştirin.",
        "scle_label": "Ses Temizliği",
        "scle_info": "Ses Temizliği: Zaman damgası hassasiyeti için transkripsiyondan önce sesleri iyileştirin, arka plan gürültüsünü kaldırın. Bu işlem özellikle uzun ses dosyalarıyla zaman alabilir.",
        "sd_limit_label": "Bölüm Süresi Sınırı",
        "sd_limit_info": "Her bölüm için maksimum süreyi (saniye cinsinden) belirtin. Ses, her bölüm parçası için süreyi sınırlayarak VAD kullanılarak işlenecektir.",
        "asr_model_info": "Varsayılan olarak 'Fısıldama modeli'ni kullanarak konuşma dilini metne dönüştürür. Özel bir model kullanın, örneğin, özel bir model kullanmak için açılan menüye 'BELLE-2/Belle-whisper-large-v3-zh' depo adını girin. Hugging Face'de ince ayarlı modeller bulun.",
        "ctype_label": "Hesaplama Türü",
        "ctype_info": "int8 veya float16 gibi daha küçük tipleri seçmek, bellek kullanımını azaltarak ve hesaplama verimliliğini artırarak performansı artırabilir, ancak float32 gibi daha büyük veri tiplerine göre hassasiyetten ödün verebilir.",
        "batchz_label": "Toplu İş Boyutu",
        "batchz_info": "GPU'nuzun daha az VRAM'a sahip olması durumunda toplu iş boyutunu azaltmak bellek tasarrufu sağlar ve Bellek Dışı Sorunları yönetmeye yardımcı olur.",
        "tsscale_label": "Metin Bölme Ölçeği",
        "tsscale_info": "Metni cümleler, kelimeler veya karakterler olarak bölümlere ayırın. Kelime ve karakter bölme, altyazılar için faydalı olan daha ince granülerlik sağlar; çeviriyi devre dışı bırakma, orijinal yapının korunmasını sağlar.",
        "srt_file_label": "Bir SRT altyazı dosyası yükleyin (Whisper'ın transkripsiyonu yerine kullanılacaktır)",
        "divide_text_label": "Metin bölümlerini yeniden böl:",
        "divide_text_info": "(Deneysel) Mevcut metin segmentlerini kaynak dildeki ayraçla bölmek için bir ayraç girin. Aracı, bu ayraçları tanımlayacak ve buna göre yeni segmentler oluşturacaktır. Birden çok ayıraç belirtmek için | kullanın, örn .: !|?|...|。",
        "diarization_label": "Diyarizasyon Modeli",
        "tr_process_label": "Çeviri Süreci",
        "out_type_label": "Çıkış Türü",
        "out_name_label": "Dosya adı",
        "out_name_info": "Çıkış dosyasının adı",
        "task_sound_label": "Görev Durumu Ses",
        "task_sound_info": "Görev Durumu Ses: Görev tamamlanması veya yürütme sırasında hataları belirten bir ses uyarısı çalar.",
        "cache_label": "İlerlemeyi Getir",
        "cache_info": "İlerlemeyi Getir: Son kontrol noktasından işlemi devam ettir.",
        "preview_info": "Önizleme, test amaçları için videonun sadece 10 saniyelik kısmını keser. Lütfen tam video süresini almak için önizlemeyi devre dışı bırakın.",
        "edit_sub_label": "Oluşturulan altyazıları düzenleyin",
        "edit_sub_info": "Oluşturulan altyazıları düzenlemeyi sağlar: Çeviriyi 2 adımda çalıştırmanıza izin verir. İlk olarak 'ALTYAZILARI AL VE DÜZENLE' düğmesiyle altyazıları alır, bunları düzenleyebilir ve ardından 'ÇEVİR' düğmesine tıklayarak videoyu oluşturabilirsiniz",
        "button_subs": "ALTYAZILARI AL VE DÜZENLE",
        "editor_sub_label": "Oluşturulan altyazılar",
        "editor_sub_info": "Burada oluşturulan altyazılardaki metni düzenleyebilirsiniz. Arayüz seçeneklerinde değişiklikler yapabilirsiniz, ancak 'Kaynak dil', 'Şuna çevir' ve 'Max konuşmacılar' dışında hata oluşmaması için 'ÇEVİR' düğmesine basmadan önce. Bitirdiğinizde, 'ÇEVİR' düğmesine tıklayın.",
        "editor_sub_ph": "Altyazıları almak için önce 'ALTYAZILARI AL VE DÜZENLE'ye basın",
        "button_translate": "ÇEVİR",
        "output_result_label": "ÇEVİRİLEN VİDEOYU İNDİR",
        "sub_ori": "Altyazılar",
        "sub_tra": "Çevrilmiş altyazılar",
        "ht_token_info": "Bir önemli adım, Pyannote kullanım lisans anlaşmasını kabul etmektir. Modelleri kullanmak için Hugging Face'de bir hesabınız olması ve lisansı kabul etmeniz gerekir: https://huggingface.co/pyannote/speaker-diarization ve https://huggingface.co/pyannote/segmentation. Anahtar JETONUNUZU buradan alın: https://hf.co/settings/tokens",
        "ht_token_ph": "Jetona buradan girin...",
        "tab_docs": "Belge çevirisi",
        "docs_input_label": "Belge Kaynağını Seçin",
        "docs_input_info": "PDF, DOCX, TXT veya metin olabilir",
        "docs_source_info": "Bu, metnin orijinal dilidir",
        "chunk_size_label": "TTS'nin her segment başına işleyeceği maksimum karakter sayısı",
        "chunk_size_info": "0 değeri, TTS için dinamik ve daha uyumlu bir değer atar.",
        "docs_button": "Dil Dönüşüm Köprüsünü Başlat",
        "cv_url_info": "R.V.C. modellerini otomatik olarak URL'den indirin. HuggingFace veya Drive bağlantılarını kullanabilir ve her birini virgülle ayırarak birden çok bağlantı ekleyebilirsiniz. Örnek: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Ses: TTS'den R.V.C.'ye Değiştir",
        "sec1_title": "### 1. Kullanımını etkinleştirmek için onu işaretleyin.",
        "enable_replace": "Modellerin kullanımını etkinleştirmek için bunu işaretleyin.",
        "sec2_title": "### 2. Her karşılık gelen konuşmacı TTS'sine uygulanacak bir ses seçin ve yapılandırmaları uygulayın.",
        "sec2_subtitle": "Kullanacağınız <TTS Konuşmacısı> sayısına bağlı olarak, her biri kendi modeline ihtiyaç duyar. Ayrıca, konuşmacı doğru şekilde tespit edilmezse, bir yardımcı model de bulunmaktadır.",
        "cv_tts1": "Konuşmacı 1 için uygulanacak sesi seçin.",
        "cv_tts2": "Konuşmacı 2 için uygulanacak sesi seçin.",
        "cv_tts3": "Konuşmacı 3 için uygulanacak sesi seçin.",
        "cv_tts4": "Konuşmacı 4 için uygulanacak sesi seçin.",
        "cv_tts5": "Konuşmacı 5 için uygulanacak sesi seçin.",
        "cv_tts6": "Konuşmacı 6 için uygulanacak sesi seçin.",
        "cv_tts7": "Konuşmacı 7 için uygulanacak sesi seçin.",
        "cv_tts8": "Konuşmacı 8 için uygulanacak sesi seçin.",
        "cv_tts9": "Konuşmacı 9 için uygulanacak sesi seçin.",
        "cv_tts10": "Konuşmacı 10 için uygulanacak sesi seçin.",
        "cv_tts11": "Konuşmacı 11 için uygulanacak sesi seçin.",
        "cv_tts12": "Konuşmacı 12 için uygulanacak sesi seçin.",
        "cv_aux": "- Konuşmacı doğru şekilde algılanamadığında uygulanacak ses.",
        "cv_button_apply": "AYARLARI UYGULA",
        "tab_help": "Yardım",
    },
    "indonesian": {
        "description": """
        ### 🎥 **Terjemahkan video dengan mudah menggunakan SoniTranslate!** 📽️

        Unggah video, file audio, atau berikan tautan YouTube. 📽️ **Dapatkan buku catatan yang diperbarui dari repositori resmi: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Lihat tab `Bantuan` untuk petunjuk penggunaan. Mari mulai bersenang-senang dengan menerjemahkan video! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Petunjuk penggunaan:**

        1. 📤 Unggah sebuah **video**, **file audio** atau berikan sebuah tautan 🌐 **YouTube.**

        2. 🌍 Pilih bahasa di mana Anda ingin **menerjemahkan video** tersebut.

        3. 🗣️ Tentukan **jumlah orang yang berbicara** dalam video dan **berikan masing-masing suara teks-ke-suara yang sesuai** untuk bahasa terjemahan.

        4. 🚀 Tekan tombol '**Terjemahkan**' untuk mendapatkan hasilnya.

        ---

        # 🧩 **SoniTranslate mendukung berbagai mesin TTS (Teks-ke-Suara), yaitu:**
        - EDGE-TTS → format `en-AU-WilliamNeural-Male` → Cepat dan akurat.
        - FACEBOOK MMS → format `en-facebook-mms VITS` → Suara lebih alami; saat ini, hanya menggunakan CPU.
        - PIPER TTS → format `en_US-lessac-high VITS-onnx` → Sama seperti sebelumnya, tetapi dioptimalkan untuk CPU dan GPU.
        - BARK → format `en_speaker_0-Male BARK` → Kualitas bagus tetapi lambat, dan rentan terhadap halusinasi.
        - OpenAI TTS → format `>alloy OpenAI-TTS` → Multibahasa tetapi membutuhkan OpenAI API key
        - Coqui XTTS → format `_XTTS_/AUTOMATIC.wav` → Hanya tersedia untuk Cina (Sederhana), Inggris, Prancis, Jerman, Italia, Portugis, Polandia, Turki, Rusia, Belanda, Ceko, Arab, Spanyol, Hungaria, Korea, dan Jepang.

        ---

        # 🎤 Cara Menggunakan Suara R.V.C. dan R.V.C.2 (Opsional) 🎶

        Tujuannya adalah menerapkan R.V.C. pada TTS yang dihasilkan (Teks-ke-Suara) 🎙️

        1. Di tab `Suara Kustom R.V.C.`, unduh model-model yang Anda butuhkan 📥 Anda dapat menggunakan tautan dari Hugging Face dan Google Drive dalam format zip, pth, atau index. Anda juga dapat mengunduh repositori ruang HF lengkap, tetapi opsi ini tidak sangat stabil 😕

        2. Sekarang, pergi ke `Ganti suara: TTS ke R.V.C.` dan centang kotak `aktifkan` ✅ Setelah ini, Anda dapat memilih model yang ingin Anda terapkan pada setiap pembicara TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Sesuaikan metode F0 yang akan diterapkan pada semua R.V.C. 🎛️

        4. Tekan `TERAPKAN KONFIGURASI` untuk menerapkan perubahan yang Anda buat 🔄

        5. Kembali ke tab terjemahan video dan klik 'Terjemahkan' ▶️ Sekarang, terjemahan akan dilakukan dengan menerapkan R.V.C. 🗣️

        Tip: Anda dapat menggunakan `Uji R.V.C.` untuk bereksperimen dan menemukan TTS atau konfigurasi terbaik untuk diterapkan pada R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Terjemahan Video",
        "video_source": "Pilih Sumber Video",
        "link_label": "Tautan Media.",
        "link_info": "Contoh: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL masukkan di sini...",
        "dir_label": "Path Video.",
        "dir_info": "Contoh: /usr/home/my_video.mp4",
        "dir_ph": "Path masukkan di sini...",
        "sl_label": "Bahasa Sumber",
        "sl_info": "Ini adalah bahasa asli video",
        "tat_label": "Terjemahkan audio ke",
        "tat_info": "Pilih bahasa target dan pastikan juga memilih TTS yang sesuai untuk bahasa tersebut.",
        "num_speakers": "Pilih berapa banyak orang yang berbicara dalam video.",
        "min_sk": "Pembicara minimum",
        "max_sk": "Pembicara maksimum",
        "tts_select": "Pilih suara yang Anda inginkan untuk setiap pembicara.",
        "sk1": "Pembicara TTS 1",
        "sk2": "Pembicara TTS 2",
        "sk3": "Pembicara TTS 3",
        "sk4": "Pembicara TTS 4",
        "sk5": "Pembicara TTS 5",
        "sk6": "Pembicara TTS 6",
        "sk7": "Pembicara TTS 7",
        "sk8": "Pembicara TTS 8",
        "sk9": "Pembicara TTS 9",
        "sk10": "Pembicara TTS 10",
        "sk11": "Pembicara TTS 11",
        "sk12": "Pembicara TTS 12",
        "vc_title": "Imitasi Suara dalam Berbagai Bahasa",
        "vc_subtitle": """
        ### Reproduksi suara seseorang di berbagai bahasa.
        Meskipun efektif dengan kebanyakan suara ketika digunakan dengan tepat, mungkin tidak mencapai kesempurnaan dalam setiap kasus.
        Imitasi Suara hanya mereproduksi nada pembicara referensi, mengecualikan aksen dan emosi, yang dikendalikan oleh model TTS pembicara dasar dan tidak direplikasi oleh konverter.
        Ini akan mengambil sampel audio dari audio utama untuk setiap pembicara dan memprosesnya.
        """,
        "vc_active_label": "Imitasi Suara Aktif",
        "vc_active_info": "Imitasi Suara Aktif: Mereplikasi nada pembicara asli",
        "vc_method_label": "Metode",
        "vc_method_info": "Pilih metode untuk proses Imitasi Suara",
        "vc_segments_label": "Sampel maksimum",
        "vc_segments_info": "Sampel maksimum: Jumlah sampel audio yang akan dihasilkan untuk proses, semakin banyak lebih baik tetapi dapat menambah noise",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Menyertakan dereverb vokal ke sampel audio.",
        "vc_remove_label": "Hapus sampel sebelumnya",
        "vc_remove_info": "Hapus sampel sebelumnya: Menghapus sampel sebelumnya yang dihasilkan, sehingga yang baru perlu dibuat.",
        "xtts_title": "Buat TTS berdasarkan audio",
        "xtts_subtitle": "Unggah file audio dengan durasi maksimal 10 detik dengan suara. Dengan menggunakan XTTS, TTS baru akan dibuat dengan suara mirip dengan file audio yang diberikan.",
        "xtts_file_label": "Unggah audio pendek dengan suara",
        "xtts_name_label": "Nama untuk TTS",
        "xtts_name_info": "Gunakan nama sederhana",
        "xtts_dereverb_label": "Dereverb audio",
        "xtts_dereverb_info": "Dereverb audio: Menyertakan dereverb vokal ke audio",
        "xtts_button": "Proses audio dan masukkan ke dalam pemilih TTS",
        "xtts_footer": "Hasilkan xtts suara secara otomatis: Anda dapat menggunakan `_XTTS_/AUTOMATIC.wav` di pemilih TTS untuk secara otomatis menghasilkan segmen untuk setiap pembicara saat menghasilkan terjemahan.",
        "extra_setting": "Pengaturan Lanjutan",
        "acc_max_label": "Akselerasi Audio maksimum",
        "acc_max_info": "Akselerasi maksimum untuk segmen audio yang diterjemahkan untuk menghindari tumpang tindih. Nilai 1.0 mewakili tidak ada akselerasi",
        "acc_rate_label": "Regulasi Tingkat Akselerasi",
        "acc_rate_info": "Regulasi Tingkat Akselerasi: Menyesuaikan akselerasi untuk mengakomodasi segmen yang membutuhkan kecepatan lebih rendah, menjaga kontinuitas, dan mempertimbangkan waktu mulai berikutnya.",
        "or_label": "Pengurangan Tumpang Tindih",
        "or_info": "Pengurangan Tumpang Tindih: Memastikan segmen tidak tumpang tindih dengan menyesuaikan waktu mulai berdasarkan waktu selesai sebelumnya; bisa mengganggu sinkronisasi.",
        "aud_mix_label": "Metode Penggabungan Audio",
        "aud_mix_info": "Gabungkan file audio asli dan diterjemahkan untuk membuat output yang seimbang dengan dua mode pencampuran yang tersedia.",
        "vol_ori": "Volume audio asli",
        "vol_tra": "Volume audio yang diterjemahkan",
        "voiceless_tk_label": "Track Tanpa Suara",
        "voiceless_tk_info": "Track Tanpa Suara: Hapus suara audio asli sebelum menggabungkannya dengan audio yang diterjemahkan.",
        "sub_type": "Tipe Subtitle",
        "soft_subs_label": "Subtitel Lembut",
        "soft_subs_info": "Subtitel Lembut: Subtitel opsional yang dapat ditonton penonton saat menonton video.",
        "burn_subs_label": "Bakar Subtitle",
        "burn_subs_info": "Bakar Subtitle: Menyematkan subtitle ke dalam video, menjadikannya bagian permanen dari konten visual.",
        "whisper_title": "Konfigurasi transkripsi.",
        "lnum_label": "Literalisasi Angka",
        "lnum_info": "Literalisasi Angka: Gantikan representasi numerik dengan ekivalen tertulisnya dalam transkrip.",
        "scle_label": "Pembersihan Suara",
        "scle_info": "Pembersihan Suara: Tingkatkan vokal, hapus kebisingan latar belakang sebelum transkripsi untuk presisi timestamp maksimum. Operasi ini bisa memakan waktu, terutama dengan file audio yang panjang.",
        "sd_limit_label": "Batas Durasi Segment",
        "sd_limit_info": "Tentukan durasi maksimum (dalam detik) untuk setiap segmen. Audio akan diproses menggunakan VAD, membatasi durasi untuk setiap potongan segmen.",
        "asr_model_info": "Ini mengubah bahasa yang diucapkan menjadi teks menggunakan model 'Whisper' secara default. Gunakan model kustom, misalnya, dengan memasukkan nama repositori 'BELLE-2/Belle-whisper-large-v3-zh' dalam dropdown untuk menggunakan model yang disesuaikan bahasa Cina. Temukan model yang disesuaikan di Hugging Face.",
        "ctype_label": "Jenis Perhitungan",
        "ctype_info": "Memilih tipe yang lebih kecil seperti int8 atau float16 dapat meningkatkan kinerja dengan mengurangi penggunaan memori dan meningkatkan throughput komputasi, tetapi dapat mengorbankan presisi dibandingkan dengan tipe data yang lebih besar seperti float32.",
        "batchz_label": "Ukuran Batch",
        "batchz_info": "Mengurangi ukuran batch menghemat memori jika GPU Anda memiliki VRAM yang lebih sedikit dan membantu mengelola masalah Out of Memory.",
        "tsscale_label": "Skala Segmentasi Teks",
        "tsscale_info": "Bagi teks menjadi segmen berdasarkan kalimat, kata, atau karakter. Segmentasi kata dan karakter menawarkan granularitas yang lebih halus, berguna untuk subjudul; menonaktifkan terjemahan mempertahankan struktur asli.",
        "srt_file_label": "Unggah file subtitle SRT (akan digunakan sebagai gantinya dari transkripsi Whisper)",
        "divide_text_label": "Bagi ulang segmen teks dengan:",
        "divide_text_info": "(Eksperimental) Masukkan pemisah untuk membagi segmen teks yang ada dalam bahasa sumber. Alat ini akan mengidentifikasi kejadian dan membuat segmen baru sesuai. Tentukan beberapa pemisah menggunakan |, misalnya: !|?|...|。",
        "diarization_label": "Model Diarization",
        "tr_process_label": "Proses Penerjemahan",
        "out_type_label": "Jenis Output",
        "out_name_label": "Nama file",
        "out_name_info": "Nama file output",
        "task_sound_label": "Suara Status Tugas",
        "task_sound_info": "Suara Status Tugas: Memainkan suara peringatan yang menandakan penyelesaian tugas atau kesalahan selama pelaksanaan.",
        "cache_label": "Pemulihan Kemajuan",
        "cache_info": "Pemulihan Kemajuan: Melanjutkan proses dari titik kontrol terakhir.",
        "preview_info": "Pratinjau memotong video menjadi hanya 10 detik untuk tujuan pengujian. Harap nonaktifkan untuk mendapatkan durasi video penuh.",
        "edit_sub_label": "Edit subtitle yang dihasilkan",
        "edit_sub_info": "Edit subtitle yang dihasilkan: Memungkinkan Anda menjalankan terjemahan dalam 2 langkah. Pertama dengan tombol 'DAPATKAN SUBTITLES DAN EDIT', Anda mendapatkan subtitle untuk diedit, dan kemudian dengan tombol 'TERJEMAHKAN', Anda dapat menghasilkan video",
        "button_subs": "DAPATKAN SUBTITLES DAN EDIT",
        "editor_sub_label": "Subtitle yang dihasilkan",
        "editor_sub_info": "Silakan sunting teks dalam subtitle yang dihasilkan di sini. Anda dapat membuat perubahan pada opsi antarmuka sebelum mengklik tombol 'TERJEMAHKAN', kecuali untuk 'Bahasa Sumber', 'Terjemahkan audio ke', dan 'Pembicara maksimum', untuk menghindari kesalahan. Setelah selesai, klik tombol 'TERJEMAHKAN'.",
        "editor_sub_ph": "Pertama tekan 'DAPATKAN SUBTITLES DAN EDIT' untuk mendapatkan subtitle",
        "button_translate": "TERJEMAHKAN",
        "output_result_label": "UNDUH VIDEO TERJEMAHAN",
        "sub_ori": "Subtitle",
        "sub_tra": "Subtitle Terjemahan",
        "ht_token_info": "Langkah penting adalah menerima perjanjian lisensi untuk menggunakan Pyannote. Anda perlu memiliki akun di Hugging Face dan menerima lisensi untuk menggunakan model: https://huggingface.co/pyannote/speaker-diarization dan https://huggingface.co/pyannote/segmentation. Dapatkan TOKEN KUNCI Anda di sini: https://hf.co/settings/tokens",
        "ht_token_ph": "Token masukkan di sini...",
        "tab_docs": "Terjemahan Dokumen",
        "docs_input_label": "Pilih Sumber Dokumen",
        "docs_input_info": "Ini bisa berupa PDF, DOCX, TXT, atau teks",
        "docs_source_info": "Ini adalah bahasa asli teks",
        "chunk_size_label": "Jumlah maksimum karakter yang akan diproses oleh TTS per segmen",
        "chunk_size_info": "Nilai 0 menetapkan nilai dinamis dan lebih kompatibel untuk TTS.",
        "docs_button": "Mulai Jembatan Konversi Bahasa",
        "cv_url_info": "Unduh model R.V.C. secara otomatis dari URL. Anda dapat menggunakan tautan dari HuggingFace atau Drive, dan Anda dapat menyertakan beberapa tautan, masing-masing dipisahkan oleh koma. Contoh: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Ganti suara: TTS ke R.V.C.",
        "sec1_title": "### 1. Untuk mengaktifkan penggunaannya, tandai sebagai aktif.",
        "enable_replace": "Centang ini untuk mengaktifkan penggunaan model.",
        "sec2_title": "### 2. Pilih suara yang akan diterapkan untuk setiap TTS dari setiap pembicara yang sesuai dan terapkan konfigurasinya.",
        "sec2_subtitle": "Tergantung pada berapa banyak <Pembicara TTS> yang akan Anda gunakan, masing-masing memerlukan model yang sesuai. Selain itu, ada satu tambahan jika dengan beberapa alasan pembicara tidak terdeteksi dengan benar.",
        "cv_tts1": "Pilih suara yang akan diterapkan untuk Pembicara 1.",
        "cv_tts2": "Pilih suara yang akan diterapkan untuk Pembicara 2.",
        "cv_tts3": "Pilih suara yang akan diterapkan untuk Pembicara 3.",
        "cv_tts4": "Pilih suara yang akan diterapkan untuk Pembicara 4.",
        "cv_tts5": "Pilih suara yang akan diterapkan untuk Pembicara 5.",
        "cv_tts6": "Pilih suara yang akan diterapkan untuk Pembicara 6.",
        "cv_tts7": "Pilih suara yang akan diterapkan untuk Pembicara 7.",
        "cv_tts8": "Pilih suara yang akan diterapkan untuk Pembicara 8.",
        "cv_tts9": "Pilih suara yang akan diterapkan untuk Pembicara 9.",
        "cv_tts10": "Pilih suara yang akan diterapkan untuk Pembicara 10.",
        "cv_tts11": "Pilih suara yang akan diterapkan untuk Pembicara 11.",
        "cv_tts12": "Pilih suara yang akan diterapkan untuk Pembicara 12.",
        "cv_aux": "- Suara yang akan diterapkan jika Pembicara tidak terdeteksi dengan sukses.",
        "cv_button_apply": "TERAPKAN KONFIGURASI",
        "tab_help": "Bantuan",
    },
    "portuguese": {
        "description": """
        ### 🎥 **Traduza vídeos facilmente com o SoniTranslate!** 📽️

        Carregue um vídeo, arquivo de áudio ou forneça um link do YouTube. 📽️ **Obtenha o caderno atualizado do repositório oficial: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Consulte a guia `Ajuda` para instruções sobre como usá-lo. Vamos começar a nos divertir com a tradução de vídeos! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Instruções de uso:**

        1. 📤 Carregue um **vídeo**, **arquivo de áudio** ou forneça um 🌐 **link do YouTube**.

        2. 🌍 Escolha o idioma para o qual você deseja **traduzir o vídeo**.

        3. 🗣️ Especifique o **número de pessoas falando** no vídeo e **atribua a cada uma uma voz de texto para fala** adequada ao idioma da tradução.

        4. 🚀 Pressione o botão '**Traduzir**' para obter os resultados.

        ---

        # 🧩 **SoniTranslate suporta diferentes motores TTS (Texto para Fala), que são:**
        - EDGE-TTS → formato `en-AU-WilliamNeural-Male` → Rápido e preciso.
        - FACEBOOK MMS → formato `en-facebook-mms VITS` → A voz é mais natural; no momento, usa apenas CPU.
        - PIPER TTS → formato `en_US-lessac-high VITS-onnx` → O mesmo que o anterior, mas é otimizado para CPU e GPU.
        - BARK → formato `en_speaker_0-Male BARK` → Boa qualidade, mas lento e propenso a alucinações.
        - OpenAI TTS → formato `>alloy OpenAI-TTS` → Multilíngue mas requer uma OpenAI API key
        - Coqui XTTS → formato `_XTTS_/AUTOMATIC.wav` → Disponível apenas para Chinês (Simplificado), Inglês, Francês, Alemão, Italiano, Português, Polonês, Turco, Russo, Holandês, Tcheco, Árabe, Espanhol, Húngaro, Coreano e Japonês.

        ---

        # 🎤 Como Usar Vozes R.V.C. e R.V.C.2 (Opcional) 🎶

        O objetivo é aplicar um R.V.C. ao TTS (Texto para Fala) gerado 🎙️

        1. Na aba `Voz Personalizada R.V.C.`, baixe os modelos que você precisa 📥 Você pode usar links do Hugging Face e Google Drive em formatos como zip, pth ou índice. Você também pode baixar repositórios completos do espaço HF, mas essa opção não é muito estável 😕

        2. Agora, vá para `Substituir voz: TTS para R.V.C.` e marque a caixa de seleção `habilitar` ✅ Após isso, você pode escolher os modelos que deseja aplicar a cada falante TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Ajuste o método F0 que será aplicado a todos os R.V.C. 🎛️

        4. Pressione `APLICAR CONFIGURAÇÃO` para aplicar as alterações feitas 🔄

        5. Volte para a aba de tradução de vídeo e clique em 'Traduzir' ▶️ Agora, a tradução será feita aplicando o R.V.C. 🗣️

        Dica: Você pode usar `Testar R.V.C.` para experimentar e encontrar o melhor TTS ou configurações para aplicar ao R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Tradução de Vídeo",
        "video_source": "Escolha a Fonte do Vídeo",
        "link_label": "Link do Mídia.",
        "link_info": "Exemplo: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL aqui...",
        "dir_label": "Caminho do Vídeo.",
        "dir_info": "Exemplo: /usr/home/meu_video.mp4",
        "dir_ph": "Caminho aqui...",
        "sl_label": "Idioma de Origem",
        "sl_info": "Este é o idioma original do vídeo",
        "tat_label": "Traduzir áudio para",
        "tat_info": "Selecione o idioma de destino e também certifique-se de escolher o TTS correspondente para esse idioma.",
        "num_speakers": "Selecione quantas pessoas estão falando no vídeo.",
        "min_sk": "Mín. falantes",
        "max_sk": "Máx. falantes",
        "tts_select": "Selecione a voz desejada para cada falante.",
        "sk1": "Falante TTS 1",
        "sk2": "Falante TTS 2",
        "sk3": "Falante TTS 3",
        "sk4": "Falante TTS 4",
        "sk5": "Falante TTS 5",
        "sk6": "Falante TTS 6",
        "sk7": "Falante TTS 7",
        "sk8": "Falante TTS 8",
        "sk9": "Falante TTS 9",
        "sk10": "Falante TTS 10",
        "sk11": "Falante TTS 11",
        "sk12": "Falante TTS 12",
        "vc_title": "Imitação de Voz em Diferentes Idiomas",
        "vc_subtitle": """
        ### Reproduza a voz de uma pessoa em vários idiomas.
        Embora eficaz com a maioria das vozes quando usada adequadamente, pode não alcançar a perfeição em todos os casos.
        A Imitação de Voz replica apenas o tom do falante de referência, excluindo sotaque e emoção, que são governados pelo modelo TTS do falante base e não replicados pelo conversor.
        Isso pegará amostras de áudio do áudio principal para cada falante e as processará.
        """,
        "vc_active_label": "Ativar Imitação de Voz",
        "vc_active_info": "Ativar Imitação de Voz: Replica o tom do falante original",
        "vc_method_label": "Método",
        "vc_method_info": "Selecione um método para o processo de Imitação de Voz",
        "vc_segments_label": "Máx. amostras",
        "vc_segments_info": "Máx. amostras: É o número de amostras de áudio que serão geradas para o processo, mais é melhor, mas pode adicionar ruído",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Aplica dereverb vocal às amostras de áudio.",
        "vc_remove_label": "Remover amostras anteriores",
        "vc_remove_info": "Remover amostras anteriores: Remove as amostras geradas anteriormente, então novas precisam ser criadas.",
        "xtts_title": "Criar um TTS baseado em um áudio",
        "xtts_subtitle": "Carregue um arquivo de áudio de no máximo 10 segundos com uma voz. Usando o XTTS, um novo TTS será criado com uma voz semelhante ao arquivo de áudio fornecido.",
        "xtts_file_label": "Carregar um áudio curto com a voz",
        "xtts_name_label": "Nome para o TTS",
        "xtts_name_info": "Use um nome simples",
        "xtts_dereverb_label": "Dereverb do áudio",
        "xtts_dereverb_info": "Dereverb do áudio: Aplica dereverb vocal ao áudio",
        "xtts_button": "Processar o áudio e incluí-lo no seletor de TTS",
        "xtts_footer": "Gerar voz xtts automaticamente: Você pode usar `_XTTS_/AUTOMATIC.wav` no seletor de TTS para gerar automaticamente segmentos para cada falante ao gerar a tradução.",
        "extra_setting": "Configurações Avançadas",
        "acc_max_label": "Máx. Aceleração de Áudio",
        "acc_max_info": "Aceleração máxima para segmentos de áudio traduzidos para evitar sobreposições. Um valor de 1.0 representa nenhuma aceleração",
        "acc_rate_label": "Regulação da Taxa de Aceleração",
        "acc_rate_info": "Regulação da Taxa de Aceleração: Ajusta a aceleração para acomodar segmentos que exigem menos velocidade, mantendo a continuidade e considerando o tempo de próximo início.",
        "or_label": "Redução de sobreposição",
        "or_info": "Redução de sobreposição: Garante que os segmentos não se sobreponham ajustando os horários de início com base nos horários de término anteriores; pode perturbar a sincronização.",
        "aud_mix_label": "Método de Mistura de Áudio",
        "aud_mix_info": "Misture arquivos de áudio original e traduzido para criar uma saída personalizada e equilibrada com dois modos de mistura disponíveis.",
        "vol_ori": "Volume do áudio original",
        "vol_tra": "Volume do áudio traduzido",
        "voiceless_tk_label": "Faixa sem Voz",
        "voiceless_tk_info": "Faixa sem Voz: Remova as vozes de áudio originais antes de combiná-las com o áudio traduzido.",
        "sub_type": "Tipo de Legenda",
        "soft_subs_label": "Legendas Suaves",
        "soft_subs_info": "Legendas Suaves: Legendas opcionais que os espectadores podem ligar ou desligar enquanto assistem ao vídeo.",
        "burn_subs_label": "Queimar Legendas",
        "burn_subs_info": "Queimar Legendas: Incorporar legendas no vídeo, tornando-as uma parte permanente do conteúdo visual.",
        "whisper_title": "Configurar transcrição.",
        "lnum_label": "Literalizar Números",
        "lnum_info": "Literalizar Números: Substituir representações numéricas por seus equivalentes escritos na transcrição.",
        "scle_label": "Limpeza de Som",
        "scle_info": "Limpeza de Som: Aprimorar vocais, remover ruído de fundo antes da transcrição para máxima precisão de marcação de tempo. Esta operação pode levar tempo, especialmente com arquivos de áudio longos.",
        "sd_limit_label": "Limite de Duração do Segmento",
        "sd_limit_info": "Especifique a duração máxima (em segundos) para cada segmento. O áudio será processado usando VAD, limitando a duração para cada fragmento de segmento.",
        "asr_model_info": "Ele converte linguagem falada em texto usando o modelo 'Whisper' por padrão. Use um modelo personalizado, por exemplo, inserindo o nome do repositório 'BELLE-2/Belle-whisper-large-v3-zh' no menu suspenso para utilizar um modelo em chinês finetuned. Encontre modelos finetuned na Hugging Face.",
        "ctype_label": "Tipo de Cálculo",
        "ctype_info": "Escolher tipos menores como int8 ou float16 pode melhorar o desempenho, reduzindo o uso de memória e aumentando o throughput computacional, mas pode sacrificar a precisão em comparação com tipos de dados maiores como float32.",
        "batchz_label": "Tamanho do Lote",
        "batchz_info": "Reduzir o tamanho do lote economiza memória se sua GPU tiver menos VRAM e ajuda a gerenciar problemas de Memória Insuficiente.",
        "tsscale_label": "Escala de Segmentação de Texto",
        "tsscale_info": "Divida o texto em segmentos por frases, palavras ou caracteres. A segmentação por palavras e caracteres oferece granularidade mais fina, útil para legendas; desativar a tradução preserva a estrutura original.",
        "srt_file_label": "Carregar um arquivo de legenda SRT (será usado em vez da transcrição de Whisper)",
        "divide_text_label": "Redividir segmentos de texto por:",
        "divide_text_info": "(Experimental) Insira um separador para dividir os segmentos de texto existentes no idioma de origem. A ferramenta identificará as ocorrências e criará novos segmentos conforme necessário. Especifique vários separadores usando |, por exemplo: !|?|...|。",
        "diarization_label": "Modelo de Diarização",
        "tr_process_label": "Processo de Tradução",
        "out_type_label": "Tipo de Saída",
        "out_name_label": "Nome do Arquivo",
        "out_name_info": "O nome do arquivo de saída",
        "task_sound_label": "Som do Estado da Tarefa",
        "task_sound_info": "Som do Estado da Tarefa: Reproduz um alerta sonoro indicando a conclusão da tarefa ou erros durante a execução.",
        "cache_label": "Recuperar Progresso",
        "cache_info": "Recuperar Progresso: Continuar processo a partir do último checkpoint.",
        "preview_info": "A prévia corta o vídeo para apenas 10 segundos para fins de teste. Por favor, desative para recuperar a duração completa do vídeo.",
        "edit_sub_label": "Editar legendas geradas",
        "edit_sub_info": "Editar legendas geradas: Permite executar a tradução em 2 etapas. Primeiro, com o botão 'OBTER LEGENDAS E EDITAR', você obtém as legendas para editá-las, e depois, com o botão 'TRADUZIR', você pode gerar o vídeo",
        "button_subs": "OBTER LEGENDAS E EDITAR",
        "editor_sub_label": "Legendas geradas",
        "editor_sub_info": "Sinta-se à vontade para editar o texto nas legendas geradas aqui. Você pode fazer alterações nas opções de interface antes de clicar no botão 'TRADUZIR', exceto para 'Idioma de Origem', 'Traduzir áudio para' e 'Max. falantes', para evitar erros. Quando terminar, clique no botão 'TRADUZIR'.",
        "editor_sub_ph": "Primeiro pressione 'OBTER LEGENDAS E EDITAR' para obter as legendas",
        "button_translate": "TRADUZIR",
        "output_result_label": "BAIXAR VÍDEO TRADUZIDO",
        "sub_ori": "Legendas Originais",
        "sub_tra": "Legendas Traduzidas",
        "ht_token_info": "Um passo importante é aceitar o acordo de licença para usar o Pyannote. Você precisa ter uma conta no Hugging Face e aceitar a licença para usar os modelos: https://huggingface.co/pyannote/speaker-diarization e https://huggingface.co/pyannote/segmentation. Obtenha seu TOKEN CHAVE aqui: https://hf.co/settings/tokens",
        "ht_token_ph": "Token aqui...",
        "tab_docs": "Tradução de Documentos",
        "docs_input_label": "Escolha a Fonte do Documento",
        "docs_input_info": "Pode ser PDF, DOCX, TXT ou texto",
        "docs_source_info": "Este é o idioma original do texto",
        "chunk_size_label": "Máx. número de caracteres que o TTS processará por segmento",
        "chunk_size_info": "Um valor de 0 atribui um valor dinâmico e mais compatível para o TTS.",
        "docs_button": "Iniciar Ponte de Conversão de Idioma",
        "cv_url_info": "Baixe automaticamente os modelos R.V.C. do URL. Você pode usar links do HuggingFace ou Drive, e pode incluir vários links, cada um separado por uma vírgula. Exemplo: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Substituir voz: TTS para R.V.C.",
        "sec1_title": "### 1. Para habilitar seu uso, marque como habilitado.",
        "enable_replace": "Marque isso para habilitar o uso dos modelos.",
        "sec2_title": "### 2. Selecione uma voz que será aplicada a cada TTS de cada falante correspondente e aplique as configurações.",
        "sec2_subtitle": "Dependendo de quantos <Falante TTS> você usará, cada um precisa do seu respectivo modelo. Além disso, há um auxiliar se, por algum motivo, o falante não for detectado corretamente.",
        "cv_tts1": "Escolha a voz para aplicar ao Falante 1.",
        "cv_tts2": "Escolha a voz para aplicar ao Falante 2.",
        "cv_tts3": "Escolha a voz para aplicar ao Falante 3.",
        "cv_tts4": "Escolha a voz para aplicar ao Falante 4.",
        "cv_tts5": "Escolha a voz para aplicar ao Falante 5.",
        "cv_tts6": "Escolha a voz para aplicar ao Falante 6.",
        "cv_tts7": "Escolha a voz para aplicar ao Falante 7.",
        "cv_tts8": "Escolha a voz para aplicar ao Falante 8.",
        "cv_tts9": "Escolha a voz para aplicar ao Falante 9.",
        "cv_tts10": "Escolha a voz para aplicar ao Falante 10.",
        "cv_tts11": "Escolha a voz para aplicar ao Falante 11.",
        "cv_tts12": "Escolha a voz para aplicar ao Falante 12.",
        "cv_aux": "- Voz para aplicar caso um Falante não seja detectado com sucesso.",
        "cv_button_apply": "APLICAR CONFIGURAÇÃO",
        "tab_help": "Ajuda",
    },
    "hindi": {
        "description": """
          ### 🎥 **SoniTranslate के साथ वीडियो को आसानी से अनुवादित करें!** 📽️

          एक वीडियो, ऑडियो फ़ाइल अपलोड करें या एक YouTube लिंक प्रदान करें। 📽️ **आधिकारिक भंडार से अपडेटेड नोटबुक प्राप्त करें: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

          उसे 'मदद' टैब देखें इसका उपयोग कैसे करना है के निर्देशों के लिए। वीडियो अनुवाद के साथ मज़े करना शुरू करें! 🚀🎉
          """,
        "tutorial": """
          # 🔰 **उपयोग के लिए निर्देश:**

          1. 📤 **वीडियो**, **ऑडियो फ़ाइल** अपलोड करें या एक 🌐 **YouTube लिंक** प्रदान करें।

          2. 🌍 चुनें कि आप किस भाषा में **वीडियो को अनुवादित** करना चाहते हैं।

          3. 🗣️ वीडियो में **बोलने वाले लोगों की संख्या** और **प्रत्येक को टेक्स्ट-टू-स्पीच आवाज** देने का निर्देश दें, जो अनुवाद भाषा के लिए उपयुक्त है।

          4. 🚀 '**अनुवाद**' बटन दबाएं और परिणाम प्राप्त करें।

          ---

          # 🧩 **SoniTranslate विभिन्न TTS (टेक्स्ट-टू-स्पीच) इंजनों का समर्थन करता है, जो हैं:**
          - EDGE-TTS → प्रारूप `en-AU-WilliamNeural-Male` → तेज़ और सटीक।
          - FACEBOOK MMS → प्रारूप `en-facebook-mms VITS` → आवाज अधिक प्राकृतिक है; वर्तमान में, यह केवल CPU का उपयोग करता है।
          - PIPER TTS → प्रारूप `en_US-lessac-high VITS-onnx` → पिछले वाले के समान, लेकिन यह CPU और GPU दोनों के लिए अनुकूलित है।
          - BARK → प्रारूप `en_speaker_0-Male BARK` → अच्छी गुणवत्ता है लेकिन धीमी, और यह हैलुसिनेशन के लिए प्रवृत्त है।
          - OpenAI TTS → प्रारूप `>alloy OpenAI-TTS` → बहुभाषी लेकिन इसमें एक OpenAI API key की आवश्यकता है
          - Coqui XTTS → प्रारूप `_XTTS_/AUTOMATIC.wav` → केवल चीनी (सरलीकृत), अंग्रेजी, फ्रेंच, जर्मन, इतालवी, पुर्तगाली, पोलिश, तुर्की, रूसी, डच, चेक, अरबी, स्पैनिश, हंगेरियन, कोरियाई और जापानी के लिए ही उपलब्ध है।

          ---

          # 🎤 R.V.C. और R.V.C.2 आवाज़ों का उपयोग कैसे करें (वैकल्पिक) 🎶

          लक्ष्य है कि जेनेरेटेड TTS (टेक्स्ट-टू-स्पीच) पर एक R.V.C. लागू करें 🎙️

          1. `कस्टम आवाज़ आर.वी.सी.` टैब में, आपको आवश्यक मॉडल डाउनलोड करने की आवश्यकता है 📥 आप हग्गिंग फेस और गूगल ड्राइव से लिंक्स का उपयोग कर सकते हैं जैसे zip, pth, या इंडेक्स के प्रारूप में। आप पूरे एचएफ स्पेस रिपॉज़िटरी को भी डाउनलोड कर सकते हैं, लेकिन यह विकल्प बहुत ही अस्थिर है 😕

          2. अब, `आवाज़ बदलें: TTS से R.V.C.` पर जाएं और `सक्रिय` बॉक्स को चेक करें ✅ इसके बाद, आप प्रत्येक TTS बोलने वाले को लागू करने के लिए जो आप चाहते हैं उसे चुन सकते हैं 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

          3. सभी R.V.C. पर लागू किया जाने वाला F0 विधि समायोजित करें 🎛️

          4. आपके द्वारा किए गए परिवर्तनों को लागू करने के लिए `आवेदन को लागू करें` दबाएं 🔄

          5. वीडियो अनुवाद टैब पर वापस जाएं और 'अनुवाद करें' पर क्लिक करें ▶️ अब, अनुवाद R.V.C. को लागू करते हुए किया जाएगा। 🗣️

          सुझाव: आप `टेस्ट R.V.C.` का उपयोग करके प्रयोग कर सकते हैं और R.V.C. को लागू करने के लिए सर्वोत्तम TTS या कॉन्फ़िगरेशन खोज सकते हैं। 🧪🔍

          ---

          """,
        "tab_translate": "वीडियो अनुवाद",
        "video_source": "वीडियो स्रोत चुनें",
        "link_label": "मीडिया लिंक।",
        "link_info": "उदाहरण: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL यहाँ डालें...",
        "dir_label": "वीडियो पथ।",
        "dir_info": "उदाहरण: /usr/home/my_video.mp4",
        "dir_ph": "पथ यहाँ डालें...",
        "sl_label": "स्रोत भाषा",
        "sl_info": "यह वीडियो की मूल भाषा है",
        "tat_label": "ऑडियो को अनुवाद करें",
        "tat_info": "लक्ष्य भाषा का चयन करें और सुनिश्चित करें कि उस भाषा के लिए संबंधित TTS चुना गया है।",
        "num_speakers": "वीडियो में कितने लोग बोल रहे हैं, उन्हें चुनें।",
        "min_sk": "न्यूनतम बोलने वाले",
        "max_sk": "अधिकतम बोलने वाले",
        "tts_select": "प्रत्येक बोलने वाले के लिए आप जो आवाज़ चाहते हैं, उसे चुनें।",
        "sk1": "TTS बोलने वाला 1",
        "sk2": "TTS बोलने वाला 2",
        "sk3": "TTS बोलने वाला 3",
        "sk4": "TTS बोलने वाला 4",
        "sk5": "TTS बोलने वाला 5",
        "sk6": "TTS बोलने वाला 6",
        "sk7": "TTS बोलने वाला 7",
        "sk8": "TTS बोलने वाला 8",
        "sk9": "TTS बोलने वाला 9",
        "sk10": "TTS बोलने वाला 10",
        "sk11": "TTS बोलने वाला 11",
        "sk12": "TTS बोलने वाला 12",
        "vc_title": "विभिन्न भाषाओं में आवाज़ का नकल",
        "vc_subtitle": """
          ### विभिन्न भाषाओं में एक व्यक्ति की आवाज़ का नकल।
          जब सही ढंग से प्रयोग किया जाता है, तो अधिकांश आवाज़ों के साथ प्रभावी है, लेकिन हर मामले में पूर्णता को हासिल नहीं कर सकता है।
          आवाज़ का नकल केवल संदर्भ वक्ता के टोन को प्रतिलिपि करता है, एक्सेंट और भावना को बाहर करता है, जो आधार वक्ता TTS मॉडल द्वारा नियंत्रित होता है और कनवर्टर द्वारा प्रतिलिपि नहीं किया जाता है।
          यह मुख्य ऑडियो के लिए ऑडियो नमूने लेता है और प्रसंस्करण करता है।
          """,
        "vc_active_label": "सक्रिय आवाज़ का नकल",
        "vc_active_info": "सक्रिय आवाज़ का नकल: मूल बोलने वाले के टोन को प्रतिलिपि करता है",
        "vc_method_label": "विधि",
        "vc_method_info": "आवाज़ का नकल प्रक्रिया के लिए एक विधि का चयन करें",
        "vc_segments_label": "अधिकतम सैंपल",
        "vc_segments_info": "अधिकतम सैंपल: प्रक्रिया के लिए ऑडियो सैंपलों की संख्या है, अधिक बेहतर है, लेकिन यह शोर जोड़ सकता है",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: ऑडियो सैंपलों पर ध्वनि dereverb लागू करता है।",
        "vc_remove_label": "पिछले सैंपल हटाएं",
        "vc_remove_info": "पिछले सैंपल हटाएं: पिछले सैंपल हटा देता है: ताकि नए सैंपल उत्पन्न किए जाने की आवश्यकता हो।",
        "xtts_title": "ऑडियो पर आधारित TTS बनाएं",
        "xtts_subtitle": "एक ऑडियो फ़ाइल को अधिकतम 10 सेकंड के साथ एक आवाज़ के साथ अपलोड करें। XTTS का उपयोग करके, एक नया TTS बनाया जाएगा जो प्रदान की गई ऑडियो फ़ाइल के समान होगा।",
        "xtts_file_label": "आवाज़ के साथ एक छोटा ऑडियो अपलोड करें",
        "xtts_name_label": "TTS के लिए नाम",
        "xtts_name_info": "एक सरल नाम का उपयोग करें",
        "xtts_dereverb_label": "Dereverb ऑडियो",
        "xtts_dereverb_info": "Dereverb ऑडियो: ऑडियो पर ध्वनि dereverb लागू करें",
        "xtts_button": "ऑडियो प्रक्रिया करें और इसे TTS सेलेक्टर में शामिल करें",
        "xtts_footer": "स्वचालित रूप से आवाज़ xtts उत्पन्न करें: अनुवाद उत्पन्न करते समय प्रत्येक बोलने वाले के लिए सेगमेंट ऑटोमेटिकली उत्पन्न करने के लिए आप `_XTTS_/AUTOMATIC.wav` का उपयोग कर सकते हैं।",
        "extra_setting": "उन्नत सेटिंग्स",
        "acc_max_label": "अधिकतम ऑडियो त्वरण",
        "acc_max_info": "ओवरलैपिंग से बचने के लिए अनुवादित ऑडियो सेगमेंटों के लिए अधिकतम त्वरण। 1.0 का मान कोई त्वरण नहीं दर्शाता है।",
        "acc_rate_label": "त्वरण दर नियामक",
        "acc_rate_info": "त्वरण दर नियामक: त्वरण को समायोजित करता है ताकि उपभागों को उससे कम गति की आवश्यकता हो, सततता को बनाए रखते हुए और अगले आरंभ के समय को ध्यान में रखते हुए।",
        "or_label": "ओवरलैप कमी करना",
        "or_info": "ओवरलैप कमी करना: पिछले समाप्ति समयों के आधार पर शुरुआत समयों को समायोजित करके सेगमेंट को ओवरलैप नहीं होने देता है; समवारण को बिगाड़ सकता है।",
        "aud_mix_label": "ऑडियो मिश्रण विधि",
        "aud_mix_info": "मूल और अनुवादित ऑडियो फ़ाइलों को मिश्रित करें और दो उपलब्ध मिश्रण मोड के साथ एक अनुकूलित, संतुलित उत्पादन बनाएं।",
        "vol_ori": "मूल ऑडियो ध्वनि",
        "vol_tra": "अनुवादित ऑडियो ध्वनि",
        "voiceless_tk_label": "वॉइसलेस ट्रैक",
        "voiceless_tk_info": "अनुवादित ऑडियो के साथ इसे मिलाने से पहले मूल ऑडियो ध्वनियों को हटाएं।",
        "sub_type": "उपशीर्षक प्रकार",
        "soft_subs_label": "मुलायम सबटाइटल्स",
        "soft_subs_info": "मुलायम सबटाइटल्स: व्यूअर्स वीडियो देखते समय चाहें तो चालू या बंद कर सकते हैं।",
        "burn_subs_label": "उपशीर्षक जलाएं",
        "burn_subs_info": "उपशीर्षक जलाएं: वीडियो में उपशीर्षक एम्बेड करें, जिससे वे दृश्यीय सामग्री का स्थायी हिस्सा बन जाएं।",
        "whisper_title": "कॉन्फ़िगर ट्रांस्क्रिप्शन।",
        "lnum_label": "संख्याओं का वाचक रूपांतरण",
        "lnum_info": "संख्याओं का वाचक रूपांतरण: संख्यात्मक प्रतिनिधित्वों को उनके लेखित समकक्षों से प्रतिस्थापित करें ट्रांसक्रिप्ट में।",
        "scle_label": "ध्वनि की सफाई",
        "scle_info": "ध्वनि की सफाई: अधिकतम समयचिह्न सटीकता के लिए ध्वनि को बेहतर बनाएं, समय चिह्नों की अधिकता के लिए अधिकतम समयचिह्न सटीकता के लिए पीछे की ध्वनि हटाएं। इस ऑपरेशन में समय लग सकता है, खासकर लंबे ऑडियो फ़ाइलों के साथ।",
        "sd_limit_label": "सेगमेंट अवधि सीमा",
        "sd_limit_info": "प्रत्येक सेगमेंट की अधिकतम अवधि (सेकंड में) को निर्दिष्ट करें। ऑडियो को वैड का उपयोग करके प्रोसेस किया जाएगा, प्रत्येक सेगमेंट चंक की अवधि को सीमित करके।",
        "asr_model_info": "यह डिफ़ॉल्ट रूप से बोली भाषा को पाठ में परिवर्तित करता है 'व्हिस्पर मॉडल' का उपयोग करके। अपना कस्टम मॉडल उपयोग करें, उदाहरण के लिए, ड्रॉपडाउन में रिपॉज़िटरी नाम 'BELLE-2/Belle-whisper-large-v3-zh' दर्ज करके एक चीनी भाषा फ़ाइन ट्यून मॉडल का उपयोग करें। Hugging Face पर फ़ाइन ट्यून मॉडल्स पाएँ।",
        "ctype_label": "हिसाब प्रकार",
        "ctype_info": "छोटे प्रकारों जैसे int8 या फ़्लोट16 का चयन करना प्रदर्शन को बढ़ावा दे सकता है, मेमोरी उपयोग को कम करके और गणनात्मक परिचालन बढ़ाकर प्रदर्शन को सुधार सकता है, लेकिन float32 जैसे बड़े डेटा प्रकारों की तुलना में निश्चितता को कट्टरता में बदल सकता है।",
        "batchz_label": "बैच का आकार",
        "batchz_info": "यदि आपके पास कम VRAM वाली जीपीयू है, तो बैच का आकार कम करने से मेमोरी बचाई जा सकती है और मेमोरी की कमी की समस्याओं का प्रबंधन किया जा सकता है।",
        "tsscale_label": "पाठ के विभाजन का पैमाना",
        "tsscale_info": "पाठ को वाक्य, शब्द या अक्षरों के आधार पर खंडों में विभाजित करें। शब्द और अक्षर विभाजन और लघु ग्रेन्युलरिटी प्रदान करता है, जो उपशीर्षकों के लिए उपयोगी है; अनुवाद को अक्षम करने से मूल संरचना को संरक्षित रखा जाता है।",
        "srt_file_label": "एक SRT उपशीर्षक फ़ाइल अपलोड करें (विस्पर की प्रतिलिपि के बजाय इस्तेमाल की जाएगी)",
        "divide_text_label": "पुनः विभाजित करें टेक्स्ट सेगमेंट द्वारा:",
        "divide_text_info": "(प्रयोगात्मक) मौजूदा पाठ सेगमेंट को विभाजित करने के लिए एक विभाजक दर्ज करें। उपकरण को घटनाओं को पहचानने और उन्हें अनुसार नए सेगमेंट बनाने के लिए। | का उपयोग करके एक से अधिक विभाजक निर्दिष्ट करें, उदा।: !|?|...|。",
        "diarization_label": "डायरिज़ेशन मॉडल",
        "tr_process_label": "अनुवाद प्रक्रिया",
        "out_type_label": "आउटपुट प्रकार",
        "out_name_label": "फ़ाइल का नाम",
        "out_name_info": "आउटपुट फ़ाइल का नाम",
        "task_sound_label": "कार्य स्थिति ध्वनि",
        "task_sound_info": "कार्य स्थिति ध्वनि: कार्य समाप्ति या क्रिया के दौरान त्रुटियों की सूचना देने वाला ध्वनि चलाता है।",
        "cache_label": "प्रगति पुनः प्राप्त करें",
        "cache_info": "प्रगति पुनः प्राप्त करें: पिछले चेकप्वाइंट से प्रक्रिया जारी रखें।",
        "preview_info": "पूर्णत: अधिकतम 10 सेकंड के लिए वीडियो काटता है परीक्षण के उद्देश्यों के लिए। कृपया इसे निष्क्रिय करें ताकि पूरा वीडियो अवधि प्राप्त की जा सके।",
        "edit_sub_label": "उत्पन्न उपशीर्षक संपादित करें",
        "edit_sub_info": "उत्पन्न उपशीर्षक संपादित करें: आपको 2 चरणों में अनुवाद चलाने की अनुमति देता है। पहले 'GET SUBTITLES AND EDIT' बटन के साथ, आप उन्हें संपादित करने के लिए उपशीर्षक प्राप्त करते हैं, और फिर 'TRANSLATE' बटन के साथ, आप वीडियो उत्पन्न कर सकते हैं",
        "button_subs": "GET SUBTITLES AND EDIT",
        "editor_sub_label": "उत्पन्न उपशीर्षक",
        "editor_sub_info": "यहाँ उत्पन्न उपशीर्षक में पाठ संपादित करने के लिए स्वतंत्र महसूस करें। आप इंटरफ़ेस विकल्पों में परिवर्तन कर सकते हैं, 'TRANSLATE' बटन पर क्लिक करने से पहले, 'Source language', 'Translate audio to' और 'Max speakers', त्रुटियों से बचने के लिए, 'TRANSLATE' बटन पर क्लिक करें। जब आप समाप्त हो जाएं, 'TRANSLATE' बटन पर क्लिक करें।",
        "editor_sub_ph": "पहले 'GET SUBTITLES AND EDIT' दबाएं ताकि उपशीर्षक प्राप्त हो",
        "button_translate": "TRANSLATE",
        "output_result_label": "अनुवादित वीडियो डाउनलोड करें",
        "sub_ori": "उपशीर्षक",
        "sub_tra": "अनुवादित उपशीर्षक",
        "ht_token_info": "एक महत्वपूर्ण कदम है प्यानोट का उपयोग करने के लिए लाइसेंस समझ। आपको Hugging Face पर एक खाता होना चाहिए और मॉडल का उपयोग करने के लिए लाइसेंस स्वीकार करने की आवश्यकता है: https://huggingface.co/pyannote/speaker-diarization और https://huggingface.co/pyannote/segmentation। अपना KEY TOKEN यहाँ प्राप्त करें: https://hf.co/settings/tokens",
        "ht_token_ph": "टोकन यहाँ जाता है...",
        "tab_docs": "दस्तावेज़ अनुवाद",
        "docs_input_label": "दस्तावेज़ स्रोत चुनें",
        "docs_input_info": "यह PDF, DOCX, TXT, या पाठ हो सकता है",
        "docs_source_info": "यह पाठ की मूल भाषा है",
        "chunk_size_label": "प्रति सेगमेंट TTS द्वारा प्रसंस्कृत किए जाने वाले अधिकतम अक्षरों की संख्या",
        "chunk_size_info": "0 का मान एक गतिशील और और संगतिपूर्ण मान को TTS के लिए सौंपता है।",
        "docs_button": "भाषा परिवर्तन सेतु शुरू करें",
        "cv_url_info": "URL से R.V.C. मॉडल आपमूर्त डाउनलोड करें। आप HuggingFace या Drive से लिंक का उपयोग कर सकते हैं, और आप कई लिंक शामिल कर सकते हैं, प्रत्येक को अल्पविराम द्वारा अलग किया जा सकता है। उदाहरण: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "आवाज़ को बदलें: TTS से R.V.C.",
        "sec1_title": "### 1. इसका उपयोग सक्षम करने के लिए, इसे सक्षम करें के रूप में चिह्नित करें।",
        "enable_replace": "मॉडल का उपयोग सक्षम करने के लिए इसे चेक करें।",
        "sec2_title": "### 2. प्रत्येक संबंधित बोलने वाले के प्रत्येक TTS को लागू करने के लिए एक आवाज़ का चयन करें और विन्यास लागू करें।",
        "sec2_subtitle": "आपके पास कितने <TTS बोलने वाले> हैं, इस पर निर्भर करता है, प्रत्येक को उसका संबंधित मॉडल चाहिए। विशेषज्ञ नहीं पाया गया है।",
        "cv_tts1": "बोलने वाले 1 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts2": "बोलने वाले 2 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts3": "बोलने वाले 3 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts4": "बोलने वाले 4 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts5": "बोलने वाले 5 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts6": "बोलने वाले 6 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts7": "बोलने वाले 7 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts8": "बोलने वाले 8 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts9": "बोलने वाले 9 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts10": "बोलने वाले 10 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts11": "बोलने वाले 11 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_tts12": "बोलने वाले 12 के लिए लागू करने के लिए आवाज़ चुनें।",
        "cv_aux": "- यदि किसी कारणवश स्पीकर सही ढंग से पहचाना नहीं गया है, तो लागू करने के लिए आवाज़।",
        "cv_button_apply": "आवेदन को लागू करें",
        "tab_help": "सहायता",
    },
    "vietnamese": {
        "description": """
        ### 🎥 **Dịch video dễ dàng với SoniTranslate!** 📽️

        Tải lên một video, tập tin âm thanh hoặc cung cấp một liên kết YouTube. 📽️ **Nhận sổ tay cập nhật từ kho chính thức: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Xem tab `Trợ giúp` để biết hướng dẫn cách sử dụng. Hãy bắt đầu vui vẻ với việc dịch video! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Hướng dẫn sử dụng:**

        1. 📤 Tải lên một **video**, **tập tin âm thanh** hoặc cung cấp một 🌐 **liên kết YouTube**.

        2. 🌍 Chọn ngôn ngữ bạn muốn **dịch video** sang.

        3. 🗣️ Chỉ định **số người nói** trong video và **gán mỗi người một giọng nói chuyển văn bản** phù hợp cho ngôn ngữ dịch.

        4. 🚀 Nhấn nút '**Dịch**' để nhận kết quả.

        ---

        # 🧩 **SoniTranslate hỗ trợ các công cụ TTS (Text-to-Speech) khác nhau, bao gồm:**
        - EDGE-TTS → định dạng `en-AU-WilliamNeural-Male` → Nhanh và chính xác.
        - FACEBOOK MMS → định dạng `en-facebook-mms VITS` → Giọng nói tự nhiên hơn; hiện tại chỉ sử dụng CPU.
        - PIPER TTS → định dạng `en_US-lessac-high VITS-onnx` → Giống như cái trước, nhưng được tối ưu hóa cho cả CPU và GPU.
        - BARK → định dạng `en_speaker_0-Male BARK` → Chất lượng tốt nhưng chậm, và dễ bị ảo giác.
        - OpenAI TTS → định dạng `>alloy OpenAI-TTS` → Đa ngôn ngữ nhưng cần một OpenAI API key
        - Coqui XTTS → định dạng `_XTTS_/AUTOMATIC.wav` → Chỉ có sẵn cho tiếng Trung (Giản thể), tiếng Anh, tiếng Pháp, tiếng Đức, tiếng Ý, tiếng Bồ Đào Nha, tiếng Ba Lan, tiếng Thổ Nhĩ Kỳ, tiếng Nga, tiếng Hà Lan, tiếng Séc, tiếng Ả Rập, tiếng Tây Ban Nha, tiếng Hungary, tiếng Hàn và tiếng Nhật.

        ---

        # 🎤 Cách Sử Dụng Giọng R.V.C. và R.V.C.2 (Tùy chọn) 🎶

        Mục tiêu là áp dụng một R.V.C. vào TTS (Text-to-Speech) được tạo ra 🎙️

        1. Trong tab `Giọng Tùy chỉnh R.V.C.`, tải xuống các mô hình bạn cần 📥 Bạn có thể sử dụng các liên kết từ Hugging Face và Google Drive ở các định dạng như zip, pth, hoặc index. Bạn cũng có thể tải xuống các kho HF hoàn chỉnh, nhưng tùy chọn này không ổn định lắm 😕

        2. Bây giờ, đi đến `Thay thế giọng: TTS thành R.V.C.` và đánh dấu vào hộp `enable` ✅ Sau đó, bạn có thể chọn các mô hình bạn muốn áp dụng cho mỗi người nói TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Điều chỉnh phương pháp F0 sẽ được áp dụng cho tất cả R.V.C. 🎛️

        4. Nhấn `APPLY CONFIGURATION` để áp dụng các thay đổi bạn đã thực hiện 🔄

        5. Quay lại tab dịch video và nhấp vào 'Dịch' ▶️ Bây giờ, dịch sẽ được thực hiện áp dụng R.V.C. 🗣️

        Mẹo: Bạn có thể sử dụng `Kiểm tra R.V.C.` để thử nghiệm và tìm ra các TTS hoặc cấu hình tốt nhất để áp dụng vào R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Dịch video",
        "video_source": "Chọn Nguồn Video",
        "link_label": "Liên kết truyền thông.",
        "link_info": "Ví dụ: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "Đường dẫn URL vào đây...",
        "dir_label": "Đường dẫn Video.",
        "dir_info": "Ví dụ: /usr/home/my_video.mp4",
        "dir_ph": "Đường dẫn vào đây...",
        "sl_label": "Ngôn ngữ nguồn",
        "sl_info": "Đây là ngôn ngữ gốc của video",
        "tat_label": "Dịch âm thanh thành",
        "tat_info": "Chọn ngôn ngữ đích và đồng thời đảm bảo chọn TTS tương ứng cho ngôn ngữ đó.",
        "num_speakers": "Chọn số người nói trong video.",
        "min_sk": "Ít người nói",
        "max_sk": "Nhiều người nói",
        "tts_select": "Chọn giọng bạn muốn cho mỗi người nói.",
        "sk1": "Người Nói TTS 1",
        "sk2": "Người Nói TTS 2",
        "sk3": "Người Nói TTS 3",
        "sk4": "Người Nói TTS 4",
        "sk5": "Người Nói TTS 5",
        "sk6": "Người Nói TTS 6",
        "sk7": "Người Nói TTS 7",
        "sk8": "Người Nói TTS 8",
        "sk9": "Người Nói TTS 9",
        "sk10": "Người Nói TTS 10",
        "sk11": "Người Nói TTS 11",
        "sk12": "Người Nói TTS 12",
        "vc_title": "Sao chép giọng nói trong các ngôn ngữ khác nhau",
        "vc_subtitle": """
        ### Sao chép giọng nói của một người qua các ngôn ngữ khác nhau.
        Mặc dù hiệu quả với hầu hết các giọng nói khi sử dụng một cách phù hợp, nhưng không phải lúc nào cũng đạt được sự hoàn hảo trong mọi trường hợp.
        Sao chép giọng nói chỉ sao chép âm sắc của người tham chiếu, loại bỏ giọng địa phương và cảm xúc, được quản lý bởi mô hình TTS cơ bản và không được sao chép bởi bộ chuyển đổi.
        Điều này sẽ lấy mẫu âm thanh từ âm thanh chính cho mỗi người nói và xử lý chúng.
        """,
        "vc_active_label": "Kích hoạt Sao chép Giọng nói",
        "vc_active_info": "Kích hoạt Sao chép Giọng nói: Sao chép âm sắc của người nói gốc",
        "vc_method_label": "Phương pháp",
        "vc_method_info": "Chọn một phương pháp cho quá trình Sao chép Giọng nói",
        "vc_segments_label": "Mẫu tối đa",
        "vc_segments_info": "Mẫu tối đa: Là số lượng mẫu âm thanh sẽ được tạo ra cho quá trình, càng nhiều càng tốt nhưng có thể thêm tiếng ồn",
        "vc_dereverb_label": "Loại bỏ tiếng vang",
        "vc_dereverb_info": "Loại bỏ tiếng vang: Áp dụng loại bỏ tiếng vang vào các mẫu âm thanh.",
        "vc_remove_label": "Loại bỏ các mẫu trước",
        "vc_remove_info": "Loại bỏ các mẫu trước: Loại bỏ các mẫu đã tạo trước đó, vì vậy cần tạo mới.",
        "xtts_title": "Tạo TTS dựa trên một âm thanh",
        "xtts_subtitle": "Tải lên một tập tin âm thanh tối đa 10 giây với một giọng nói. Sử dụng XTTS, một TTS mới sẽ được tạo ra với một giọng nói tương tự như tập tin âm thanh được cung cấp.",
        "xtts_file_label": "Tải lên một âm thanh ngắn với giọng nói",
        "xtts_name_label": "Tên cho TTS",
        "xtts_name_info": "Sử dụng một tên đơn giản",
        "xtts_dereverb_label": "Loại bỏ tiếng vang âm thanh",
        "xtts_dereverb_info": "Loại bỏ tiếng vang âm thanh: Áp dụng loại bỏ tiếng vang âm thanh",
        "xtts_button": "Xử lý âm thanh và bao gồm nó trong trình chọn TTS",
        "xtts_footer": "Tạo TTS giọng nói tự động: Bạn có thể sử dụng `_XTTS_/AUTOMATIC.wav` trong trình chọn TTS để tự động tạo các đoạn cho mỗi người nói khi tạo dịch.",
        "extra_setting": "Cài Đặt Nâng Cao",
        "acc_max_label": "Tăng tốc âm thanh tối đa",
        "acc_max_info": "Tăng tốc tối đa cho các đoạn âm thanh dịch để tránh chồng chéo. Giá trị 1.0 đại diện cho không tăng tốc",
        "acc_rate_label": "Điều Chỉnh Tốc Độ Tăng Tốc",
        "acc_rate_info": "Điều Chỉnh Tốc Độ Tăng Tốc: Điều chỉnh tốc độ tăng tốc để phù hợp với các đoạn yêu cầu tốc độ thấp hơn, duy trì liên tục và xem xét thời gian bắt đầu tiếp theo.",
        "or_label": "Giảm chồng chéo",
        "or_info": "Giảm chồng chéo: Đảm bảo các đoạn không chồng chéo bằng cách điều chỉnh thời gian bắt đầu dựa trên thời gian kết thúc trước đó; có thể làm gián đoạn đồng bộ hóa.",
        "aud_mix_label": "Phương pháp Trộn Âm thanh",
        "aud_mix_info": "Trộn các tập tin âm thanh gốc và dịch để tạo ra một đầu ra cân bằng tùy chỉnh với hai chế độ trộn có sẵn.",
        "vol_ori": "Âm lượng âm thanh gốc",
        "vol_tra": "Âm lượng âm thanh dịch",
        "voiceless_tk_label": "Dạng Dữ liệu Không Có Giọng Nói",
        "voiceless_tk_info": "Dạng Dữ liệu Không Có Giọng Nói: Loại bỏ các giọng nói âm thanh gốc trước khi kết hợp nó với âm thanh dịch.",
        "sub_type": "Loại Phụ Đề",
        "soft_subs_label": "Phụ Đề Mềm",
        "soft_subs_info": "Phụ Đề Mềm: Phụ đề tùy chọn mà người xem có thể bật hoặc tắt trong khi xem video.",
        "burn_subs_label": "Đốt Phụ đề",
        "burn_subs_info": "Đốt Phụ đề: Nhúng phụ đề vào video, biến chúng thành một phần cố định của nội dung hình ảnh.",
        "whisper_title": "Cấu hình chuyển đổi.",
        "lnum_label": "Biểu Diễn Số Bằng Chữ",
        "lnum_info": "Biểu Diễn Số Bằng Chữ: Thay thế các biểu diễn số thành các tương đương viết của chúng trong bản ghi âm.",
        "scle_label": "Dọn Dẹp Âm Thanh",
        "scle_info": "Dọn Dẹp Âm Thanh: Nâng cao giọng nói, loại bỏ tiếng ồn nền trước khi chuyển đổi để đạt được độ chính xác cao nhất về dấu thời gian. Thao tác này có thể mất thời gian, đặc biệt là với các tệp âm thanh dài.",
        "sd_limit_label": "Giới Hạn Thời Lượng Đoạn",
        "sd_limit_info": "Chỉ định thời lượng tối đa (theo giây) cho mỗi đoạn. Âm thanh sẽ được xử lý bằng cách sử dụng VAD, giới hạn thời lượng cho mỗi đoạn.",
        "asr_model_info": "Nó chuyển đổi ngôn ngữ nói thành văn bản bằng cách sử dụng mô hình 'Whisper' theo mặc định. Sử dụng một mô hình tùy chỉnh, ví dụ, bằng cách nhập tên kho 'BELLE-2/Belle-whisper-large-v3-zh' trong danh sách thả xuống để sử dụng một mô hình đã được điều chỉnh cho ngôn ngữ Trung Quốc. Tìm mô hình đã điều chỉnh trên Hugging Face.",
        "ctype_label": "Loại Tính Toán",
        "ctype_info": "Lựa chọn các loại nhỏ hơn như int8 hoặc float16 có thể cải thiện hiệu suất bằng cách giảm việc sử dụng bộ nhớ và tăng thông lượng tính toán, nhưng có thể hy sinh độ chính xác so với các loại dữ liệu lớn hơn như float32.",
        "batchz_label": "Kích Thước Lô",
        "batchz_info": "Giảm kích thước lô giúp tiết kiệm bộ nhớ nếu GPU của bạn có ít VRAM và giúp quản lý các vấn đề Cạn Kiệt Bộ Nhớ.",
        "tsscale_label": "Thước Đo Phân Đoạn Văn Bản",
        "tsscale_info": "Chia văn bản thành các đoạn theo câu, từ hoặc ký tự. Phân đoạn theo từng từ và ký tự cung cấp độ mịn hơn, hữu ích cho phụ đề; vô hiệu hóa dịch thuật bảo tồn cấu trúc gốc.",
        "srt_file_label": "Tải lên một tập tin phụ đề SRT (sẽ được sử dụng thay vì việc chuyển đổi của Whisper)",
        "divide_text_label": "Chia lại đoạn văn bản bằng:",
        "divide_text_info": "(Thử nghiệm) Nhập một bộ phân cách để chia các đoạn văn bản hiện có trong ngôn ngữ nguồn. Công cụ sẽ nhận dạng các xuất hiện và tạo ra các đoạn mới tương ứng. Chỉ định nhiều bộ phân cách bằng |, ví dụ: !|?|...|。",
        "diarization_label": "Mô hình Phân tích",
        "tr_process_label": "Quy trình Dịch",
        "out_type_label": "Loại Đầu ra",
        "out_name_label": "Tên tập tin",
        "out_name_info": "Tên của tập tin đầu ra",
        "task_sound_label": "Âm thanh Trạng thái Nhiệm vụ",
        "task_sound_info": "Âm thanh Trạng thái Nhiệm vụ: Phát ra một cảnh báo âm thanh cho biết nhiệm vụ đã hoàn thành hoặc có lỗi trong quá trình thực thi.",
        "cache_label": "Lấy Tiến Trình",
        "cache_info": "Lấy Tiến Trình: Tiếp tục quá trình từ điểm kiểm soát cuối cùng.",
        "preview_info": "Xem trước cắt video chỉ 10 giây cho mục đích kiểm tra. Vui lòng tắt nó để lấy lại độ dài video đầy đủ.",
        "edit_sub_label": "Chỉnh sửa phụ đề đã tạo",
        "edit_sub_info": "Chỉnh sửa phụ đề đã tạo: Cho phép bạn chạy dịch trong 2 bước. Đầu tiên với nút 'NHẬN PHỤ ĐỀ VÀ CHỈNH SỬA', bạn nhận được phụ đề để chỉnh sửa chúng, và sau đó với nút 'DỊCH', bạn có thể tạo ra video",
        "button_subs": "NHẬN PHỤ ĐỀ VÀ CHỈNH SỬA",
        "editor_sub_label": "Phụ đề đã tạo",
        "editor_sub_info": "Hãy tự do chỉnh sửa văn bản trong phụ đề đã tạo ở đây. Bạn có thể thay đổi các tùy chọn giao diện trước khi nhấn nút 'DỊCH', ngoại trừ 'Ngôn ngữ nguồn', 'Dịch âm thanh thành', và 'Số người nói tối đa', để tránh lỗi. Khi bạn hoàn thành, nhấn nút 'DỊCH'.",
        "editor_sub_ph": "Đầu tiên nhấn 'NHẬN PHỤ ĐỀ VÀ CHỈNH SỬA' để nhận phụ đề",
        "button_translate": "DỊCH",
        "output_result_label": "TẢI VỀ VIDEO DỊCH",
        "sub_ori": "Phụ đề",
        "sub_tra": "Phụ đề dịch",
        "ht_token_info": "Một bước quan trọng là chấp nhận thỏa thuận giấy phép để sử dụng Pyannote. Bạn cần có một tài khoản trên Hugging Face và chấp nhận thỏa thuận giấy phép để sử dụng các mô hình: https://huggingface.co/pyannote/speaker-diarization và https://huggingface.co/pyannote/segmentation. Lấy KEY TOKEN của bạn tại đây: https://hf.co/settings/tokens",
        "ht_token_ph": "Token vào đây...",
        "tab_docs": "Dịch tài liệu",
        "docs_input_label": "Chọn Nguồn Tài Liệu",
        "docs_input_info": "Có thể là PDF, DOCX, TXT, hoặc văn bản",
        "docs_source_info": "Đây là ngôn ngữ gốc của văn bản",
        "chunk_size_label": "Số ký tự tối đa mà TTS sẽ xử lý cho mỗi đoạn",
        "chunk_size_info": "Giá trị 0 gán một giá trị động và tương thích hơn cho TTS.",
        "docs_button": "Bắt đầu Cầu Nối Chuyển Đổi Ngôn Ngữ",
        "cv_url_info": "Tự động tải xuống các mô hình R.V.C. từ URL. Bạn có thể sử dụng các liên kết từ HuggingFace hoặc Drive, và bạn có thể bao gồm nhiều liên kết, mỗi liên kết cách nhau bằng dấu phẩy. Ví dụ: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Thay thế giọng: TTS thành R.V.C.",
        "sec1_title": "### 1. Để kích hoạt việc sử dụng, đánh dấu nó như là kích hoạt.",
        "enable_replace": "Kiểm tra điều này để kích hoạt việc sử dụng các mô hình.",
        "sec2_title": "### 2. Chọn một giọng nói sẽ được áp dụng cho mỗi TTS của mỗi người nói tương ứng và áp dụng các cấu hình.",
        "sec2_subtitle": "Tùy thuộc vào số lượng <Người Nói TTS> bạn sẽ sử dụng, mỗi người cần một mô hình tương ứng của mình. Ngoài ra, còn có một mô hình phụ trợ nếu vì một lý do nào đó không nhận diện được người nói đúng cách.",
        "cv_tts1": "Chọn giọng nói áp dụng cho Người Nói 1.",
        "cv_tts2": "Chọn giọng nói áp dụng cho Người Nói 2.",
        "cv_tts3": "Chọn giọng nói áp dụng cho Người Nói 3.",
        "cv_tts4": "Chọn giọng nói áp dụng cho Người Nói 4.",
        "cv_tts5": "Chọn giọng nói áp dụng cho Người Nói 5.",
        "cv_tts6": "Chọn giọng nói áp dụng cho Người Nói 6.",
        "cv_tts7": "Chọn giọng nói áp dụng cho Người Nói 7.",
        "cv_tts8": "Chọn giọng nói áp dụng cho Người Nói 8.",
        "cv_tts9": "Chọn giọng nói áp dụng cho Người Nói 9.",
        "cv_tts10": "Chọn giọng nói áp dụng cho Người Nói 10.",
        "cv_tts11": "Chọn giọng nói áp dụng cho Người Nói 11.",
        "cv_tts12": "Chọn giọng nói áp dụng cho Người Nói 12.",
        "cv_aux": "- Giọng nói được áp dụng trong trường hợp không nhận diện được người nói thành công.",
        "cv_button_apply": "ÁP DỤNG CẤU HÌNH",
        "tab_help": "Trợ giúp",
    },
    "polish": {
        "description": """
        ### 🎥 **Łatwe tłumaczenie filmów dzięki SoniTranslate!** 📽️

        Prześlij film, plik dźwiękowy lub podaj link do YouTube. 📽️ **Pobierz aktualny notatnik ze strony oficjalnego repozytorium: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Zobacz zakładkę `Pomoc` w celu uzyskania instrukcji dotyczących korzystania z aplikacji. Zaczynajmy zabawę z tłumaczeniem filmów! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Instrukcje dotyczące użytkowania:**

        1. 📤 Prześlij **film**, **plik dźwiękowy** lub podaj 🌐 **link do YouTube**.

        2. 🌍 Wybierz język, na który chcesz **przetłumaczyć film**.

        3. 🗣️ Określ **liczbę osób mówiących** w filmie i **przypisz każdej z nich odpowiednią syntezę mowy tekstowej (TTS)** odpowiednią dla języka tłumaczenia.

        4. 🚀 Naciśnij przycisk '**Tłumacz**', aby uzyskać wyniki.

        ---

        # 🧩 **SoniTranslate obsługuje różne silniki TTS (tekst do mowy), które to:**
        - EDGE-TTS → format `en-AU-WilliamNeural-Male` → Szybki i dokładny.
        - FACEBOOK MMS → format `en-facebook-mms VITS` → Głos jest bardziej naturalny; obecnie wykorzystuje tylko CPU.
        - PIPER TTS → format `en_US-lessac-high VITS-onnx` → To samo co poprzednie, ale zoptymalizowane zarówno pod CPU, jak i GPU.
        - BARK → format `en_speaker_0-Male BARK` → Dobra jakość, ale wolne działanie, podatne na halucynacje.
        - OpenAI TTS → format `>alloy OpenAI-TTS` → Wielojęzyczne, ale wymaga klucza OpenAI API
        - Coqui XTTS → format `_XTTS_/AUTOMATIC.wav` → Dostępne tylko dla języka chińskiego (uproszczonego), angielskiego, francuskiego, niemieckiego, włoskiego, portugalskiego, polskiego, tureckiego, rosyjskiego, niderlandzkiego, czeskiego, arabskiego, hiszpańskiego, węgierskiego, koreańskiego i japońskiego.

        ---

        # 🎤 Jak używać głosów R.V.C. i R.V.C.2 (opcjonalnie) 🎶

        Celem jest zastosowanie R.V.C. do wygenerowanego TTS (tekst do mowy) 🎙️

        1. W zakładce `Custom Voice R.V.C.` pobierz potrzebne modele 📥 Możesz użyć linków z Hugging Face i Google Drive w formatach takich jak zip, pth lub index. Możesz również pobrać pełne repozytoria HF Space, ale ta opcja nie jest bardzo stabilna 😕

        2. Teraz przejdź do `Zamień głos: TTS na R.V.C.` i zaznacz pole `włącz` ✅ Następnie możesz wybrać modele, które chcesz zastosować do każdego mówcy TTS 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Dostosuj metodę F0, która zostanie zastosowana do wszystkich R.V.C. 🎛️

        4. Naciśnij przycisk `ZASTOSUJ KONFIGURACJĘ`, aby zastosować wprowadzone zmiany 🔄

        5. Wróć do zakładki tłumaczenia filmu i kliknij 'Tłumacz' ▶️ Teraz tłumaczenie zostanie wykonane, zastosowując R.V.C. 🗣️

        Wskazówka: Możesz użyć `Test R.V.C.` do eksperymentowania i znalezienia najlepszego TTS lub konfiguracji do zastosowania w R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Tłumaczenie filmu",
        "video_source": "Wybierz Źródło Wideo",
        "link_label": "Link do multimediów.",
        "link_info": "Przykład: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "Wklej tutaj URL...",
        "dir_label": "Ścieżka do Wideo.",
        "dir_info": "Przykład: /usr/home/my_video.mp4",
        "dir_ph": "Wklej tutaj ścieżkę...",
        "sl_label": "Język źródłowy",
        "sl_info": "To jest oryginalny język filmu",
        "tat_label": "Przetłumacz audio na",
        "tat_info": "Wybierz język docelowy i upewnij się, że wybierzesz odpowiednią syntezę mowy tekstowej (TTS) dla tego języka.",
        "num_speakers": "Wybierz, ile osób mówi w filmie.",
        "min_sk": "Min. mówców",
        "max_sk": "Maks. mówców",
        "tts_select": "Wybierz głos dla każdego mówcy.",
        "sk1": "Głos TTS Mówca 1",
        "sk2": "Głos TTS Mówca 2",
        "sk3": "Głos TTS Mówca 3",
        "sk4": "Głos TTS Mówca 4",
        "sk5": "Głos TTS Mówca 5",
        "sk6": "Głos TTS Mówca 6",
        "sk7": "Głos TTS Mówca 7",
        "sk8": "Głos TTS Mówca 8",
        "sk9": "Głos TTS Mówca 9",
        "sk10": "Głos TTS Mówca 10",
        "sk11": "Głos TTS Mówca 11",
        "sk12": "Głos TTS Mówca 12",
        "vc_title": "Imitacja głosu w różnych językach",
        "vc_subtitle": """
        ### Odtwórz głos osoby w różnych językach.
        Mimo że jest skuteczny w większości przypadków, nie zawsze osiąga doskonałość.
        Imitacja głosu odtwarza tylko ton osoby referencyjnej, wykluczając akcent i emocje, które są kontrolowane przez model TTS podstawowego mówcy i nie są replikowane przez konwerter.
        Będzie pobierać próbki dźwiękowe z głównego dźwięku dla każdego mówcy i je przetwarzać.
        """,
        "vc_active_label": "Aktywna Imitacja Głosu",
        "vc_active_info": "Aktywna Imitacja Głosu: Odtwarza ton oryginalnego mówcy",
        "vc_method_label": "Metoda",
        "vc_method_info": "Wybierz metodę procesu imitacji głosu",
        "vc_segments_label": "Maks. liczba próbek",
        "vc_segments_info": "Maks. liczba próbek: To jest liczba próbek dźwiękowych, które zostaną wygenerowane w procesie, więcej to lepiej, ale może to wprowadzić hałas",
        "vc_dereverb_label": "Usuń pogłos",
        "vc_dereverb_info": "Usuń pogłos: Zastosuj usuwanie pogłosu do próbek dźwiękowych.",
        "vc_remove_label": "Usuń poprzednie próbki",
        "vc_remove_info": "Usuń poprzednie próbki: Usuń wcześniej wygenerowane próbki, więc trzeba będzie wygenerować nowe.",
        "xtts_title": "Utwórz TTS na podstawie dźwięku",
        "xtts_subtitle": "Prześlij krótki plik dźwiękowy o maksymalnej długości 10 sekund z głosem. Korzystając z XTTS, zostanie utworzony nowy TTS z głosem podobnym do dostarczonego pliku dźwiękowego.",
        "xtts_file_label": "Prześlij krótki dźwięk z głosem",
        "xtts_name_label": "Nazwa dla TTS",
        "xtts_name_info": "Użyj prostej nazwy",
        "xtts_dereverb_label": "Usuń pogłos dźwięku",
        "xtts_dereverb_info": "Usuń pogłos dźwięku: Zastosuj usuwanie pogłosu do dźwięku",
        "xtts_button": "Przetwórz dźwięk i dodaj go do selektora TTS",
        "xtts_footer": "Automatycznie generuj głos XTTS: Możesz użyć `_XTTS_/AUTOMATIC.wav` w selektorze TTS, aby automatycznie generować segmenty dla każdego mówcy podczas generowania tłumaczenia.",
        "extra_setting": "Ustawienia Zaawansowane",
        "acc_max_label": "Maks. przyspieszenie dźwięku",
        "acc_max_info": "Maksymalne przyspieszenie dla przetłumaczonych segmentów dźwiękowych, aby uniknąć nakładania się. Wartość 1.0 oznacza brak przyspieszenia",
        "acc_rate_label": "Regulacja prędkości przyśpieszania",
        "acc_rate_info": "Regulacja prędkości przyśpieszania: Dostosowuje przyśpieszenie, aby dostosować się do segmentów wymagających mniejszej prędkości, zachowując ciągłość i uwzględniając czas następnego startu.",
        "or_label": "Redukcja Nakładania",
        "or_info": "Redukcja Nakładania: Zapewnia, że segmenty się nie nakładają, poprzez dostosowanie czasów rozpoczęcia na podstawie wcześniejszych czasów zakończenia; może zakłócić synchronizację.",
        "aud_mix_label": "Metoda Mieszania Audio",
        "aud_mix_info": "Mieszaj pliki audio oryginalne i przetłumaczone, aby utworzyć spersonalizowane, zrównoważone wyjście z dwoma dostępnymi trybami mieszania.",
        "vol_ori": "Głośność oryginalnego dźwięku",
        "vol_tra": "Głośność przetłumaczonego dźwięku",
        "voiceless_tk_label": "Ścieżka bezgłosowa",
        "voiceless_tk_info": "Ścieżka bezgłosowa: Usuń głosy oryginalne przed połączeniem ich z przetłumaczonym dźwiękiem.",
        "sub_type": "Typ Napisów",
        "soft_subs_label": "Miękkie napisy",
        "soft_subs_info": "Miękkie napisy: Opcjonalne napisy, które widzowie mogą włączać lub wyłączać podczas oglądania wideo.",
        "burn_subs_label": "Wypal napisy",
        "burn_subs_info": "Wypal napisy: Osadź napisy w wideo, stając się trwałą częścią treści wizualnej.",
        "whisper_title": "Konfiguracja transkrypcji.",
        "lnum_label": "Zliteralizuj Liczby",
        "lnum_info": "Zliteralizuj Liczby: Zastąp numeryczne reprezentacje ich pisemnymi odpowiednikami w transkrypcji.",
        "scle_label": "Oczyszczanie Dźwięku",
        "scle_info": "Oczyszczanie Dźwięku: Poprawa głosu, usuwanie szumów tła przed transkrypcją dla najwyższej precyzji znaczników czasowych. Ta operacja może zająć trochę czasu, szczególnie przy długich plikach dźwiękowych.",
        "sd_limit_label": "Ograniczenie Czasu Trwania Segmentu",
        "sd_limit_info": "Określ maksymalny czas trwania (w sekundach) dla każdego segmentu. Dźwięk będzie przetwarzany za pomocą VAD, ograniczając czas trwania dla każdego fragmentu segmentu.",
        "asr_model_info": "Konwertuje mowę na tekst za pomocą modelu „Szept” domyślnie. Użyj niestandardowego modelu, na przykład, wpisując nazwę repozytorium „BELLE-2/Belle-whisper-large-v3-zh” w rozwijanej liście, aby użyć dostosowanego modelu w języku chińskim. Znajdź dostosowane modele na Hugging Face.",
        "ctype_label": "Typ Obliczeń",
        "ctype_info": "Wybór mniejszych typów, takich jak int8 lub float16, może poprawić wydajność poprzez zmniejszenie użycia pamięci i zwiększenie przepustowości obliczeniowej, ale może poświęcić precyzję w porównaniu do większych typów danych, takich jak float32.",
        "batchz_label": "Rozmiar Partii",
        "batchz_info": "Zmniejszenie rozmiaru partii oszczędza pamięć, jeśli Twój GPU ma mniej VRAM, i pomaga zarządzać problemami z brakiem pamięci.",
        "tsscale_label": "Skala Segmentacji Tekstu",
        "tsscale_info": "Podziel tekst na segmenty według zdań, słów lub znaków. Segmentacja według słów i znaków zapewnia drobniejszą granulację, przydatną dla napisów; wyłączenie tłumaczenia zachowuje pierwotną strukturę.",
        "srt_file_label": "Prześlij plik napisów SRT (będzie używany zamiast transkrypcji Whisper)",
        "divide_text_label": "Podziel segmenty tekstu przez:",
        "divide_text_info": "(Eksperymentalne) Wprowadź separator do podziału istniejących segmentów tekstu w języku źródłowym. Narzędzie zidentyfikuje wystąpienia i utworzy nowe segmenty zgodnie z nimi. Wprowadź kilka separatorów, używając |, np.: !|?|...|。",
        "diarization_label": "Model diarization",
        "tr_process_label": "Proces tłumaczenia",
        "out_type_label": "Typ wyjścia",
        "out_name_label": "Nazwa pliku",
        "out_name_info": "Nazwa pliku wyjściowego",
        "task_sound_label": "Dźwięk statusu zadania",
        "task_sound_info": "Dźwięk statusu zadania: Odtwarza alert dźwiękowy informujący o zakończeniu zadania lub błędach w trakcie wykonywania.",
        "cache_label": "Pobierz postęp",
        "cache_info": "Pobierz postęp: Kontynuuj proces od ostatniego punktu kontrolnego.",
        "preview_info": "Podgląd przycina wideo do 10 sekund tylko do celów testowych. Proszę wyłączyć go, aby pobrać pełną długość wideo.",
        "edit_sub_label": "Edytuj wygenerowane napisy",
        "edit_sub_info": "Edytuj wygenerowane napisy: Pozwala uruchomić tłumaczenie w 2 krokach. Najpierw za pomocą przycisku 'POBIERZ NAPISY I EDYTUJ' pobierz napisy, aby je edytować, a następnie za pomocą przycisku 'TRANSLATE' możesz wygenerować wideo",
        "button_subs": "POBIERZ NAPISY I EDYTUJ",
        "editor_sub_label": "Wygenerowane napisy",
        "editor_sub_info": "Zapraszamy do edycji tekstu w wygenerowanych napisach tutaj. Możesz wprowadzić zmiany w opcjach interfejsu przed kliknięciem przycisku 'TRANSLATE', oprócz 'Języka źródłowego', 'Przetłumacz audio na' i 'Maks. mówców', aby uniknąć błędów. Po zakończeniu kliknij przycisk 'TRANSLATE'.",
        "editor_sub_ph": "Najpierw naciśnij 'POBIERZ NAPISY I EDYTUJ', aby pobrać napisy",
        "button_translate": "TRANSLATE",
        "output_result_label": "POBIERZ PRZETŁUMACZONE WIDEO",
        "sub_ori": "Napisy oryginalne",
        "sub_tra": "Przetłumaczone napisy",
        "ht_token_info": "Jednym ważnym krokiem jest zaakceptowanie umowy licencyjnej dotyczącej korzystania z Pyannote. Musisz mieć konto na Hugging Face i zaakceptować licencję do użytkowania modeli: https://huggingface.co/pyannote/speaker-diarization oraz https://huggingface.co/pyannote/segmentation. Pobierz swój KLUCZ TOKEN tutaj: https://hf.co/settings/tokens",
        "ht_token_ph": "Wklej tutaj Token...",
        "tab_docs": "Tłumaczenie dokumentu",
        "docs_input_label": "Wybierz Źródło Dokumentu",
        "docs_input_info": "To może być plik PDF, DOCX, TXT lub tekst",
        "docs_source_info": "To jest oryginalny język tekstu",
        "chunk_size_label": "Maks. liczba znaków, które TTS będzie przetwarzał na segment",
        "chunk_size_info": "Wartość 0 przypisuje dynamiczną i bardziej kompatybilną wartość dla TTS.",
        "docs_button": "Rozpocznij most konwersji językowej",
        "cv_url_info": "Automatycznie pobierz modele R.V.C. z adresu URL. Możesz użyć linków z HuggingFace lub Drive, i możesz dołączyć kilka linków, każdy oddzielony przecinkiem. Przykład: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Zamień głos: TTS na R.V.C.",
        "sec1_title": "### 1. Aby włączyć jego użycie, zaznacz go jako aktywny.",
        "enable_replace": "Zaznacz to, aby włączyć używanie modeli.",
        "sec2_title": "### 2. Wybierz głos, który zostanie zastosowany do każdego TTS każdego odpowiedniego mówcy i zastosuj konfiguracje.",
        "sec2_subtitle": "W zależności od liczby <TTS Speaker>, którą będziesz używać, każdy potrzebuje odpowiedniego modelu. Dodatkowo, jest jeden pomocniczy, jeśli z jakiegoś powodu mówca nie zostanie poprawnie wykryty.",
        "cv_tts1": "Wybierz głos, który ma być stosowany dla Mówcy 1.",
        "cv_tts2": "Wybierz głos, który ma być stosowany dla Mówcy 2.",
        "cv_tts3": "Wybierz głos, który ma być stosowany dla Mówcy 3.",
        "cv_tts4": "Wybierz głos, który ma być stosowany dla Mówcy 4.",
        "cv_tts5": "Wybierz głos, który ma być stosowany dla Mówcy 5.",
        "cv_tts6": "Wybierz głos, który ma być stosowany dla Mówcy 6.",
        "cv_tts7": "Wybierz głos, który ma być stosowany dla Mówcy 7.",
        "cv_tts8": "Wybierz głos, który ma być stosowany dla Mówcy 8.",
        "cv_tts9": "Wybierz głos, który ma być stosowany dla Mówcy 9.",
        "cv_tts10": "Wybierz głos, który ma być stosowany dla Mówcy 10.",
        "cv_tts11": "Wybierz głos, który ma być stosowany dla Mówcy 11.",
        "cv_tts12": "Wybierz głos, który ma być stosowany dla Mówcy 12.",
        "cv_aux": "- Głos do zastosowania w przypadku niepowodzenia wykrycia Mówcy.",
        "cv_button_apply": "ZASTOSUJ KONFIGURACJĘ",
        "tab_help": "Pomoc",
    },
    "swedish": {
        "description": """
        ### 🎥 **Översätt videor enkelt med SoniTranslate!** 📽️

        Ladda upp en video, ljudfil eller ange en YouTube-länk. 📽️ **Få den uppdaterade anteckningsboken från det officiella arkivet: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Se fliken `Hjälp` för instruktioner om hur du använder det. Nu ska vi ha roligt med videöversättning! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Instruktioner för användning:**

        1. 📤 Ladda upp en **video**, **ljudfil** eller ange en 🌐 **YouTube-länk.**

        2. 🌍 Välj det språk du vill **översätta videon till**.

        3. 🗣️ Ange **antalet personer som talar** i videon och **tilldela var och en en text-till-tal-röst** lämplig för översättningsspråket.

        4. 🚀 Tryck på knappen '**Översätt**' för att få resultatet.

        ---

        # 🧩 **SoniTranslate stöder olika TTS (Text-to-Speech) motorer, vilka är:**
        - EDGE-TTS → format `en-AU-WilliamNeural-Male` → Snabbt och noggrant.
        - FACEBOOK MMS → format `en-facebook-mms VITS` → Rösten är mer naturlig; för tillfället använder den endast CPU.
        - PIPER TTS → format `en_US-lessac-high VITS-onnx` → Samma som den föregående, men den är optimerad för både CPU och GPU.
        - BARK → format `en_speaker_0-Male BARK` → Bra kvalitet men långsam och benägen för hallucinationer.
        - OpenAI TTS → format `>alloy OpenAI-TTS` → Multispråkigt men kräver en OpenAI API-nyckel
        - Coqui XTTS → format `_XTTS_/AUTOMATIC.wav` → Endast tillgängligt för kinesiska (förenklad), engelska, franska, tyska, italienska, portugisiska, polska, turkiska, ryska, nederländska, tjeckiska, arabiska, spanska, ungerska, koreanska och japanska.

        ---

        # 🎤 Hur man använder R.V.C. och R.V.C.2-röster (Valfritt) 🎶

        Målet är att tillämpa en R.V.C. på den genererade TTS (Text-to-Speech) 🎙️

        1. I fliken `Anpassad röst R.V.C.`, ladda ner de modeller du behöver 📥 Du kan använda länkar från Hugging Face och Google Drive i format som zip, pth eller index. Du kan också ladda ner kompletta HF-utrymmen, men den här alternativet är inte särskilt stabilt 😕

        2. Gå nu till `Ersätt röst: TTS till R.V.C.` och markera rutan `aktivera` ✅ Efter det kan du välja de modeller du vill tillämpa på varje TTS-högtalare 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Justera F0-metoden som kommer att tillämpas på alla R.V.C. 🎛️

        4. Tryck på `TILLÄMPA KONFIGURATION` för att tillämpa de ändringar du gjorde 🔄

        5. Gå tillbaka till fliken för videöversättning och klicka på 'Översätt' ▶️ Nu kommer översättningen att göras med tillämpning av R.V.C. 🗣️

        Tips: Du kan använda `Test R.V.C.` för att experimentera och hitta de bästa TTS eller konfigurationer att tillämpa på R.V.C. 🧪🔍

        ---

        """,
        "tab_translate": "Videöversättning",
        "video_source": "Välj Videokälla",
        "link_label": "Medialänk.",
        "link_info": "Exempel: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL går här...",
        "dir_label": "Videostig.",
        "dir_info": "Exempel: /usr/home/min_video.mp4",
        "dir_ph": "Sökväg går här...",
        "sl_label": "Källspråk",
        "sl_info": "Detta är det ursprungliga språket för videon",
        "tat_label": "Översätt ljud till",
        "tat_info": "Välj målspråket och se också till att välja den motsvarande TTS för det språket.",
        "num_speakers": "Välj hur många personer som talar i videon.",
        "min_sk": "Min högtalare",
        "max_sk": "Max högtalare",
        "tts_select": "Välj röst för varje högtalare.",
        "sk1": "TTS Högtalare 1",
        "sk2": "TTS Högtalare 2",
        "sk3": "TTS Högtalare 3",
        "sk4": "TTS Högtalare 4",
        "sk5": "TTS Högtalare 5",
        "sk6": "TTS Högtalare 6",
        "sk7": "TTS Högtalare 7",
        "sk8": "TTS Högtalare 8",
        "sk9": "TTS Högtalare 9",
        "sk10": "TTS Högtalare 10",
        "sk11": "TTS Högtalare 11",
        "sk12": "TTS Högtalare 12",
        "vc_title": "Röstimitation på olika språk",
        "vc_subtitle": """
        ### Replicera en persons röst över olika språk.
        Effektiv med de flesta röster när den används på rätt sätt, men den kan inte uppnå perfektion i varje fall.
        Röstimitation reproducerar endast referenshögtalarens ton, exklusive accent och känslor, som styrs av basens högtalar-TTS-modell och inte reproduceras av omvandlaren.
        Detta kommer att ta ljudprover från huvudljudet för varje högtalare och bearbeta dem.
        """,
        "vc_active_label": "Aktiv Röstimitation",
        "vc_active_info": "Aktiv Röstimitation: Reproducerar den ursprungliga högtalarens ton",
        "vc_method_label": "Metod",
        "vc_method_info": "Välj en metod för Röstimitationsprocessen",
        "vc_segments_label": "Maxprover",
        "vc_segments_info": "Maxprover: Är antalet ljudprover som kommer att genereras för processen, fler är bättre men det kan lägga till brus",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Tillämpar vokal dereverb på ljudproverna.",
        "vc_remove_label": "Ta bort tidigare prover",
        "vc_remove_info": "Ta bort tidigare prover: Ta bort de tidigare genererade proven, så nya måste skapas.",
        "xtts_title": "Skapa en TTS baserad på ett ljud",
        "xtts_subtitle": "Ladda upp en ljudfil på maximalt 10 sekunder med en röst. Genom att använda XTTS kommer en ny TTS att skapas med en röst liknande den tillhandahållna ljudfilen.",
        "xtts_file_label": "Ladda upp ett kort ljud med rösten",
        "xtts_name_label": "Namn för TTS",
        "xtts_name_info": "Använd ett enkelt namn",
        "xtts_dereverb_label": "Dereverb ljud",
        "xtts_dereverb_info": "Dereverb ljud: Tillämpar vokal dereverb på ljudet",
        "xtts_button": "Bearbeta ljudet och inkludera det i TTS-väljaren",
        "xtts_footer": "Generera röst xtts automatiskt: Du kan använda `_XTTS_/AUTOMATIC.wav` i TTS-väljaren för att automatiskt generera segment för varje högtalare vid generering av översättningen.",
        "extra_setting": "Avancerade Inställningar",
        "acc_max_label": "Max Ljudacceleration",
        "acc_max_info": "Maximal acceleration för översatta ljudsegment för att undvika överlappning. En värde på 1,0 representerar ingen acceleration",
        "acc_rate_label": "Accelerationshastighetsreglering",
        "acc_rate_info": "Accelerationshastighetsreglering: Justerar accelerationen för att passa segment som kräver lägre hastighet, vilket bibehåller kontinuitet och överväger nästa starttid.",
        "or_label": "Överlappningsreducering",
        "or_info": "Överlappningsreducering: Säkerställer att segment inte överlappar genom att justera starttider baserat på tidigare sluttider; kan störa synkroniseringen.",
        "aud_mix_label": "Ljudmixningsmetod",
        "aud_mix_info": "Blanda original- och översatta ljudfiler för att skapa en anpassad, balanserad utdata med två tillgängliga blandningslägen.",
        "vol_ori": "Volym ursprungligt ljud",
        "vol_tra": "Volym översatt ljud",
        "voiceless_tk_label": "Röstlös spår",
        "voiceless_tk_info": "Röstlös spår: Ta bort de ursprungliga ljudrösterna innan de kombineras med det översatta ljudet.",
        "sub_type": "Undertexttyp",
        "soft_subs_label": "Mjuka undertexter",
        "soft_subs_info": "Mjuka undertexter: Valfria undertexter som tittare kan slå på eller av medan de tittar på videon.",
        "burn_subs_label": "Bränn undertexter",
        "burn_subs_info": "Bränn undertexter: Bädda in undertexter i videon, vilket gör dem till en permanent del av det visuella innehållet.",
        "whisper_title": "Konfigurera transkription.",
        "lnum_label": "Literalisera Siffror",
        "lnum_info": "Literalisera Siffror: Ersätt numeriska representationer med deras skrivna motsvarigheter i transkriptet.",
        "scle_label": "Ljudstädning",
        "scle_info": "Ljudstädning: Förbättra röster, ta bort bakgrundsljud innan transkribering för högsta tidsstämpelprecision. Denna operation kan ta tid, särskilt med långa ljudfiler.",
        "sd_limit_label": "Segmentvaraktighetsbegränsning",
        "sd_limit_info": "Ange den maximala varaktigheten (i sekunder) för varje segment. Ljudet kommer att bearbetas med VAD och begränsa varaktigheten för varje segmentbit.",
        "asr_model_info": "Det konverterar talat språk till text med hjälp av standardmodellen 'Whisper'. Använd en anpassad modell, till exempel genom att ange lagringsnamnet 'BELLE-2/Belle-whisper-large-v3-zh' i rullgardinsmenyn för att använda en anpassad modell för kinesiska. Hitta finjusterade modeller på Hugging Face.",
        "ctype_label": "Beräkningstyp",
        "ctype_info": "Att välja mindre typer som int8 eller float16 kan förbättra prestanda genom att minska minnesanvändningen och öka den beräkningsmässiga genomströmningen, men kan offra precisionen jämfört med större datatyper som float32.",
        "batchz_label": "Batchstorlek",
        "batchz_info": "Att minska batchstorleken sparar minne om din GPU har mindre VRAM och hjälper till att hantera minnesproblem.",
        "tsscale_label": "Text segmenteringsskala",
        "tsscale_info": "Dela upp texten i segment efter meningar, ord eller tecken. Ordet och teckensegmentering ger finare granularitet, användbart för undertexter; inaktivering av översättning bevarar den ursprungliga strukturen.",
        "srt_file_label": "Ladda upp en SRT-undertextsfil (kommer att användas istället för Whisper-transkriptionen)",
        "divide_text_label": "Dela upp textsegment med:",
        "divide_text_info": "(Experimentell) Ange en avgränsare för att dela upp befintliga textsegment på källspråket. Verktyget kommer att identifiera förekomster och skapa nya segment därefter. Ange flera avgränsare med |, t.ex.: !|?|...|。",
        "diarization_label": "Diariseringsmodell",
        "tr_process_label": "Översättningsprocess",
        "out_type_label": "Utgångstyp",
        "out_name_label": "Filnamn",
        "out_name_info": "Namnet på utdatafilen",
        "task_sound_label": "Uppgiftsstatusljud",
        "task_sound_info": "Uppgiftsstatusljud: Spelar upp ett ljudlarm som indikerar uppgiftsslutförande eller fel under utförandet.",
        "cache_label": "Återställ Framsteg",
        "cache_info": "Återställ Framsteg: Fortsätt processen från senaste kontrollpunkt.",
        "preview_info": "Förhandsgranskning klipper videon till endast 10 sekunder för teständamål. Avaktivera det för att hämta full videolängd.",
        "edit_sub_label": "Redigera genererade undertexter",
        "edit_sub_info": "Redigera genererade undertexter: Tillåter dig att köra översättningen i 2 steg. Först med knappen 'FÅ UNDERSKRIFTER OCH REDIGERA', får du undertexterna för att redigera dem, och sedan med knappen 'ÖVERFÖRA', kan du generera videon",
        "button_subs": "FÅ UNDERSKRIFTER OCH REDIGERA",
        "editor_sub_label": "Genererade undertexter",
        "editor_sub_info": "Du kan redigera texten i de genererade undertexterna här. Du kan göra ändringar i gränssnittsalternativen innan du klickar på knappen 'ÖVERFÖRA', förutom 'Källspråk', 'Översätt ljud till' och 'Max högtalare', för att undvika fel. När du är klar, klicka på knappen 'ÖVERFÖRA'.",
        "editor_sub_ph": "Tryck först på 'FÅ UNDERSKRIFTER OCH REDIGERA' för att hämta undertexterna",
        "button_translate": "ÖVERFÖRA",
        "output_result_label": "LADDA NER ÖVERSATT VIDEO",
        "sub_ori": "Undertexter",
        "sub_tra": "Översatta undertexter",
        "ht_token_info": "Ett viktigt steg är att godkänna licensavtalet för att använda Pyannote. Du behöver ha ett konto på Hugging Face och acceptera licensen för att använda modellerna: https://huggingface.co/pyannote/speaker-diarization och https://huggingface.co/pyannote/segmentation. Hämta din NYCKELTOKEN här: https://hf.co/settings/tokens",
        "ht_token_ph": "Token går här...",
        "tab_docs": "Dokumentöversättning",
        "docs_input_label": "Välj Dokumentkälla",
        "docs_input_info": "Det kan vara PDF, DOCX, TXT eller text",
        "docs_source_info": "Detta är det ursprungliga språket för texten",
        "chunk_size_label": "Max antal tecken som TTS kommer att behandla per segment",
        "chunk_size_info": "Ett värde på 0 tilldelar ett dynamiskt och mer kompatibelt värde för TTS.",
        "docs_button": "Starta Språkomvandlingsbryggan",
        "cv_url_info": "Ladda automatiskt ner R.V.C.-modellerna från URL:en. Du kan använda länkar från HuggingFace eller Drive, och du kan inkludera flera länkar, var och en separerad med ett komma. Exempel: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Ersätt röst: TTS till R.V.C.",
        "sec1_title": "### 1. För att aktivera dess användning, markera den som aktiverad.",
        "enable_replace": "Markera detta för att aktivera användningen av modellerna.",
        "sec2_title": "### 2. Välj en röst som ska tillämpas på varje TTS för varje motsvarande högtalare och tillämpa konfigurationerna.",
        "sec2_subtitle": "Beroende på hur många <TTS Speaker> du kommer att använda, behöver var och en sin respektive modell. Dessutom finns det en hjälpmodell om högtalaren av någon anledning inte upptäcks korrekt.",
        "cv_tts1": "Välj röst att tillämpa för Högtalare 1.",
        "cv_tts2": "Välj röst att tillämpa för Högtalare 2.",
        "cv_tts3": "Välj röst att tillämpa för Högtalare 3.",
        "cv_tts4": "Välj röst att tillämpa för Högtalare 4.",
        "cv_tts5": "Välj röst att tillämpa för Högtalare 5.",
        "cv_tts6": "Välj röst att tillämpa för Högtalare 6.",
        "cv_tts7": "Välj röst att tillämpa för Högtalare 7.",
        "cv_tts8": "Välj röst att tillämpa för Högtalare 8.",
        "cv_tts9": "Välj röst att tillämpa för Högtalare 9.",
        "cv_tts10": "Välj röst att tillämpa för Högtalare 10.",
        "cv_tts11": "Välj röst att tillämpa för Högtalare 11.",
        "cv_tts12": "Välj röst att tillämpa för Högtalare 12.",
        "cv_aux": "- Röst att tillämpa om en högtalare inte upptäcks framgångsrikt.",
        "cv_button_apply": "TILLÄMPA KONFIGURATION",
        "tab_help": "Hjälp",
    },
    "korean": {
        "description": """
        ### 🎥 **SoniTranslate를 사용하여 비디오를 쉽게 번역하세요!** 📽️

        비디오, 오디오 파일을 업로드하거나 YouTube 링크를 제공하세요. 📽️ **공식 저장소에서 최신 노트북을 받으세요.: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        사용 방법에 대한 지침은 `도움말` 탭을 참조하세요. 비디오 번역으로 즐거운 시간을 보내세요! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **사용 방법:**

        1. 📤 **비디오**, **오디오 파일**을 업로드하거나 🌐 **YouTube 링크**를 제공하세요.

        2. 🌍 **비디오를 번역할 언어**를 선택하세요.

        3. 🗣️ 비디오에서 **말하는 사람 수**를 지정하고 각각을 번역 언어에 적합한 텍스트 음성으로 할당하세요.

        4. 🚀 '**번역**' 버튼을 눌러 결과를 얻으세요.

        ---

        # 🧩 **SoniTranslate는 다양한 TTS (텍스트 음성 변환) 엔진을 지원합니다. 이는 다음과 같습니다:**
        - EDGE-TTS → 형식 `en-AU-WilliamNeural-Male` → 빠르고 정확합니다.
        - FACEBOOK MMS → 형식 `en-facebook-mms VITS` → 음성이 더 자연스럽지만 현재 CPU만 사용됩니다.
        - PIPER TTS → 형식 `en_US-lessac-high VITS-onnx` → 이전 것과 동일하지만 CPU와 GPU 모두 최적화되었습니다.
        - BARK → 형식 `en_speaker_0-Male BARK` → 품질은 좋지만 느리고 환각에 취약합니다.
        - OpenAI TTS → 형식 `>alloy OpenAI-TTS` → 다국어지만 OpenAI API 키가 필요합니다
        - Coqui XTTS → 형식 `_XTTS_/AUTOMATIC.wav` → 중국어 (간체), 영어, 프랑스어, 독일어, 이탈리아어, 포르투갈어, 폴란드어, 터키어, 러시아어, 네덜란드어, 체코어, 아랍어, 스페인어, 헝가리어, 한국어 및 일본어만 사용할 수 있습니다.

        ---

        # 🎤 R.V.C. 및 R.V.C.2 음성 사용 방법 (선택 사항) 🎶

        목표는 생성된 TTS (텍스트 음성 변환)에 R.V.C.를 적용하는 것입니다. 🎙️

        1. `Custom Voice R.V.C.` 탭에서 필요한 모델을 다운로드하세요. 📥 Hugging Face 및 Google Drive에서 zip, pth 또는 index와 같은 형식의 링크를 사용할 수 있습니다. HF 공간 저장소 전체를 다운로드할 수도 있지만 이 옵션은 안정성이 떨어집니다 😕

        2. 이제 `Replace voice: TTS to R.V.C.`로 이동하여 `enable` 상자를 확인하세요 ✅ 이후 각 TTS 스피커에 적용할 모델을 선택할 수 있습니다 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. 모든 R.V.C.에 적용할 F0 방법을 조정하세요. 🎛️

        4. 변경한 사항을 적용하려면 `APPLY CONFIGURATION`을 누르세요. 🔄

        5. 비디오 번역 탭으로 돌아가 'Translate'를 클릭하세요 ▶️ 이제 번역은 R.V.C.를 적용하여 수행됩니다. 🗣️

        팁: `Test R.V.C.`를 사용하여 실험하고 R.V.C.에 적용할 최상의 TTS 또는 구성을 찾을 수 있습니다. 🧪🔍

        ---

        """,
        "tab_translate": "비디오 번역",
        "video_source": "비디오 소스 선택",
        "link_label": "미디어 링크.",
        "link_info": "예시: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL을 입력하세요...",
        "dir_label": "비디오 경로.",
        "dir_info": "예시: /usr/home/my_video.mp4",
        "dir_ph": "경로를 입력하세요...",
        "sl_label": "원본 언어",
        "sl_info": "비디오의 원래 언어입니다",
        "tat_label": "번역할 언어 선택",
        "tat_info": "대상 언어를 선택하고 해당 언어에 대한 TTS도 선택하세요.",
        "num_speakers": "비디오에서 몇 명이 말하고 있는지 선택하세요.",
        "min_sk": "최소 스피커",
        "max_sk": "최대 스피커",
        "tts_select": "각 스피커에 원하는 음성 선택",
        "sk1": "TTS 스피커 1",
        "sk2": "TTS 스피커 2",
        "sk3": "TTS 스피커 3",
        "sk4": "TTS 스피커 4",
        "sk5": "TTS 스피커 5",
        "sk6": "TTS 스피커 6",
        "sk7": "TTS 스피커 7",
        "sk8": "TTS 스피커 8",
        "sk9": "TTS 스피커 9",
        "sk10": "TTS 스피커 10",
        "sk11": "TTS 스피커 11",
        "sk12": "TTS 스피커 12",
        "vc_title": "다른 언어에서 음성 모방",
        "vc_subtitle": """
        ### 여러 언어로 사람의 음성을 복제합니다.
        대부분의 경우 적절하게 사용되면 효과적이지만 모든 경우에 완벽한 결과를 보장하지는 않을 수 있습니다.
        음성 모방은 기본 스피커 TTS 모델에 의해 지배되는 악센트 및 감정을 제외한 참조 스피커의 음조만 복제합니다.
        이는 각 스피커의 주요 오디오에서 오디오 샘플을 가져와 처리합니다.
        """,
        "vc_active_label": "활성화된 음성 모방",
        "vc_active_info": "활성화된 음성 모방: 원래 스피커의 음조를 복제합니다",
        "vc_method_label": "방법",
        "vc_method_info": "음성 모방 프로세스에 사용할 방법 선택",
        "vc_segments_label": "최대 샘플 수",
        "vc_segments_info": "최대 샘플 수: 프로세스에 생성될 오디오 샘플 수입니다. 더 많으면 더 좋지만 노이즈가 추가될 수 있습니다",
        "vc_dereverb_label": "소음 제거",
        "vc_dereverb_info": "소음 제거: 오디오 샘플에 음성 소음 제거를 적용합니다.",
        "vc_remove_label": "이전 샘플 제거",
        "vc_remove_info": "이전 샘플 제거: 생성된 이전 샘플을 제거하므로 새로 생성해야 합니다.",
        "xtts_title": "오디오 기반 TTS 생성",
        "xtts_subtitle": "음성을 포함한 최대 10초의 짧은 오디오 파일을 업로드하세요. XTTS를 사용하여 제공된 오디오 파일과 유사한 음성을 가진 새 TTS가 생성됩니다.",
        "xtts_file_label": "음성을 포함한 짧은 오디오를 업로드하세요",
        "xtts_name_label": "TTS에 대한 이름",
        "xtts_name_info": "간단한 이름을 사용하세요",
        "xtts_dereverb_label": "음성 소음 제거",
        "xtts_dereverb_info": "음성 소음 제거: 오디오에 음성 소음 제거를 적용합니다",
        "xtts_button": "오디오를 처리하고 TTS 선택기에 포함시킵니다",
        "xtts_footer": "음성 xtts 자동 생성: 번역 생성 시 각 스피커에 대해 세그먼트를 자동으로 생성하려면 TTS 선택기에서 `_XTTS_/AUTOMATIC.wav`를 사용할 수 있습니다.",
        "extra_setting": "고급 설정",
        "acc_max_label": "최대 오디오 가속도",
        "acc_max_info": "중첩을 피하기 위해 번역된 오디오 세그먼트에 대한 최대 가속도. 값이 1.0이면 가속도가 없음을 의미합니다",
        "acc_rate_label": "가속도 조절",
        "acc_rate_info": "가속도 조절: 속도가 느린 세그먼트에 대응하기 위해 가속도를 조절하여 연속성을 유지하고 다음 시작 시간을 고려합니다.",
        "or_label": "중첩 감소",
        "or_info": "중첩 감소: 이전 종료 시간을 기반으로 시작 시간을 조정하여 세그먼트가 겹치지 않도록 합니다. 동기화를 방해할 수 있습니다.",
        "aud_mix_label": "오디오 혼합 방법",
        "aud_mix_info": "원본 및 번역된 오디오 파일을 혼합하여 두 가지 사용 가능한 혼합 모드로 사용자 정의된 균형 잡힌 출력을 만듭니다.",
        "vol_ori": "원본 오디오 볼륨",
        "vol_tra": "번역된 오디오 볼륨",
        "voiceless_tk_label": "음성 제거 트랙",
        "voiceless_tk_info": "음성 제거 트랙: 번역된 오디오와 결합하기 전에 원본 오디오 음성을 제거합니다.",
        "sub_type": "자막 유형",
        "soft_subs_label": "부드러운 자막",
        "soft_subs_info": "부드러운 자막: 시청자가 비디오를 시청하는 동안 켜고 끌 수 있는 선택적 자막.",
        "burn_subs_label": "자막 불러오기",
        "burn_subs_info": "자막 불러오기: 자막을 비디오에 임베드하여 시각 콘텐츠의 영구적인 부분으로 만듭니다.",
        "whisper_title": "전사 구성.",
        "lnum_label": "숫자를 문자로 변환",
        "lnum_info": "숫자를 문자로 변환: 텍스트에서 숫자 표현을 해당되는 글자로 대체하십시오.",
        "scle_label": "소리 정리",
        "scle_info": "소리 정리: 음성을 향상시키고 타임 스탬프 정확도를 위해 전사하기 전에 배경 소음을 제거하십시오. 이 작업은 특히 긴 오디오 파일의 경우 시간이 걸릴 수 있습니다.",
        "sd_limit_label": "세그먼트 기간 제한",
        "sd_limit_info": "각 세그먼트의 최대 기간(초)을 지정하십시오. 오디오는 VAD를 사용하여 각 세그먼트 조각의 기간을 제한하여 처리됩니다.",
        "asr_model_info": "기본적으로 '속삭임 모델'을 사용하여 구어를 텍스트로 변환합니다. 예를 들어, 중국어 언어 파인튜닝 모델을 사용하려면 드롭다운에 'BELLE-2/Belle-whisper-large-v3-zh' 저장소 이름을 입력하십시오. Hugging Face에서 파인튜닝된 모델을 찾을 수 있습니다.",
        "ctype_label": "계산 유형",
        "ctype_info": "int8 또는 float16과 같은 더 작은 유형을 선택하면 메모리 사용을 줄이고 계산 처리량을 증가시켜 성능을 향상시킬 수 있지만 float32와 같은 큰 데이터 유형에 비해 정밀성을 희생할 수 있습니다.",
        "batchz_label": "일괄 크기",
        "batchz_info": "일괄 크기를 줄이면 GPU의 VRAM이 적은 경우 메모리를 절약할 수 있으며 메모리 부족 문제를 관리하는 데 도움이됩니다.",
        "tsscale_label": "텍스트 분할 규모",
        "tsscale_info": "문장, 단어 또는 문자별로 텍스트를 세그먼트로 나눕니다. 단어 및 문자 분할은 자막에 유용한 더 세밀한 세분성을 제공합니다. 번역 비활성화는 원래 구조를 보존합니다.",
        "srt_file_label": "SRT 자막 파일 업로드(전사 대신 사용됨)",
        "divide_text_label": "다음에 따라 텍스트 세그먼트를 분할:",
        "divide_text_info": "(실험적) 기존 텍스트 세그먼트를 분할하기 위해 구분 기호를 입력하세요. 도구는 발생한 사례를 식별하고 그에 따라 새 세그먼트를 생성합니다. |를 사용하여 여러 구분 기호를 지정하세요. 예: !|?|...|。",
        "diarization_label": "다이어리제이션 모델",
        "tr_process_label": "번역 프로세스",
        "out_type_label": "출력 유형",
        "out_name_label": "파일 이름",
        "out_name_info": "출력 파일의 이름",
        "task_sound_label": "작업 상태 사운드",
        "task_sound_info": "작업 상태 사운드: 작업 완료 또는 실행 중 오류를 나타내는 사운드 알림을 재생합니다.",
        "cache_label": "진행 상태 검색",
        "cache_info": "진행 상태 검색: 마지막 체크포인트에서 프로세스를 계속합니다.",
        "preview_info": "미리 보기는 테스트 목적으로 비디오를 10초로 자릅니다. 전체 비디오 지속 시간을 검색하려면 비활성화하세요.",
        "edit_sub_label": "생성된 자막 편집",
        "edit_sub_info": "생성된 자막을 편집할 수 있습니다: '자막 가져오기 및 편집' 버튼을 사용하여 먼저 자막을 가져와 편집한 후, '번역' 버튼을 사용하여 비디오를 생성할 수 있습니다",
        "button_subs": "자막 가져오기 및 편집",
        "editor_sub_label": "생성된 자막",
        "editor_sub_info": "여기에서 생성된 자막의 텍스트를 자유롭게 편집할 수 있습니다. '번역할 언어', '번역할 언어' 및 '최대 스피커'를 제외한 인터페이스 옵션을 변경한 후 '번역' 버튼을 클릭하여 오류를 방지하세요. 작업을 마치면 '번역' 버튼을 클릭하세요.",
        "editor_sub_ph": "먼저 '자막 가져오기 및 편집'를 눌러 자막을 가져옵니다",
        "button_translate": "번역",
        "output_result_label": "번역된 비디오 다운로드",
        "sub_ori": "자막",
        "sub_tra": "번역된 자막",
        "ht_token_info": "중요한 단계 중 하나는 Pyannote 사용에 대한 라이선스 동의를 받는 것입니다. Hugging Face에서 계정을 가져야하며 다음 모델을 사용하기 위해 라이선스를 수락해야합니다: https://huggingface.co/pyannote/speaker-diarization 및 https://huggingface.co/pyannote/segmentation. 여기에서 키 토큰을 가져옵니다: https://hf.co/settings/tokens",
        "ht_token_ph": "토큰을 입력하세요...",
        "tab_docs": "문서 번역",
        "docs_input_label": "문서 소스 선택",
        "docs_input_info": "PDF, DOCX, TXT 또는 텍스트가 될 수 있습니다",
        "docs_source_info": "텍스트의 원래 언어입니다",
        "chunk_size_label": "TTS가 세그먼트 당 처리할 최대 문자 수",
        "chunk_size_info": "값이 0이면 TTS에 대해 동적이고 더 호환 가능한 값이 할당됩니다.",
        "docs_button": "언어 변환 브릿지 시작",
        "cv_url_info": "URL에서 R.V.C. 모델을 자동으로 다운로드합니다. HuggingFace 또는 드라이브에서 링크를 사용할 수 있으며 각각을 쉼표로 구분하여 여러 링크를 포함할 수 있습니다. 예: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "음성 교체: TTS에서 R.V.C.로",
        "sec1_title": "### 1. 사용하도록 설정하려면 활성화로 표시합니다.",
        "enable_replace": "모델 사용을 활성화하려면 이를 확인합니다.",
        "sec2_title": "### 2. 각 해당하는 스피커의 TTS에 적용할 음성을 선택하고 구성을 적용합니다.",
        "sec2_subtitle": "사용할 <TTS 스피커> 수에 따라 각각에 해당하는 모델이 필요합니다. 추가적으로 스피커가 올바르게 감지되지 않은 경우 보조 모델이 있습니다.",
        "cv_tts1": "스피커 1에 적용할 음성을 선택하세요.",
        "cv_tts2": "스피커 2에 적용할 음성을 선택하세요.",
        "cv_tts3": "스피커 3에 적용할 음성을 선택하세요.",
        "cv_tts4": "스피커 4에 적용할 음성을 선택하세요.",
        "cv_tts5": "스피커 5에 적용할 음성을 선택하세요.",
        "cv_tts6": "스피커 6에 적용할 음성을 선택하세요.",
        "cv_tts7": "스피커 7에 적용할 음성을 선택하세요.",
        "cv_tts8": "스피커 8에 적용할 음성을 선택하세요.",
        "cv_tts9": "스피커 9에 적용할 음성을 선택하세요.",
        "cv_tts10": "스피커 10에 적용할 음성을 선택하세요.",
        "cv_tts11": "스피커 11에 적용할 음성을 선택하세요.",
        "cv_tts12": "스피커 12에 적용할 음성을 선택하세요.",
        "cv_aux": "- 스피커가 올바르게 감지되지 않은 경우 적용할 음성.",
        "cv_button_apply": "구성 적용",
        "tab_help": "도움말",
    },
    "marathi": {
        "description": """
        ### 🎥 **आसानीसोबत SoniTranslate द्वारे व्हिडिओ अनुवाद करा!** 📽️

        एक व्हिडिओ, ऑडिओ फाईल अपलोड करा किंवा एक YouTube लिंक प्रदान करा. 📽️ **अद्यतनित नोटबुक घ्या आधिकृत भंडारात।: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        तपशील देखण्यासाठी 'मदत' टॅब पहा. व्हिडिओ अनुवादासोबत मजा करण्याची सुरवात करूया! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **वापरायला निर्देशिका:**

        1. 📤 **व्हिडिओ**, **ऑडिओ फाईल** अपलोड करा किंवा 🌐 **YouTube लिंक प्रदान करा.**

        2. 🌍 व्हिडिओ **अनुवाद** करण्यासाठी कोणत्या **भाषेत निवडा.**

        3. 🗣️ व्हिडिओमध्ये **किती लोक बोलत आहेत** ते स्पष्ट करा आणि प्रत्येकाला अनुवाद भाषेसाठी उपयुक्त TTS द्या.

        4. 🚀 '**अनुवाद**' बटण दाबा निकाल मिळवण्यासाठी.

        ---

        # 🧩 **SoniTranslate विविध TTS (पाठ-टू-स्पीच) इंजिनसाठी समर्थन करते, ज्या म्हणजे:**
        - EDGE-TTS → स्वरूप `en-AU-WilliamNeural-Male` → जलद आणि खात्रीशील.
        - FACEBOOK MMS → स्वरूप `en-facebook-mms VITS` → ध्वनी अधिक प्राकृतिक आहे; ह्या क्षणी, हे केवळ CPU वापरते.
        - PIPER TTS → स्वरूप `en_US-lessac-high VITS-onnx` → म्हणजे अखेरचा, परंतु ह्यात CPU आणि GPU दोन्हीत अनुकूलित केले आहे.
        - BARK → स्वरूप `en_speaker_0-Male BARK` → चांगली गुणवत्ता परंतु मंद, आणि हे हल्ल्यांसाठी आदर्श आहे.
        - OpenAI TTS → स्वरूप `>alloy OpenAI-TTS` → बहुभाषिक आहे पण OpenAI API की आवश्यकता आहे
        - Coqui XTTS → स्वरूप `_XTTS_/AUTOMATIC.wav` → केवळ उपलब्ध आहे: चिनी (सरलीकृत), इंग्रजी, फ्रेंच, जर्मन, इटालियन, पोर्तुगीज, पोलिश, तुर्की, रशियन, डच, चेक, अरबी, स्पॅनिश, हंगेरियन, कोरियन आणि जपानी.

        ---

        # 🎤 कसे वापरावे आर.व्ही.सी. आणि आर.व्ही.सी.2 आवाज (पर्वतीय) 🎶

        उद्दिष्ट म्हणजे उत्पन्न केलेल्या TTS (पाठ-टू-स्पीच) वर एक आर.व्ही.सी. लागू करा 🎙️

        1. `कस्टम व्हॉईस आर.व्ही.सी.` टॅबमध्ये, आपल्याला आवश्यक असलेल्या मॉडेल्स डाउनलोड करा 📥 आपण Hugging Face आणि Google Drive यांच्या लिंक्सचा वापर करू शकता, जसे की zip, pth किंवा इंडेक्स. आपण पूर्ण HF स्पेस भंडारांचा डाउनलोड करू शकता, परंतु ह्या पर्यायाचा स्थिरपणा काही कमी आहे 😕

        2. आता, `आर.व्ही.सी. च्या आवाजाच्या TTS ला बदला: टीटीएस ते आर.व्ही.सी.` आणि `सक्षम` बॉक्स तपासा ✅ यानंतर, आपण प्रत्येक TTS वक्त्याला लागणारा मॉडेल निवडू शकता 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. सर्व आर.व्ही.सी. ला लागू केलेला F0 विधान अनुकूलीत करा 🎛️

        4. आपल्याने केलेल्या बदल लागू करण्यासाठी `अनुप्रयोग बदल` दाबा 🔄

        5. व्हिडिओ अनुवाद टॅबमध्ये परत जा आणि 'अनुवाद' वर क्लिक करा ▶️ आता, अनुवाद R.V.C. लागू करत आहे 🗣️

        सूचना: आपण `टेस्ट आर.व्ही.सी.` वापरू शकता व सर्वोत्तम TTS किंवा आर.व्ही.सी. लागू करण्यासाठी गुणवत्ता शोधण्यासाठी वापरू शकता 🧪🔍

        ---

        """,
        "tab_translate": "व्हिडिओ अनुवाद",
        "video_source": "व्हिडिओ स्रोत निवडा",
        "link_label": "मीडिया लिंक.",
        "link_info": "उदाहरण: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL येथे जातो...",
        "dir_label": "व्हिडिओ मार्ग.",
        "dir_info": "उदाहरण: /usr/home/my_video.mp4",
        "dir_ph": "मार्ग येथे जातो...",
        "sl_label": "मूळ भाषा",
        "sl_info": "हे व्हिडिओची मूळ भाषा आहे",
        "tat_label": "ऑडिओ अनुवाद करा",
        "tat_info": "लक्ष्य भाषा निवडा आणि त्या भाषेसाठी संबद्ध TTS निवडण्यास सुनिश्चित करा.",
        "num_speakers": "व्हिडिओमध्ये किती लोक बोलत आहेत हे निवडा.",
        "min_sk": "किमान बोलताही",
        "max_sk": "किमान बोलताही",
        "tts_select": "प्रत्येक वक्त्यासाठी आपल्याला कसा आवाज आवडतो ते निवडा.",
        "sk1": "TTS वक्त्य 1",
        "sk2": "TTS वक्त्य 2",
        "sk3": "TTS वक्त्य 3",
        "sk4": "TTS वक्त्य 4",
        "sk5": "TTS वक्त्य 5",
        "sk6": "TTS वक्त्य 6",
        "sk7": "TTS वक्त्य 7",
        "sk8": "TTS वक्त्य 8",
        "sk9": "TTS वक्त्य 9",
        "sk10": "TTS वक्त्य 10",
        "sk11": "TTS वक्त्य 11",
        "sk12": "TTS वक्त्य 12",
        "vc_title": "विविध भाषांमध्ये आवाज नक्कल",
        "vc_subtitle": """
        ### विविध भाषांमध्ये व्यक्तीचा आवाज पुनर्निर्मित करा.
        अनुकूलप्रद केल्यास अधिकांश आवाजांसह अद्याप अव्याप्ती न मिळताना, प्रत्येक गोष्टीत उपयोगी आहे. आवाज पुनर्निर्मित केवळ संदर्भ वक्त्याच्या टोन अधिल्यास आहे, ज्याची मूळ वक्त्य TTS मॉडेल द्वारे नियंत्रित केली जाते आणि नक्कल करणारी नाही. या विधानाने एका प्रमुख व्हिडिओतील प्रत्येक वक्त्याचे ऑडियो संच घेऊन ते प्रक्रिया करेल.
        """,
        "vc_active_label": "सक्रिय आवाज नक्कल",
        "vc_active_info": "सक्रिय आवाज नक्कल: मूळ वक्त्याचा आवाज पुनर्निर्मित करते",
        "vc_method_label": "पद्धत",
        "vc_method_info": "आवाज नक्कल प्रक्रियेसाठी एक पद्धत निवडा",
        "vc_segments_label": "कमाल सॅम्पल्स",
        "vc_segments_info": "कमाल सॅम्पल्स: प्रक्रियेसाठी ऑडियो सॅम्पल्सची संख्या आहे, अधिक चांगलं आहे परंतु ते आवाज जोडणारं करू शकतात",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: ऑडियो सॅम्पल्सवर ध्वनीक सांकेतिक दिवस लागू करते.",
        "vc_remove_label": "आधीचे सॅम्पल्स काढा",
        "vc_remove_info": "आधीचे सॅम्पल्स काढा: मागील सॅम्पल्स काढा: मागील सॅम्पल्स काढा, म्हणजे नवीन सामग्री करण्यासाठी त्या नवीन सॅम्पल्स बनवणे आवश्यक आहे.",
        "xtts_title": "ऑडियोवर आधारित TTS तयार करा",
        "xtts_subtitle": "आवाजासह 10 सेकंदांचा मोठा ऑडियो फाईल अपलोड करा. XTTS वापरून, दिलेल्या ऑडियो फाईलसोबत समान आवाजासह नवीन TTS तयार केला जाईल.",
        "xtts_file_label": "आवाजासह एक क्षिप्र ऑडियो अपलोड करा",
        "xtts_name_label": "TTS साठी नाव",
        "xtts_name_info": "एक साधा नाव वापरा",
        "xtts_dereverb_label": "ऑडियोवर ध्वनीक सांकेतिक दिवस लागू करा",
        "xtts_dereverb_info": "ऑडियोवर ध्वनीक सांकेतिक दिवस लागू करा: ऑडियोवर ध्वनीक सांकेतिक दिवस लागू करते",
        "xtts_button": "ऑडियो प्रक्रिया करा आणि त्यामध्ये समाविष्ट करा",
        "xtts_footer": "स्वयंचली आवाज XTTS उत्पादित करा: आपण TTS निवडकासाठी `_XTTS_/AUTOMATIC.wav` वापरू शकता, प्रत्येक वक्त्यासाठी नवीन सेगमेंट उत्पन्न करण्यासाठी आणि अनुवाद वापरताना एकत्रित करण्यासाठी।",
        "extra_setting": "उन्नत सेटिंग्ज",
        "acc_max_label": "ऑडियो अधिकतम एक्सेलरेशन",
        "acc_max_info": "ओव्हरलॅपिंग टाळण्यासाठी अनुवादित ऑडियो सेगमेंटसाठी अधिकतम एक्सेलरेशन. 1.0 ची एक मूल्य अधिकतम एक्सेलरेशन प्रतिनिधित्व करते",
        "acc_rate_label": "वेगवर्धी दर व्यवस्थापन",
        "acc_rate_info": "वेगवर्धी दर व्यवस्थापन: अल्प गतीचे आवश्यक असलेले क्षेत्र समायोजित करण्यासाठी वेगवर्धी व्यवस्थापन करते, सततता ठेवते आणि पुढील सुरुवातीचा वेळ मलान घेतला जातो.",
        "or_label": "ओव्हरलॅप कमी करा",
        "or_info": "ओव्हरलॅप कमी करा: मागील समाप्तीच्या वेळेस आधारित सुरुवातीच्या वेळा समायोजित करून सेगमेंट ओव्हरलॅप होण्यास रोखते; समकालिकरण अडचणी उत्पन्न करू शकतो.",
        "aud_mix_label": "ऑडियो मिक्सिंग पद्धत",
        "aud_mix_info": "स्वच्छ आणि संतुलित आउटपुट सादर करण्यासाठी मूळ आणि अनुवादित ऑडियो फाईल्स एकत्रित करण्यासाठी आवश्यक दोन मिक्सिंग मोड्युल्या सोडल्या आहेत.",
        "vol_ori": "मूळ ऑडियोची व्हॉल्यूम",
        "vol_tra": "अनुवादित ऑडियोची व्हॉल्यूम",
        "voiceless_tk_label": "आवाजरहित ट्रॅक",
        "voiceless_tk_info": "आवाजरहित ट्रॅक: अनुवादित ऑडियोसोबत संयुक्त करण्यापूर्वी मूळ ऑडियोची आवाजे काढा.",
        "sub_type": "उपशीर्षक प्रकार",
        "soft_subs_label": "कोमल सबटायटल्स",
        "soft_subs_info": "कोमल सबटायटल्स: दर्शक व्हिडिओ पाहताना चालू निशांत करू शकतात किंवा बंद करू शकतात.",
        "burn_subs_label": "सबटायटल्स जळवा",
        "burn_subs_info": "सबटायटल्स जळवा: व्हिडिओमध्ये सबटायटल्स आजार करा, त्यांना दृश्यांतराचा कोणताही स्थायी भाग बनवून करा.",
        "whisper_title": "वाचन विक्रमण संरचना.",
        "lnum_label": "संख्या शब्दांतर",
        "lnum_info": "संख्या शब्दांतर: अंकांचे प्रतिनिधित्व लेखित सर्वकाशांमध्ये बदला करा.",
        "scle_label": "आवाज स्वच्छता",
        "scle_info": "आवाज स्वच्छता: वादला तयार करण्यापूर्वी आवाज आणि बॅकग्राऊंड ध्वनी काढा. हे काम वेगवेगळ्या आवाज फाईल्ससह करता येऊ शकते.",
        "sd_limit_label": "सेगमेंट अवधी सीमा",
        "sd_limit_info": "प्रत्येक सेगमेंटसाठी कोणत्याही अवधीचा महासूचीत (सेकंदांमध्ये) सुनिश्चित करा. ऑडिओ वाडचा वापर करून प्रत्येक सेगमेंटच्या तुकड्याची अवधी सीमित करण्यात येईल.",
        "asr_model_info": "जीवनाचा मूळ 'फिस्फिंग' मॉडेल वापरून बोललेली भाषा ते टेक्स्टमध्ये बदलते. उदाहरणार्थ, चीनी भाषेतील फायनट्यून्ड मॉडेल वापरण्यासाठी ड्रॉपडाऊनमध्ये 'BELLE-2/Belle-whisper-large-v3-zh' संग्रह नाव नोंदवा. Hugging Face वर फायनट्यून्ड मॉडेल्स शोधा.",
        "ctype_label": "गणना प्रकार",
        "ctype_info": "int8 किंवा float16 आढळवून कमी डेटा प्रकारांमध्ये निर्देशन करणे कामाची वेगवेगळी प्रदर्शन करू शकते आणि गणना द्वारे अपेक्षित क्षमतेची वाढवू शकते, परंतु float32 आणि इतर मोठ्या डेटा प्रकारांपेक्षा निश्चितता कुठल्या प्रकारे कमी करू शकते.",
        "batchz_label": "बॅच आकार",
        "batchz_info": "आपल्याला कमी VRAM असलेले GPU असल्यास बॅच आकार कमी करणे मेमरी झटका आणू शकते आणि मेमरी नसलेली समस्या व्यवस्थापित करण्यास मदत करू शकते.",
        "tsscale_label": "टेक्स्ट सेगमेंटेशन पैमाना",
        "tsscale_info": "पाठाचे सेगमेंट वाक्य, शब्द किंवा अक्षरांमध्ये वागवा. शब्द आणि अक्षर सेगमेंटेशन उपशीर्षकसाठी उपयुक्त तंत्रज्ञान उपलब्ध करून देतात; अनुवाद बंद करणे मूल संरचना संरक्षित करते.",
        "srt_file_label": "एसआरटी उपशीर्षक फाईल अपलोड करा (व्हिस्परच्या विवेचनाच्या विरोधात वापरली जाईल)",
        "divide_text_label": "टेक्स्ट सेगमेंट्स पुनर्विभाजित करा:",
        "divide_text_info": "(प्रयोगशील) स्रोत भाषेतील विद्यमान टेक्स्ट सेगमेंट्सचा विभाग करण्यासाठी एक विभाजक प्रविष्ट करा. टूलला उपलब्धींना ओळखण्यासाठी आणि नुकसानकर्ता करण्यासाठी त्यामुळे नवीन सेगमेंट्स निर्मित करते. | चा वापर करून अनेक विभाजक स्पष्ट करा, उदा.: !|?|...|।",
        "diarization_label": "डायरिझेशन मॉडेल",
        "tr_process_label": "भाषांतर प्रक्रिया",
        "out_type_label": "आउटपुट प्रकार",
        "out_name_label": "फाईलचं नाव",
        "out_name_info": "आउटपुट फाईलचं नाव",
        "task_sound_label": "काम स्थिती आवाज",
        "task_sound_info": "काम स्थिती आवाज: काम संपल्याचे किंवा क्रियाकलापातील त्रुटी दर्शवणारा ध्वन आवाज करा.",
        "cache_label": "प्रगती पुनर्प्राप्त करा",
        "cache_info": "प्रगती पुनर्प्राप्त करा: शेवटचा चेकपॉईंट येथून प्रक्रिया सुरू करा.",
        "preview_info": "परीक्षणासाठी व्हिडिओला केवळ 10 सेकंदांसाठी कट्टा करते. कृपया पूर्ण व्हिडिओ अवधी प्राप्त करण्यासाठी हे निष्क्रिय करा.",
        "edit_sub_label": "तयार केलेले उपशीर्षक संपादित करा",
        "edit_sub_info": "तयार केलेले उपशीर्षक संपादित करा: अनुवाद करण्यासाठी 2 चरणांमध्ये अनुवाद चालवण्याची परवानगी देते. पहिल्यांदा 'उपशीर्षक मिळवा आणि संपादित करा' बटणावर क्लिक करून तुम्हाला उपशीर्षक मिळेल आणि त्या संपादित करण्यासाठी, आणि त्यानंतर 'अनुवाद' बटणावर क्लिक करून, आपण व्हिडिओ तयार करू शकता",
        "button_subs": "उपशीर्षक मिळवा आणि संपादित करा",
        "editor_sub_label": "तयार केलेले उपशीर्षक",
        "editor_sub_info": "येथील तयार केलेल्या उपशीर्षकांमध्ये टेक्स्ट संपादित करण्यासाठी मनःपूर्वक वापरा. आपण 'अनुवाद' बटणावर क्लिक करण्यापूर्वी, संवादीचे निवडणे, 'मूळ भाषा', 'ऑडियोचे अनुवाद करा', आणि 'अधिक स्पीकर्स' या अनुक्रमात किंवा संरचना विकल्प बदलू शकता, त्यांचा अशा चुकांवर टाकण्यासाठी. एकदा तुम्ही संपू नेल, 'अनुवाद' बटणावर क्लिक करा.",
        "editor_sub_ph": "प्रथम 'उपशीर्षक मिळवा आणि संपादित करा' बटणावर क्लिक करण्यात येतो",
        "button_translate": "अनुवाद करा",
        "output_result_label": "अनुवादित व्हिडिओ डाउनलोड करा",
        "sub_ori": "उपशीर्षक",
        "sub_tra": "अनुवादित उपशीर्षक",
        "ht_token_info": "एक महत्त्वाचं कार्य म्हणजे Pyannote वापरासाठी लायसेंस समजून घेणे. आपल्याला Hugging Face वर एक खाते असावी लागते आणि मॉडेल्स वापरण्यासाठी लायसेंस स्वीकारा लागते: https://huggingface.co/pyannote/speaker-diarization आणि https://huggingface.co/pyannote/segmentation. आपल्याला येथे आपला की टोकन मिळेल: https://hf.co/settings/tokens",
        "ht_token_ph": "टोकन येथे जाते...",
        "tab_docs": "कागदपत्र अनुवाद",
        "docs_input_label": "कागदपत्र स्रोत निवडा",
        "docs_input_info": "ते पीडीएफ, डॉक्स, टीएक्सट किंवा मजकूर होऊ शकते",
        "docs_source_info": "हे मजकूरची मूळ भाषा आहे",
        "chunk_size_label": "प्रत्येक सेगमेंट प्रत्येक करकटाने TTS ला प्रक्रिया करण्यासाठी अधिकतम अक्षरांची संख्या",
        "chunk_size_info": "0 चा मूल्य एक विनामूल्य आणि अधिक संगणकांसाठी संगणकात अधिक संगणकांसाठी अनुकूलित मूल्य नेमल्याची अर्थी होतो.",
        "docs_button": "भाषा कन्वर्ट ब्रिज सुरू करा",
        "cv_url_info": "यूआरएलपासून ऑटोमॅटिक रॉकी मॉडेल्स डाउनलोड करा. तुम्ही HuggingFace किंवा Drive ची लिंक वापरू शकता, आणि तुम्हाला किंवा तुम्हाला प्रत्येक लिंक, प्रत्येक लिंक समाविष्ट करण्यासाठी प्रत्येक लिंक वापरू शकता, प्रत्येक लिंक वापरू शकता. उदाहरण: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "आवाज बदला: TTS ते R.V.C.",
        "sec1_title": "### 1. त्याचा वापर सक्षम करण्यासाठी, ते सक्षम जाहीर करा.",
        "enable_replace": "मॉडेल्सचा वापर सक्षम करण्यासाठी हे तपासा.",
        "sec2_title": "### 2. प्रत्येक TTS च्या प्रत्येक प्रतिनिधीत्व करण्यासाठी आवाज निवडा आणि सेटिंग्ज लागू करा.",
        "sec2_subtitle": "आपण किती <TTS Speaker> वापरणार आहात यानुसार, प्रत्येकाने स्वत: च्या मॉडेलची आवश्यकता आहे. अधिक केल्यासाठी, अधिक स्पेकरच्या उपयोगासाठी एक सहाय्यक असते जर कारणाने वक्ता सही रिकामे ओळखले जात नाहीत.",
        "cv_tts1": "स्पीकर 1 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts2": "स्पीकर 2 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts3": "स्पीकर 3 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts4": "स्पीकर 4 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts5": "स्पीकर 5 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts6": "स्पीकर 6 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts7": "स्पीकर 7 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts8": "स्पीकर 8 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts9": "स्पीकर 9 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts10": "स्पीकर 10 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts11": "स्पीकर 11 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_tts12": "स्पीकर 12 साठी लागू करण्यासाठी आवाज निवडा.",
        "cv_aux": "- जर कारणाने वक्ता सही ओळखले जात नाही तर लागू करण्यासाठी आवाज.",
        "cv_button_apply": "सेटिंग्ज लागू करा",
        "tab_help": "मदत",
    },
    "azerbaijani": {
        "description": """
        ### 🎥 **SoniTranslate ilə videoları asanlıqla tərcümə edin!** 📽️

        Video, səs faylı yükləyin və ya YouTube bağlantısı təqdim edin. 📽️ **SoniTranslate-in rəsmi repositoriyasından yenilənmiş qeydləri alın: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        İstifadəsi üçün təlimatlar üçün `Kömək` sekmesinə baxın. Video tərcüməsi ilə əyləncəyə başlayaq! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **İstifadə təlimatları:**

        1. 📤 **Video**, **səs faylı** yükləyin və ya 🌐 **YouTube bağlantısı** təqdim edin.

        2. 🌍 **Videonu tərcümə etmək istədiyiniz dilə** seçin.

        3. 🗣️ **Videoda danışan insanların sayını** göstərin və **hər birinə uyğun tərcümə dilində məsələlərin səsləndirilməsi üçün tələb edilən səsləndirməni təyin edin.**

        4. 🚀 '**Tərcümə et**' düyməsini basın və nəticələri əldə edin.

        ---

        # 🧩 **SoniTranslate, fərqli TTS (Mətnə Səsləndirmə) mühərriklərini dəstəkləyir ki, onlar:**
        - EDGE-TTS → format `en-AU-WilliamNeural-Male` → Sürətli və dəqiqdir.
        - FACEBOOK MMS → format `en-facebook-mms VITS` → Səsi daha doğaldır; ancaq ancaq CPU istifadə edir.
        - PIPER TTS → format `en_US-lessac-high VITS-onnx` → Əvvəlki ilə eynidir, ancaq hem CPU, hem də GPU üçün optimalaşdırılmışdır.
        - BARK → format `en_speaker_0-Male BARK` → Yaxşı keyfiyyətli, ancaq yavaş və halüsinasiyalara meyllidir.
        - OpenAI TTS → format `>alloy OpenAI-TTS` → Çoxdilli, lakin OpenAI API açarı tələb olunur
        - Coqui XTTS → format `_XTTS_/AUTOMATIC.wav` → Yalnız Çin (Sadələşdirilmiş), İngilis, Fransız, Alman, İtalyan, Portuqal, Poliş, Türk, Rus, Holland, Çex, Ərəb, İspan, Macar, Korey və Yapon dilində mövcuddur.

        ---

        # 🎤 R.V.C. və R.V.C.2 Səsləri Necə İstifadə Etmək (İstəyə Bağlı) 🎶

        Məqsəd, tərtib olunmuş TTS (Mətnə Səsləndirmə) -ə bir R.V.C. tətbiq etməkdir 🎙️

        1. `Xüsusi Səs R.V.C.` tabınızda ehtiyacınız olan modelləri yükləyin 📥 Hugging Face və Google Drive-da linklərdən, zip, pth və ya index formatlarında istifadə edə bilərsiniz. HF məkan repositoriyalarını da yükləyə bilərsiniz, lakin bu seçim çox sabit deyil 😕

        2. İndi, `Səsləndiriciyi əvəzlə: TTS to R.V.C.` -ni işarələyin və `aktivləşdirmək` qutusunu seçin ✅ Bundan sonra, istədiyiniz modelləri hər bir TTS speaker üçün tətbiq edə bilərsiniz 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Bütün R.V.C. -yə tətbiq olunacaq F0 metodunu tənzimləyin 🎛️

        4. Dəyişiklikləri tətbiq etmək üçün `KONFİQURASYANI TƏTİBİ ET` düyməsini basın 🔄

        5. Video tərcüməsi tabınıza qayıdın və 'Tərcümə et'ə klikləyin ▶️ Artıq tərcümə, R.V.C. tətbiq edilərək həyata keçirilir 🗣️

        Məsləhət: R.V.C -ni təcrübə və ən yaxşı TTS və ya konfiqurasiyaları tapmaq üçün `Test R.V.C.` istifadə edə bilərsiniz 🧪🔍

        ---

        """,
        "tab_translate": "Video tərcüməsi",
        "video_source": "Video mənbəyi seçin",
        "link_label": "Mediya bağlantısı.",
        "link_info": "Nümunə: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL buraya daxil olur...",
        "dir_label": "Video Yolu.",
        "dir_info": "Nümunə: /usr/home/my_video.mp4",
        "dir_ph": "Yol buraya daxil olur...",
        "sl_label": "Mənbə dil",
        "sl_info": "Bu videoyun əsas dilidir",
        "tat_label": "Audio tərcüməsi",
        "tat_info": "Hədəf dil seçin və həmçinin o dil üçün uyğun olan TTS-i seçdiyinizdən əmin olun.",
        "num_speakers": "Videoda danışan insanların sayını seçin.",
        "min_sk": "Min speakerlər",
        "max_sk": "Max speakerlər",
        "tts_select": "Hər bir səsçiyə istədiyiniz səsi seçin.",
        "sk1": "TTS Səsçi 1",
        "sk2": "TTS Səsçi 2",
        "sk3": "TTS Səsçi 3",
        "sk4": "TTS Səsçi 4",
        "sk5": "TTS Səsçi 5",
        "sk6": "TTS Səsçi 6",
        "sk7": "TTS Səsçi 7",
        "sk8": "TTS Səsçi 8",
        "sk9": "TTS Səsçi 9",
        "sk10": "TTS Səsçi 10",
        "sk11": "TTS Səsçi 11",
        "sk12": "TTS Səsçi 12",
        "vc_title": "Fərqli dillərdə Səs İmələsi",
        "vc_subtitle": """
        ### Bir insanın səsini müxtəlif dillərdə çoğaldın.
        Əksər səslər üçün effektiv olsa da, hər halda tam mükəmməlliyətə nail olmayabilir.
        Səs imitasiyası sadəcə referans səsçinin tonunu çoxaldır, aksent və həssaslar, istifadə olunan əsas səsçi TTS modeli tərəfindən nəzarət olunur və çevirici tərəfindən çoğaldırılmır.
        Bu, hər səsçi üçün əsas səs məlumatlarını alır və onları işləyir.
        """,
        "vc_active_label": "Fəal Səs İmələsi",
        "vc_active_info": "Fəal Səs İmələsi: orijinal səsçinin tonunu çoğaldır",
        "vc_method_label": "Metod",
        "vc_method_info": "Səs İmələsi prosesində metod seçin",
        "vc_segments_label": "Maksimum nümunələr",
        "vc_segments_info": "Maksimum nümunələr: Proses üçün yaradılacaq səs nümunələrinin sayıdır, daha çoxu daha yaxşıdır, lakin gürültü əlavə edə bilər",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Səs nümunələrinə vokal dereverb tətbiq edir.",
        "vc_remove_label": "Əvvəlki nümunələri silin",
        "vc_remove_info": "Əvvəlki nümunələri silin: Əvvəlki yaradılmış nümunələri silir, beləliklə yeni olanları yaratmaq lazımdır.",
        "xtts_title": "Səsə əsaslanan bir TTS yaratın",
        "xtts_subtitle": "Maksimum 10 saniyəlik bir səs faylı yükləyin. XTTS istifadə edərək, müvafiq səslə bir TTS yeni bir səs yaradılacaq.",
        "xtts_file_label": "Səslə qısa bir səs yükləyin",
        "xtts_name_label": "TTS üçün ad",
        "xtts_name_info": "Sadə bir ad istifadə edin",
        "xtts_dereverb_label": "Səsi dereverb edin",
        "xtts_dereverb_info": "Səsi dereverb edin: Səsə vokal dereverb tətbiq edir",
        "xtts_button": "Səsi proses edin və TTS seçiciyə daxil edin",
        "xtts_footer": "Səs xtts-ini avtomatik olaraq yaradın: Tərcüməni yaratarkən hər səsçiyə avtomatik olaraq segmentlər yaratmaq üçün TTS seçicidə `_XTTS_/AUTOMATIC.wav` -dən istifadə edə bilərsiniz.",
        "extra_setting": "Əlavə Ayarlar",
        "acc_max_label": "Maksimum Audio sürəti",
        "acc_max_info": "Üstünlük təşkil etməmək üçün tərcümə olunmuş audio segmentlərinin maksimum sürəti. 1.0 dəyəri heç bir sürəti təşkil etmir",
        "acc_rate_label": "Sürətin Artımının Tənzimlənməsi",
        "acc_rate_info": "Sürətin Artımının Tənzimlənməsi: Sürəti az olan segmentlərə uyğun olaraq sürəti tənzimləyir, davam etməni qoruyur və növbəti başlanğıcın vaxtını nəzərə alır.",
        "or_label": "Üstünlüklərin Azaldılması",
        "or_info": "Üstünlüklərin Azaldılması: Segmentlərin bir-birinin üstündə olmamasını təmin edir, əvvəlki bitiş vaxtlarına əsasən başlanğıc vaxtlarını tənzimləyərək; sinxronlaşmaya mane ola bilər.",
        "aud_mix_label": "Audio qarışdırma metodları",
        "aud_mix_info": "Orijinal və tərcümə olunmuş audio fayllarını qarışdıraraq iki mövcud qarışdırma rejimi ilə xüsusi, dengəli bir çıxış yaradın.",
        "vol_ori": "Orijinal səsin səsi",
        "vol_tra": "Tərcümə olunmuş audio səsi",
        "voiceless_tk_label": "Səssiz Trekk",
        "voiceless_tk_info": "Səssiz Trekk: Tərcümə olunmuş audio ilə birləşdirilmədən əvvəl orijinal audio səsini silin.",
        "sub_type": "Subtitrlərin növü",
        "soft_subs_label": "Yumuşaq Subtitrlər",
        "soft_subs_info": "Yumuşaq Subtitrlər: İzləyicilərin videonu izləyərkən açıb bağlaya biləcəyi seçməlik subtitrlər.",
        "burn_subs_label": "Altyazıları Yanma",
        "burn_subs_info": "Altyazıları Yanma: Altyazıları videoya ilave edərək, onları görünən məzmunun daimi bir hissəsi halına gətirin.",
        "whisper_title": "Tərcümə edilən mətnin konfiqurasiyası.",
        "lnum_label": "Rəqəmləri Litarallarlaşdırmaq",
        "lnum_info": "Rəqəmləri Litarallarlaşdırmaq: Sayısal təsvirləri onların yazılı müqabilələri ilə əvəzləyin.",
        "scle_label": "Səs Təmizliyi",
        "scle_info": "Səs Təmizliyi: Maksimum vaxt damğası dəqiqliyi üçün səsi yaxşılaşdırın, transkripsiyadan əvvəl fon gürültüsünü çıxarın. Bu əməliyyat uzun səs faylları ilə xüsusilə vaxt ala bilər.",
        "sd_limit_label": "Segment Müddəti Məhdudiyyəti",
        "sd_limit_info": "Hər bir segment üçün maksimum müddəti (saniyə) təyin edin. Səs VAD-dan istifadə edilərək hər bir segment parçasının müddəti məhdudlaşdırılacaq.",
        "asr_model_info": "Bu, default olaraq danışılan dilə mətni 'Əfsus' modeli istifadə edərək mətnə çevirir. Xüsusi model istifadə edin, məsələn, çin dilində fayin-tuninq edilmiş model istifadə etmək üçün 'BELLE-2/Belle-whisper-large-v3-zh' depozit adını keçid menyusuna daxil edin. Hugging Face-də fayin-tuninq edilmiş modelləri tapın.",
        "ctype_label": "Hesablama Növü",
        "ctype_info": "int8 və ya float16 kimi kiçik növ seçmək yaddaş istifadəsini azaldaraq və hesablama nəzarətini artıraraq performansı yaxşılaşdıra bilər, lakin float32 kimi daha böyük veri növlərinə nisbətən dəqiqliyi fəda etmək olar.",
        "batchz_label": "Toplu Ölçüsü",
        "batchz_info": "Toplu ölçüsünü azaldaraq, əğer GPU-nuzun az VRAM varsa, yaddaş qənaət etmək mümkündür və Yaddaşsız Yaddaş problemə idarə edə bilər.",
        "tsscale_label": "Mətn Segmentlərinin Masshtabı",
        "tsscale_info": "Mətni cümlə, söz və ya simvollarla segmentlərə bölmək. Söz və simvol bölməsi, subtitrlər üçün faydalı olan daha dəqiqliyi təmin edir; tərcüməni söndürmək asal strukturu qoruyur.",
        "srt_file_label": "Bir SRT subtitri faylı yükləyin (Fısıldağın transkripsiyası əvəzinə istifadə olunacaq)",
        "divide_text_label": "Mətn segmentlərini bölmək üçün ayırıcı daxil edin:",
        "divide_text_info": "(Təcrübəli) Mövcud mətn segmentlərini böləcək bir ayırıcı daxil edin. Alətlər tez-tez yaradır və uyğun gələn yerlərdə yeni segmentlər yaradır. Birdən çox ayırıcı daxil edin, |, misal: !|?|...|。",
        "diarization_label": "Diyarizasiya Modeli",
        "tr_process_label": "Tərcümə Prosesi",
        "out_type_label": "Çıxış növü",
        "out_name_label": "Fayl adı",
        "out_name_info": "Çıxış faylının adı",
        "task_sound_label": "Tapşırığın Vəziyyət Səsi",
        "task_sound_info": "Tapşırığın Vəziyyət Səsi: Tapşırığın başa çatdığını və ya icra zamanı xətalıları göstərən səsli xəbərdarlıq səsi oxuyur.",
        "cache_label": "İrəliyə Alma İşləmi",
        "cache_info": "İrəliyə Alma İşləmi: Son yoxlama nöqtəsindən davam etmək.",
        "preview_info": "Təcrübə məqsədi ilə videoyu yalnız 10 saniyəyə kəsir. Tam video müddətini əldə etmək üçün onu deaktiv edin.",
        "edit_sub_label": "Yaradılan subtitrləri redaktə edin",
        "edit_sub_info": "Yaradılan subtitrləri redaktə edin: Tərcüməni 2 addımlı olaraq başlatmaq üçün olan imkan. İlk olaraq 'SUBTITRİ AL VƏ REDAKTƏ ET' düyməsini basaraq subtitrləri alın, onları redaktə edin və sonra 'TƏRCÜMƏ ET' düyməsini basaraq video yarada bilərsiniz",
        "button_subs": "SUBTITRİ AL VƏ REDAKTƏ ET",
        "editor_sub_label": "Yaradılan subtitrlər",
        "editor_sub_info": "Burada yaradılan subtitrlərdə mətni redaktə etmək azadır. Interfeys seçimlərini dəyişdirə bilərsiniz, lakin xəbərdarlıq olaraq 'Mənbə dil', 'Audio tərcüməsi' və 'Max speakerlər' üçün xətalara yol verməmək üçün, 'TƏRCÜMƏ ET' düyməsini basmadan əvvəl. Bitdikdən sonra, 'TƏRCÜMƏ ET' düyməsini basın.",
        "editor_sub_ph": "İlk olaraq 'SUBTITRİ AL VƏ REDAKTƏ ET' düyməsini basın və subtitrləri alın",
        "button_translate": "TƏRCÜMƏ ET",
        "output_result_label": "TƏRCÜMƏ OLUNMUŞ VİDEOYU YÜKLƏYİN",
        "sub_ori": "Subtitrlər",
        "sub_tra": "Tərcümə olunmuş subtitrlər",
        "ht_token_info": "Pyannote istifadəsi üçün lisenziya razılaşmasını qəbul etmək önəmli addımdır. Model istifadə etmək üçün Hugging Face-da hesabınız olmalı və modelləri istifadə etmək üçün lisenziya qəbul etməlisiniz: https://huggingface.co/pyannote/speaker-diarization və https://huggingface.co/pyannote/segmentation. Özüncə TOKENİNİZİ buradan əldə edin: https://hf.co/settings/tokens",
        "ht_token_ph": "Token buraya daxil olur...",
        "tab_docs": "Sənəd tərcüməsi",
        "docs_input_label": "Sənəd mənbəyini seçin",
        "docs_input_info": "PDF, DOCX, TXT və ya mətn ola bilər",
        "docs_source_info": "Bu mətnin əsas dili",
        "chunk_size_label": "TTS-in hər segmenti üçün təşkil olunan maksimum simvolların sayı",
        "chunk_size_info": "0 dəyəri TTS üçün dinamik və daha uyğun bir dəyər təyin edir.",
        "docs_button": "Dil Dəyişikliyi Köprüsünü Başlat",
        "cv_url_info": "R.V.C. modellərini URL-dən avtomatik olaraq yükləyin. HuggingFace və Drive linklərindən istifadə edə bilərsiniz, və hər birini vergül ilə ayrılmış bir neçə link daxil edə bilərsiniz. Misal: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Səs əvəzləmə: TTS-dən R.V.C.-yə",
        "sec1_title": "### 1. İstifadəsini aktivləşdirmək üçün onu aktiv edin.",
        "enable_replace": "Bu modellərin istifadəsini aktivləşdirmək üçün bunu işarələyin.",
        "sec2_title": "### 2. Hər bir uyğun səsçi TTS-ə tətbiq olunacaq səsi seçin və konfiqurasiyaları tətbiq edin.",
        "sec2_subtitle": "Istifadə edəcəyiniz <TTS Səsçisi> sayına bağlı olaraq, hər biri öz modellərinə ehtiyac duyar. Əlavə olaraq, səsçi doğru şəkildə aşkar edilmirsə yardımcı bir tətbiqi mövcuddur.",
        "cv_tts1": "1-ci Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts2": "2-ci Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts3": "3-cü Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts4": "4-cü Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts5": "5-ci Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts6": "6-cı Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts7": "7-ci Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts8": "8-ci Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts9": "9-cu Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts10": "10-cu Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts11": "11-ci Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_tts12": "12-ci Səsçi üçün tətbiq olunacaq səsi seçin.",
        "cv_aux": "- Səsçi doğru şəkildə aşkar edilmirsə tətbiq ediləcək səs.",
        "cv_button_apply": "KONFiQURASiYANI TƏTBiQ EDiN",
        "tab_help": "Kömək",
    },

    "persian": {
        "description": """
        ### 🎥 **با SoniTranslate به راحتی ویدئوها را ترجمه کنید!** 📽️

        یک ویدئو، فایل زیرنویس، فایل صوتی را آپلود کنید یا یک لینک ویدئوی URL ارائه دهید. 📽️ **دفترچه یادداشت به‌روز شده را از مخزن رسمی دریافت کنید: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        دستورالعمل‌های استفاده را در تب `Help` ببینید. بیایید با ترجمه ویدئوها سرگرم شویم! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **دستورالعمل استفاده:**

        1. 📤 یک **ویدئو**، **فایل زیرنویس**، **فایل صوتی** را آپلود کنید یا 🌐 **لینک URL** به یک ویدئو مانند یوتیوب ارائه دهید.

        2. 🌍 زبانی را که می‌خواهید **ویدئو را به آن ترجمه کنید** انتخاب کنید.

        3. 🗣️ تعداد **افراد گوینده** در ویدئو را مشخص کنید و **برای هرکدام یک صدای متن به گفتار مناسب** برای زبان ترجمه انتخاب کنید.

        4. 🚀 دکمه '**ترجمه**' را فشار دهید تا نتایج را دریافت کنید.

        ---

        # 🧩 **SoniTranslate از موتورهای مختلف TTS (متن به گفتار) پشتیبانی می‌کند، که شامل:**
        - EDGE-TTS → فرمت `en-AU-WilliamNeural-Male` → سریع و دقیق.
        - FACEBOOK MMS → فرمت `en-facebook-mms VITS` → صدای طبیعی‌تر؛ در حال حاضر فقط از CPU استفاده می‌کند.
        - PIPER TTS → فرمت `en_US-lessac-high VITS-onnx` → مانند قبلی، اما برای CPU و GPU بهینه‌سازی شده است.
        - BARK → فرمت `en_speaker_0-Male BARK` → کیفیت خوب ولی کند و مستعد هذیان.
        - OpenAI TTS → فرمت `>alloy OpenAI-TTS` → چندزبانه اما نیاز به کلید API OpenAI دارد.
        - Coqui XTTS → فرمت `_XTTS_/AUTOMATIC.wav` → فقط برای چینی (ساده‌شده)، انگلیسی، فرانسوی، آلمانی، ایتالیایی، پرتغالی، لهستانی، ترکی، روسی، هلندی، چک، عربی، اسپانیایی، مجارستانی، کره‌ای و ژاپنی در دسترس است.

        ---

        # 🎤 چگونه از صداهای R.V.C. و R.V.C.2 استفاده کنیم (اختیاری) 🎶

        هدف اعمال R.V.C. به TTS تولید شده است 🎙️

        1. در تب `Custom Voice R.V.C.` مدل‌های مورد نیاز را دانلود کنید 📥 می‌توانید از لینک‌های Hugging Face و Google Drive در قالب‌های zip، pth، یا index استفاده کنید. همچنین می‌توانید مخازن کامل HF را دانلود کنید، اما این گزینه خیلی پایدار نیست 😕

        2. حالا به `Replace voice: TTS to R.V.C.` بروید و جعبه `enable` را تیک بزنید ✅ پس از این، می‌توانید مدل‌هایی را که می‌خواهید به هر سخنگوی TTS اعمال کنید انتخاب کنید 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. روش F0 که برای همه R.V.C. اعمال خواهد شد تنظیم کنید 🎛️

        4. دکمه `APPLY CONFIGURATION` را فشار دهید تا تغییرات اعمال شود 🔄

        5. به تب ترجمه ویدئو بازگردید و بر روی 'Translate' کلیک کنید ▶️ حالا ترجمه با اعمال R.V.C. انجام خواهد شد 🗣️

        نکته: می‌توانید از `Test R.V.C.` استفاده کنید تا بهترین TTS یا تنظیمات را برای اعمال به R.V.C. آزمایش و پیدا کنید 🧪🔍

        ---

        """,
        "tab_translate": "ترجمه ویدئو",
        "video_source": "منبع ویدئو را انتخاب کنید",
        "link_label": "لینک رسانه.",
        "link_info": "مثال: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "لینک URL را اینجا وارد کنید...",
        "dir_label": "مسیر ویدئو.",
        "dir_info": "مثال: /usr/home/my_video.mp4",
        "dir_ph": "مسیر را اینجا وارد کنید...",
        "sl_label": "زبان مبدا",
        "sl_info": "این زبان اصلی ویدئو است",
        "tat_label": "ترجمه صوتی به",
        "tat_info": "زبان مقصد را انتخاب کنید و همچنین مطمئن شوید که TTS مربوط به آن زبان را انتخاب کنید.",
        "num_speakers": "تعداد افراد گوینده در ویدئو را انتخاب کنید.",
        "min_sk": "حداقل گوینده‌ها",
        "max_sk": "حداکثر گوینده‌ها",
        "tts_select": "صدای مورد نظر برای هر گوینده را انتخاب کنید.",
        "sk1": "گوینده TTS 1",
        "sk2": "گوینده TTS 2",
        "sk3": "گوینده TTS 3",
        "sk4": "گوینده TTS 4",
        "sk5": "گوینده TTS 5",
        "sk6": "گوینده TTS 6",
        "sk7": "گوینده TTS 7",
        "sk8": "گوینده TTS 8",
        "sk9": "گوینده TTS 9",
        "sk10": "گوینده TTS 10",
        "sk11": "گوینده TTS 11",
        "sk12": "گوینده TTS 12",
        "vc_title": "تقلید صدا در زبان‌های مختلف",
        "vc_subtitle": """
        ### صدای یک فرد را در زبان‌های مختلف بازتولید کنید.
        در حالی که با اکثر صداها به درستی کار می‌کند، ممکن است در هر مورد به صورت کامل عمل نکند.
        تقلید صدا تنها لحن گوینده مرجع را بازتولید می‌کند، بدون لهجه و احساسات که توسط مدل پایه TTS تعیین می‌شوند و توسط مبدل بازتولید نمی‌شوند.
        این کار نمونه‌های صوتی را از صدای اصلی هر گوینده گرفته و پردازش می‌کند.
        """,
        "vc_active_label": "تقلید صدا فعال است",
        "vc_active_info": "تقلید صدا فعال: لحن گوینده اصلی را بازتولید می‌کند",
        "vc_method_label": "روش",
        "vc_method_info": "یک روش برای فرآیند تقلید صدا انتخاب کنید",
        "vc_segments_label": "حداکثر نمونه‌ها",
        "vc_segments_info": "حداکثر نمونه‌ها: تعداد نمونه‌های صوتی که برای فرآیند تولید خواهند شد، بیشتر بهتر است اما ممکن است نویز اضافه کند",
        "vc_dereverb_label": "حذف اکو",
        "vc_dereverb_info": "حذف اکو: حذف اکو صوتی از نمونه‌های صوتی.",
        "vc_remove_label": "حذف نمونه‌های قبلی",
        "vc_remove_info": "حذف نمونه‌های قبلی: حذف نمونه‌های قبلی تولید شده، بنابراین نمونه‌های جدید نیاز به تولید دارند.",
        "xtts_title": "ایجاد TTS بر اساس یک فایل صوتی",
        "xtts_subtitle": "یک فایل صوتی کوتاه با صدای حداکثر 10 ثانیه آپلود کنید. با استفاده از XTTS، یک TTS جدید با صدای مشابه به فایل صوتی ارائه شده ایجاد خواهد شد.",
        "xtts_file_label": "یک فایل صوتی کوتاه با صدا آپلود کنید",
        "xtts_name_label": "نام برای TTS",
        "xtts_name_info": "یک نام ساده استفاده کنید",
        "xtts_dereverb_label": "حذف اکو صوتی",
        "xtts_dereverb_info": "حذف اکو صوتی: حذف اکو از صوت",
        "xtts_button": "پردازش صوت و افزودن آن به انتخابگر TTS",
        "xtts_footer": "تولید صدای XTTS به طور خودکار: می‌توانید از `_XTTS_/AUTOMATIC.wav` در انتخابگر TTS برای تولید خودکار بخش‌ها برای هر گوینده هنگام تولید ترجمه استفاده کنید.",
        "extra_setting": "تنظیمات پیشرفته",
        "acc_max_label": "حداکثر شتاب صوتی",
        "acc_max_info": "حداکثر شتاب برای بخش‌های صوتی ترجمه شده برای جلوگیری از تداخل. مقدار 1.0 نمایانگر بدون شتاب است",
        "acc_rate_label": "تنظیم نرخ شتاب",
        "acc_rate_info": "تنظیم نرخ شتاب: تنظیم شتاب برای سازگاری با بخش‌هایی که نیاز به سرعت کمتری دارند، حفظ پیوستگی و در نظر گرفتن زمان شروع بعدی.",
        "or_label": "کاهش تداخل",
        "or_info": "کاهش تداخل: اطمینان از عدم تداخل بخش‌ها با تنظیم زمان شروع بر اساس زمان پایان قبلی؛ ممکن است همگام‌سازی را مختل کند.",
        "aud_mix_label": "روش ترکیب صوتی",
        "aud_mix_info": "میکس فایل‌های صوتی اصلی و ترجمه شده برای ایجاد خروجی سفارشی و متعادل با دو حالت میکس موجود.",
        "vol_ori": "حجم صدای اصلی",
        "vol_tra": "حجم صدای ترجمه شده",
        "voiceless_tk_label": "مسیر بدون صدا",
        "voiceless_tk_info": "مسیر بدون صدا: حذف صدای اصلی قبل از ترکیب آن با صدای ترجمه شده.",
        "sub_type": "نوع زیرنویس",
        "soft_subs_label": "زیرنویس نرم",
        "soft_subs_info": "زیرنویس نرم: زیرنویس‌های اختیاری که بینندگان می‌توانند آنها را هنگام تماشا روشن یا خاموش کنند.",
        "burn_subs_label": "زیرنویس سوخته",
        "burn_subs_info": "زیرنویس سوخته: تعبیه زیرنویس‌ها در ویدئو، که آنها را به بخشی دائمی از محتوای بصری تبدیل می‌کند.",
        "whisper_title": "پیکربندی رونوشت.",
        "lnum_label": "نوشتاری اعداد",
        "lnum_info": "نوشتاری اعداد: جایگزین نمایش عددی با معادل‌های نوشتاری آنها در رونوشت.",
        "scle_label": "پاکسازی صدا",
        "scle_info": "پاکسازی صدا: تقویت صداها، حذف نویز پس‌زمینه قبل از رونوشت برای دقت زمان‌بندی بالا. این عملیات ممکن است زمان ببرد، به ویژه با فایل‌های صوتی طولانی.",
        "sd_limit_label": "حداکثر مدت زمان بخش",
        "sd_limit_info": "حداکثر مدت زمان برای هر بخش را مشخص کنید. صوت با استفاده از VAD پردازش خواهد شد، و مدت زمان برای هر بخش محدود خواهد شد.",
        "asr_model_info": "این مدل زبان گفتاری را به متن تبدیل می‌کند و از مدل 'Whisper' به‌صورت پیش‌فرض استفاده می‌کند. از یک مدل سفارشی استفاده کنید، برای مثال، با وارد کردن نام مخزن 'BELLE-2/Belle-whisper-large-v3-zh' در لیست کشویی برای استفاده از مدل چینی فاین‌تیون شده. مدل‌های فاین‌تیون شده را در Hugging Face پیدا کنید.",
        "ctype_label": "نوع محاسبه",
        "ctype_info": "انتخاب انواع کوچکتر مانند int8 یا float16 می‌تواند عملکرد را با کاهش استفاده از حافظه و افزایش توان محاسباتی بهبود بخشد، اما ممکن است دقت را نسبت به انواع داده‌های بزرگ‌تر مانند float32 فدا کند.",
        "batchz_label": "اندازه دسته",
        "batchz_info": "کاهش اندازه دسته حافظه را ذخیره می‌کند اگر GPU شما VRAM کمتری دارد و کمک می‌کند به مدیریت مشکلات کمبود حافظه.",
        "tsscale_label": "مقیاس بخش‌بندی متن",
        "tsscale_info": "تقسیم متن به بخش‌ها با جملات، کلمات، یا کاراکترها. بخش‌بندی کلمه و کاراکتر دانه‌بندی بیشتری ارائه می‌دهد که برای زیرنویس‌ها مفید است؛ غیرفعال کردن ترجمه ساختار اصلی را حفظ می‌کند.",
        "srt_file_label": "یک فایل زیرنویس SRT آپلود کنید (به جای رونوشت Whisper استفاده خواهد شد)",
        "divide_text_label": "تقسیم مجدد بخش‌های متن توسط:",
        "divide_text_info": "(آزمایشی) یک جداکننده برای تقسیم بخش‌های موجود متن در زبان منبع وارد کنید. ابزار وقوع‌ها را شناسایی کرده و بخش‌های جدید را بر اساس آن ایجاد می‌کند. چندین جداکننده را با | مشخص کنید، به عنوان مثال: !|?|...|。",
        "diarization_label": "مدل دیاریزیشن",
        "tr_process_label": "فرآیند ترجمه",
        "out_type_label": "نوع خروجی",
        "out_name_label": "نام فایل",
        "out_name_info": "نام فایل خروجی",
        "task_sound_label": "صدای وضعیت کار",
        "task_sound_info": "صدای وضعیت کار: پخش صدای هشدار نشان‌دهنده تکمیل کار یا خطاها در حین اجرا.",
        "cache_label": "بازیابی پیشرفت",
        "cache_info": "بازیابی پیشرفت: ادامه فرآیند از آخرین نقطه توقف.",
        "preview_info": "پیش‌نمایش ویدئو را به 10 ثانیه برای آزمایش برش می‌دهد. لطفاً آن را غیرفعال کنید تا ویدئوی کامل را دریافت کنید.",
        "edit_sub_label": "ویرایش زیرنویس‌های تولید شده",
        "edit_sub_info": "ویرایش زیرنویس‌های تولید شده: به شما امکان می‌دهد ترجمه را در دو مرحله انجام دهید. ابتدا با دکمه 'GET SUBTITLES AND EDIT' زیرنویس‌ها را بگیرید و ویرایش کنید، و سپس با دکمه 'TRANSLATE' ویدئو را تولید کنید",
        "button_subs": "GET SUBTITLES AND EDIT",
        "editor_sub_label": "زیرنویس‌های تولید شده",
        "editor_sub_info": "می‌توانید متن زیرنویس‌های تولید شده را اینجا ویرایش کنید. قبل از کلیک بر روی دکمه 'TRANSLATE' می‌توانید تغییرات را در گزینه‌های رابط ایجاد کنید، به جز 'زبان منبع'، 'ترجمه صوتی به' و 'حداکثر گوینده‌ها'، تا از بروز خطاها جلوگیری شود. پس از اتمام، دکمه 'TRANSLATE' را فشار دهید.",
        "editor_sub_ph": "ابتدا دکمه 'GET SUBTITLES AND EDIT' را فشار دهید تا زیرنویس‌ها را دریافت کنید",
        "button_translate": "TRANSLATE",
        "output_result_label": "دانلود ویدئوی ترجمه شده",
        "sub_ori": "زیرنویس‌ها",
        "sub_tra": "زیرنویس‌های ترجمه شده",
        "ht_token_info": "یکی از مراحل مهم قبول موافقتنامه مجوز برای استفاده از Pyannote است. شما نیاز به داشتن یک حساب کاربری در Hugging Face و قبول مجوز برای استفاده از مدل‌ها دارید: https://huggingface.co/pyannote/speaker-diarization و https://huggingface.co/pyannote/segmentation. کلید TOKEN خود را اینجا بگیرید: https://hf.co/settings/tokens",
        "ht_token_ph": "کلید TOKEN را اینجا وارد کنید...",
        "tab_docs": "ترجمه اسناد",
        "docs_input_label": "منبع سند را انتخاب کنید",
        "docs_input_info": "می‌تواند PDF، DOCX، TXT، یا متن باشد",
        "docs_source_info": "این زبان اصلی متن است",
        "chunk_size_label": "حداکثر تعداد کاراکترهایی که TTS در هر بخش پردازش خواهد کرد",
        "chunk_size_info": "مقدار 0 یک مقدار پویا و سازگارتر برای TTS اختصاص می‌دهد.",
        "docs_button": "شروع پل تبدیل زبان",
        "cv_url_info": "مدل‌های R.V.C. را به صورت خودکار از URL دانلود کنید. می‌توانید از لینک‌های HuggingFace یا Drive استفاده کنید و می‌توانید چندین لینک را شامل کنید، هرکدام با کاما جدا شده باشند. مثال: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "تعویض صدا: TTS به R.V.C.",
        "sec1_title": "### 1. برای فعال‌سازی استفاده، آن را به عنوان فعال علامت بزنید.",
        "enable_replace": "این را بررسی کنید تا استفاده از مدل‌ها فعال شود.",
        "sec2_title": "### 2. صدایی را که به هر TTS هر گوینده اعمال خواهد شد انتخاب کنید و تنظیمات را اعمال کنید.",
        "sec2_subtitle": "بسته به تعداد <گوینده TTS> که استفاده می‌کنید، هرکدام به مدل مربوطه خود نیاز دارند. علاوه بر این، یک مدل کمکی نیز وجود دارد که در صورت عدم تشخیص صحیح گوینده استفاده می‌شود.",
        "cv_tts1": "صدایی را برای گوینده 1 انتخاب کنید.",
        "cv_tts2": "صدایی را برای گوینده 2 انتخاب کنید.",
        "cv_tts3": "صدایی را برای گوینده 3 انتخاب کنید.",
        "cv_tts4": "صدایی را برای گوینده 4 انتخاب کنید.",
        "cv_tts5": "صدایی را برای گوینده 5 انتخاب کنید.",
        "cv_tts6": "صدایی را برای گوینده 6 انتخاب کنید.",
        "cv_tts7": "صدایی را برای گوینده 7 انتخاب کنید.",
        "cv_tts8": "صدایی را برای گوینده 8 انتخاب کنید.",
        "cv_tts9": "صدایی را برای گوینده 9 انتخاب کنید.",
        "cv_tts10": "صدایی را برای گوینده 10 انتخاب کنید.",
        "cv_tts11": "صدایی را برای گوینده 11 انتخاب کنید.",
        "cv_tts12": "صدایی را برای گوینده 12 انتخاب کنید.",
        "cv_aux": "- صدایی که در صورت عدم تشخیص موفقیت‌آمیز گوینده اعمال خواهد شد.",
        "cv_button_apply": "اعمال تنظیمات",
        "tab_help": "کمک",
    },

    "afrikaans": {
        "description": """
        ### 🎥 **Vertaal video's maklik met SoniTranslate!** 📽️

        Laai 'n video, onderskrif, klanklêer op of verskaf 'n URL-videolink. 📽️ **Kry die opgedateerde notaboek van die amptelike repository: [SoniTranslate](https://github.com/R3gm/SoniTranslate)!**

        Sien die tab 'Hulp' vir instruksies oor hoe om dit te gebruik. Kom ons begin pret hê met videovertaal! 🚀🎉
        """,
        "tutorial": """
        # 🔰 **Instruksies vir gebruik:**

        1. 📤 Laai 'n **video**, **onderskriflêer**, **klanklêer** op of verskaf 'n 🌐 **URL link** na 'n video soos YouTube.

        2. 🌍 Kies die taal waarin jy die **video wil vertaal**.

        3. 🗣️ Spesifiseer die **aantal mense wat praat** in die video en **ken elkeen 'n teks-na-spraak-stem toe** wat geskik is vir die vertalingstaal.

        4. 🚀 Druk die '**Vertaal**' knoppie om die resultate te verkry.

        ---

        # 🧩 **SoniTranslate ondersteun verskillende TTS (Teks-na-Spraak) enjins, wat is:**
        - EDGE-TTS → formaat `en-AU-WilliamNeural-Male` → Vinnig en akkuraat.
        - FACEBOOK MMS → formaat `en-facebook-mms VITS` → Die stem is meer natuurlik; op die oomblik gebruik dit net CPU.
        - PIPER TTS → formaat `en_US-lessac-high VITS-onnx` → Dieselfde as die vorige een, maar dit is geoptimaliseer vir beide CPU en GPU.
        - BARK → formaat `en_speaker_0-Male BARK` → Goeie kwaliteit maar stadig, en dit is geneig tot hallusinasies.
        - OpenAI TTS → formaat `>alloy OpenAI-TTS` → Veeltalig maar dit benodig 'n OpenAI API sleutel.
        - Coqui XTTS → formaat `_XTTS_/AUTOMATIC.wav` → Slegs beskikbaar vir Vereenvoudigde Chinees, Engels, Frans, Duits, Italiaans, Portugees, Pools, Turks, Russies, Nederlands, Tsjeggies, Arabies, Spaans, Hongaars, Koreaans en Japanees.

        ---

        # 🎤 Hoe om R.V.C. en R.V.C.2 Stemmen te Gebruik (Opsioneel) 🎶

        Die doel is om 'n R.V.C. toe te pas op die gegenereerde TTS (Teks-na-Spraak) 🎙️

        1. In die `Aangepaste Stem R.V.C.` tab, laai die modelle af wat jy benodig 📥 Jy kan skakels van Hugging Face en Google Drive in formate soos zip, pth, of index gebruik. Jy kan ook volledige HF-ruimte-repositories aflaai, maar hierdie opsie is nie baie stabiel nie 😕

        2. Gaan nou na `Vervang stem: TTS na R.V.C.` en merk die `aktiveer` boks ✅ Na dit, kan jy die modelle kies wat jy wil toepas op elke TTS spreker 👩‍🦰👨‍🦱👩‍🦳👨‍🦲

        3. Pas die F0 metode aan wat toegepas sal word op alle R.V.C. 🎛️

        4. Druk `PAS KONFIGURASIE TOE` om die veranderinge wat jy gemaak het toe te pas 🔄

        5. Gaan terug na die videovertaal tab en klik op 'Vertaal' ▶️ Nou sal die vertaling gedoen word met die toepassing van die R.V.C. 🗣️

        Wenke: Jy kan `Toets R.V.C.` gebruik om te eksperimenteer en die beste TTS of konfigurasies te vind om op die R.V.C. toe te pas 🧪🔍

        ---

        """,
        "tab_translate": "Videovertaal",
        "video_source": "Kies Video Bron",
        "link_label": "Media link.",
        "link_info": "Voorbeeld: www.youtube.com/watch?v=g_9rPvbENUw",
        "link_ph": "URL gaan hier...",
        "dir_label": "Video Pad.",
        "dir_info": "Voorbeeld: /usr/home/my_video.mp4",
        "dir_ph": "Pad gaan hier...",
        "sl_label": "Bron taal",
        "sl_info": "Dit is die oorspronklike taal van die video",
        "tat_label": "Vertaal klank na",
        "tat_info": "Kies die teikentaal en maak ook seker om die ooreenstemmende TTS vir daardie taal te kies.",
        "num_speakers": "Kies hoeveel mense praat in die video.",
        "min_sk": "Min sprekers",
        "max_sk": "Max sprekers",
        "tts_select": "Kies die stem wat jy vir elke spreker wil hê.",
        "sk1": "TTS Spreker 1",
        "sk2": "TTS Spreker 2",
        "sk3": "TTS Spreker 3",
        "sk4": "TTS Spreker 4",
        "sk5": "TTS Spreker 5",
        "sk6": "TTS Spreker 6",
        "sk7": "TTS Spreker 7",
        "sk8": "TTS Spreker 8",
        "sk9": "TTS Spreker 9",
        "sk10": "TTS Spreker 10",
        "sk11": "TTS Spreker 11",
        "sk12": "TTS Spreker 12",
        "vc_title": "Stem Nabootsing in Verskillende Tale",
        "vc_subtitle": """
        ### Herhaal 'n persoon se stem oor verskeie tale.
        Terwyl effektief met die meeste stemme wanneer gepas gebruik, mag dit nie perfek wees in elke geval nie.
        Stem Nabootsing herhaal slegs die verwysingspreker se toon, sonder aksent en emosie, wat deur die basispreker TTS model beheer word en nie deur die omskakelaar nageboots word nie.
        Dit sal oudio monsters van die hoof oudio neem vir elke spreker en hulle verwerk.
        """,
        "vc_active_label": "Aktiewe Stem Nabootsing",
        "vc_active_info": "Aktiewe Stem Nabootsing: Herhaal die oorspronklike spreker se toon",
        "vc_method_label": "Metode",
        "vc_method_info": "Kies 'n metode vir die Stem Nabootsing proses",
        "vc_segments_label": "Max monsters",
        "vc_segments_info": "Max monsters: Is die aantal oudio monsters wat gegenereer sal word vir die proses, meer is beter maar dit kan geraas byvoeg",
        "vc_dereverb_label": "Dereverb",
        "vc_dereverb_info": "Dereverb: Pas vokale dereverb toe op die oudio monsters.",
        "vc_remove_label": "Verwyder vorige monsters",
        "vc_remove_info": "Verwyder vorige monsters: Verwyder die vorige monsters wat gegenereer is, sodat nuwe monsters geskep moet word.",
        "xtts_title": "Skep 'n TTS gebaseer op 'n oudio",
        "xtts_subtitle": "Laai 'n oudio lêer van maksimum 10 sekondes op met 'n stem. Deur XTTS te gebruik, sal 'n nuwe TTS geskep word met 'n stem soortgelyk aan die verskafde oudio lêer.",
        "xtts_file_label": "Laai 'n kort oudio op met die stem",
        "xtts_name_label": "Naam vir die TTS",
        "xtts_name_info": "Gebruik 'n eenvoudige naam",
        "xtts_dereverb_label": "Dereverb oudio",
        "xtts_dereverb_info": "Dereverb oudio: Pas vokale dereverb toe op die oudio",
        "xtts_button": "Verwerk die oudio en sluit dit in die TTS keurder in",
        "xtts_footer": "Genereer stem xtts outomaties: Jy kan `_XTTS_/AUTOMATIC.wav` gebruik in die TTS keurder om outomaties segmente te genereer vir elke spreker wanneer die vertaling gegenereer word.",
        "extra_setting": "Gevorderde Instellings",
        "acc_max_label": "Max Oudio versnelling",
        "acc_max_info": "Maksimum versnelling vir vertaalde oudio segmente om oorvleueling te vermy. 'n Waarde van 1.0 verteenwoordig geen versnelling nie",
        "acc_rate_label": "Versnelling Reguleringskoers",
        "acc_rate_info": "Versnelling Reguleringskoers: Pas versnelling aan om segmente wat minder spoed benodig te akkommodeer, handhaaf kontinuïteit en oorweeg volgende-begin tydsberekening.",
        "or_label": "Oorvleueling Reduksie",
        "or_info": "Oorvleueling Reduksie: Verseker segmente oorvleuel nie deur begin tye aan te pas gebaseer op vorige eind tye; kan sinkronisasie versteur.",
        "aud_mix_label": "Oudio Meng Metode",
        "aud_mix_info": "Meng oorspronklike en vertaalde oudio lêers om 'n aangepaste, gebalanseerde uitset te skep met twee beskikbare mengmodusse.",
        "vol_ori": "Volume oorspronklike oudio",
        "vol_tra": "Volume vertaalde oudio",
        "voiceless_tk_label": "Stemlose Snit",
        "voiceless_tk_info": "Stemlose Snit: Verwyder die oorspronklike oudio stemme voordat dit met die vertaalde oudio gekombineer word.",
        "sub_type": "Onderskrif tipe",
        "soft_subs_label": "Sagte Onderskrifte",
        "soft_subs_info": "Sagte Onderskrifte: Opsionele onderskrifte wat kykers kan aanskakel of afskakel terwyl hulle die video kyk.",
        "burn_subs_label": "Brand Onderskrifte",
        "burn_subs_info": "Brand Onderskrifte: Inbed onderskrifte in die video, maak hulle 'n permanente deel van die visuele inhoud.",
        "whisper_title": "Konfigureer transkripsie.",
        "lnum_label": "Literaliseer Nommer",
        "lnum_info": "Literaliseer Nommer: Vervang numeriese verteenwoordigings met hul geskrewe ekwivalente in die transkripsie.",
        "scle_label": "Klank Opruiming",
        "scle_info": "Klank Opruiming: Versterk vokale, verwyder agtergrondgeraas voor transkripsie vir uiterste tydstempel presisie. Hierdie operasie kan tyd neem, veral met lang oudio lêers.",
        "sd_limit_label": "Segmentduur Beperking",
        "sd_limit_info": "Spesifiseer die maksimum duur (in sekondes) vir elke segment. Die oudio sal verwerk word met VAD, wat die duur vir elke segment stuk beperk.",
        "asr_model_info": "Dit omskakel gesproke taal na teks met die 'Whisper model' by verstek. Gebruik 'n aangepaste model, byvoorbeeld, deur die repository naam 'BELLE-2/Belle-whisper-large-v3-zh' in die dropdown in te voer om 'n Chinees taal fyn-afgestelde model te gebruik. Vind fyn-afgestelde modelle op Hugging Face.",
        "ctype_label": "Reken tipe",
        "ctype_info": "Kies kleiner tipes soos int8 of float16 kan prestasie verbeter deur geheuegebruik te verminder en berekeningstempo te verhoog, maar kan presisie opoffer in vergelyking met groter datatipes soos float32.",
        "batchz_label": "Batch grootte",
        "batchz_info": "Verkleining van die batch grootte bespaar geheue as jou GPU minder VRAM het en help om Uit-van-Geheue probleme te bestuur.",
        "tsscale_label": "Teks Segmentasie Skale",
        "tsscale_info": "Verdeel teks in segmente deur sinne, woorde, of karakters. Woord en karakter segmentasie bied fyner granulariteit, nuttig vir onderskrifte; deaktiveer vertaling behou oorspronklike struktuur.",
        "srt_file_label": "Laai 'n SRT onderskriflêer op (sal gebruik word in plaas van die transkripsie van Whisper)",
        "divide_text_label": "Her-verdeel teks segmente deur:",
        "divide_text_info": "(Eksperimenteel) Voer 'n skeier in om bestaande teks segmente in die brontaal te verdeel. Die hulpmiddel sal voorkomste identifiseer en nuwe segmente dienooreenkomstig skep. Spesifiseer verskeie skeiers met behulp van |, bv.: !|?|...|。",
        "diarization_label": "Diarisering model",
        "tr_process_label": "Vertaal proses",
        "out_type_label": "Uitvoer tipe",
        "out_name_label": "Lêer naam",
        "out_name_info": "Die naam van die uitvoer lêer",
        "task_sound_label": "Taak Status Klank",
        "task_sound_info": "Taak Status Klank: Speel 'n klank waarskuwing wat taak voltooiing of foute tydens uitvoering aandui.",
        "cache_label": "Herstel Vordering",
        "cache_info": "Herstel Vordering: Gaan voort met die proses vanaf die laaste kontrolepunt.",
        "preview_info": "Voorskou sny die video tot slegs 10 sekondes vir toetsdoeleindes. Skakel dit asseblief af om die volle video duur te kry.",
        "edit_sub_label": "Wysig gegenereerde onderskrifte",
        "edit_sub_info": "Wysig gegenereerde onderskrifte: Laat jou toe om die vertaling in 2 stappe uit te voer. Eerstens met die 'KRY ONDERSKRIFTE EN WYSIG' knoppie, kry jy die onderskrifte om dit te wysig, en dan met die 'VERTAAL' knoppie, kan jy die video genereer.",
        "button_subs": "KRY ONDERSKRIFTE EN WYSIG",
        "editor_sub_label": "Gegenereerde onderskrifte",
        "editor_sub_info": "Voel vry om die teks in die gegenereerde onderskrifte hier te wysig. Jy kan veranderinge aan die koppelvlak opsies maak voordat jy die 'VERTAAL' knoppie druk, behalwe vir 'Bron taal', 'Vertaal klank na', en 'Max sprekers', om foute te vermy. Sodra jy klaar is, klik die 'VERTAAL' knoppie.",
        "editor_sub_ph": "Druk eers 'KRY ONDERSKRIFTE EN WYSIG' om die onderskrifte te kry",
        "button_translate": "VERTAAL",
        "output_result_label": "LAAI VERTAALDE VIDEO AF",
        "sub_ori": "Onderskrifte",
        "sub_tra": "Vertaalde onderskrifte",
        "ht_token_info": "Een belangrike stap is om die lisensie-ooreenkoms te aanvaar vir die gebruik van Pyannote. Jy moet 'n rekening hê op Hugging Face en die lisensie aanvaar om die modelle te gebruik: https://huggingface.co/pyannote/speaker-diarization en https://huggingface.co/pyannote/segmentation. Kry jou SLEUTEL TOKEN hier: https://hf.co/settings/tokens",
        "ht_token_ph": "Token gaan hier...",
        "tab_docs": "Dokument vertaling",
        "docs_input_label": "Kies Dokument Bron",
        "docs_input_info": "Dit kan 'n PDF, DOCX, TXT, of teks wees",
        "docs_source_info": "Dit is die oorspronklike taal van die teks",
        "chunk_size_label": "Max aantal karakters wat die TTS per segment sal verwerk",
        "chunk_size_info": "'n Waarde van 0 ken 'n dinamiese en meer versoenbare waarde toe vir die TTS.",
        "docs_button": "Begin Taal Omskakelingsbrug",
        "cv_url_info": "Laai outomaties die R.V.C. modelle af van die URL. Jy kan skakels van HuggingFace of Drive gebruik, en jy kan verskeie skakels insluit, elkeen geskei deur 'n komma. Voorbeeld: https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.pth, https://huggingface.co/sail-rvc/yoimiya-jp/blob/main/model.index",
        "replace_title": "Vervang stem: TTS na R.V.C.",
        "sec1_title": "### 1. Om die gebruik te aktiveer, merk dit as aktief.",
        "enable_replace": "Merk dit om die gebruik van die modelle te aktiveer.",
        "sec2_title": "### 2. Kies 'n stem wat toegepas sal word op elke TTS van elke ooreenstemmende spreker en pas die konfigurasies toe.",
        "sec2_subtitle": "Afhangende van hoeveel <TTS Spreker> jy sal gebruik, benodig elkeen sy onderskeie model. Daar is ook 'n hulp een indien 'n spreker nie korrek opgespoor word nie.",
        "cv_tts1": "Kies die stem om toe te pas vir Spreker 1.",
        "cv_tts2": "Kies die stem om toe te pas vir Spreker 2.",
        "cv_tts3": "Kies die stem om toe te pas vir Spreker 3.",
        "cv_tts4": "Kies die stem om toe te pas vir Spreker 4.",
        "cv_tts5": "Kies die stem om toe te pas vir Spreker 5.",
        "cv_tts6": "Kies die stem om toe te pas vir Spreker 6.",
        "cv_tts7": "Kies die stem om toe te pas vir Spreker 7.",
        "cv_tts8": "Kies die stem om toe te pas vir Spreker 8.",
        "cv_tts9": "Kies die stem om toe te pas vir Spreker 9.",
        "cv_tts10": "Kies die stem om toe te pas vir Spreker 10.",
        "cv_tts11": "Kies die stem om toe te pas vir Spreker 11.",
        "cv_tts12": "Kies die stem om toe te pas vir Spreker 12.",
        "cv_aux": "- Stem om toe te pas in geval 'n Spreker nie suksesvol opgespoor word nie.",
        "cv_button_apply": "PAS KONFIGURASIE TOE",
        "tab_help": "Hulp",
    },
}
