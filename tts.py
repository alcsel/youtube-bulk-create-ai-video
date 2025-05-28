from gtts import gTTS
import os
def text_to_speech_and_save():
    try:
        text = input("Please enter text to generate speech: ").strip()
        if not text:
            print("Text cannot be empty. Please enter something.")
            return
        language = input("Enter the language code for the text (e.g., 'en' for English, 'tr' for Turkish): ").strip() or 'tr'
        save_path = input("Enter the directory where the MP3 file will be saved (default: current directory): ").strip() or "./"
        file_name = input("Enter the name of the MP3 file (e.g., 'output'): ").strip() or "output"
        file_path = os.path.join(save_path, f"{file_name}.mp3")
        print("Generating speech...")
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(file_path)
        print(f"Speech successfully generated and saved to: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
text_to_speech_and_save()
