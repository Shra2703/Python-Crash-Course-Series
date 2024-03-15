# Day 5(09-03-2024)
# Robo Speaker

import os
# For mac

# if __name__ == "__main__":
#     print("Welcome to the Robo Speaker 1.1")
#     while(True):
#         x = input("Enter what you want to say")
#         if x == 'q':
#             break   
#         command = f"say {x}"
#         os.system(command)


# For Windows user
import subprocess
 
if __name__ == '__main__':
     print("Welcome to Robospeaker Python Project")
     while True:
         x = input("What you wan me to speak: ")
         if x == "q":
             break
         command = f'echo {x} | PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())"'
         subprocess.run(command, shell=True)