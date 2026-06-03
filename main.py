import os
import speech_recognition as sr
import keyboard
import threading

keep_running = True

recognizer = sr.Recognizer()

def menu():
    print(" = = = = = = = = = = = = QUICK NOTES (HOMEMADE)  = = = =  = = = = = = = = = ")
    print(" - - - because notes app doesn't catch you when you speak - - -")
    print("\n      ~ Version 2.0 ~           \n")
    print()

def check_for_space():
    global keep_running
    keyboard.wait('space')
    keep_running = False
    print("\n[SYSTEM]: SPACEBAR Detected. Saving and Closing note...")
def create_note():
    filename = input("NOTE NAME: ")
    filepath = os.path.join("QuickNotes", filename)
    with open(filepath, "w"):
        pass
    return filepath

def write_to_note(filepath, text):
    with open(filepath, "a") as file:
        file.write(text + "\n")
        file.flush()
        os.fsync(file.fileno())


if __name__ == "__main__":

    if not os.path.exists("QuickNotes"):
        os.mkdir("QuickNotes")


    menu()
    target_file = create_note()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)

    threading.Thread(target=check_for_space, daemon=True).start()
    print("[SYSTEM]: Microphone enabled.\n[NOTE]: Press SPACEBAR to save and exit.")

    while keep_running:

        if keyboard.is_pressed('space'):
            print("[SYSTEM]: SPACEBAR was pressed. Closing and saving contents...")
            break

        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=10)
                text = r.recognize_google(audio)
                print(f"[USER ENTERED]: {text}")
                write_to_note(target_file, text)
        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            continue
        except Exception as e:
            print("Error; {0}".format(e))

print("[QUICKNOTES]: Thank You for using my homemade program :)")