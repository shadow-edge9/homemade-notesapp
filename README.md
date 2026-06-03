# QuickNotes

A lightweight, terminal-based voice-to-text note-taking application.

## The Problem
Standard notes applications often struggle to keep up with the speed of thought. This tool is designed to capture dictated thoughts directly into local text files, bypassing traditional GUI overhead.

## Prerequisites
This project requires Python 3.x and the following dependencies:

* `SpeechRecognition`
* `keyboard`
* `PyAudio` (Required for microphone input)

Install the dependencies via pip:
```bash
pip install SpeechRecognition keyboard PyAudio
```
Cloone the repository
```bash
git clone [https://github.com/shadow-edge9/homemade-notesapp]
```
Run the script:
```bash
python main.py
```
NOTE: MacOS users, it's python3. You may require admin priviledges to access the keyboard. If the spacebar doesn't work try this:

```bash
sudo python main.py
```
## Running The Script

* Enter the desired name for your note when prompted.
* Speak clearly. The program will automatically append your input to the file in the QuickNotes/ directory.
* Press the SPACEBAR at any time to save your progress and it will safely save and close your note.
  
## Technical Notes
This is an experimental build.
Files are stored locally in the QuickNotes/ folder created at runtime.
The script utilizes threading to monitor for input interrupts while actively listening to the microphone.
