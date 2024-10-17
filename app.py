import os


if __name__ == '__main__':
  print("Welcome to RoboSpeaker! created by Maheen Arif")
  while True:
    x = input("Enter what you want me to speak (or type 'exit' to quit): ")
    if x.lower() == 'exit':
      break
    # Use a platform-specific command for text-to-speech
    if os.name == 'posix':  # macOS and Linux
        command = f"say '{x}'"
    elif os.name == 'nt':  # Windows
        command = f"powershell -Command Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
    else:
        print("Unsupported operating system.")
        continue

    os.system(command)