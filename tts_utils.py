from gtts import gTTS
from pydub import AudioSegment
from pydub.utils import which
import os

# Automatically find ffmpeg and ffprobe installed on the system
AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

# Extra precaution: Add to environment PATH at runtime
# os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

def text_to_speech(text, file_name, lang_code="hi"):
    tts = gTTS(text, lang=lang_code, slow=False)
    tts.save(file_name)
    return os.path.abspath(file_name)

def increase_speed(input_file, speed, output_file):
    try:
        input_file = os.path.abspath(input_file)
        output_file = os.path.abspath(output_file)

        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        audio = AudioSegment.from_file(input_file)
        faster_audio = audio.speedup(playback_speed=speed)
        faster_audio.export(output_file, format="mp3")
        return output_file
    except Exception as e:
        print(f"🔴 Error in increase_speed: {e}")
        raise
