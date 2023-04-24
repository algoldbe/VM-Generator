import asyncio
import edge_tts
import os
import sys
import msvcrt

WELCOME_MESSAGE = "Welcome to the Cisco Voicemail Generator App"
GOODBYE_MESSAGE = "Your new voicemail audio file has been generated successfully, please look for it in the same folder as this script and upload it to your phone profile. Press any key to exit."
TEXT_TEMPLATE = "Hello, you have reached {name} at Cisco Tac, my working hours are from 10 am to 6 pm Monday through Friday, Central Time, so I'm not available right now, Please leave your name and service request number, I'll review the information and contact you as soon as possible; Thank you!"

async def _main() -> None:
    name = input("Please enter your name: ")
    voice_gender = input("Select voice gender (1 for male, 2 for female): ")
    voice_id = "en-US-GuyNeural" if voice_gender == "1" else "en-US-JennyNeural"
    text = TEXT_TEMPLATE.format(name=name)
    output_file = "vm.wav"

    communicate = edge_tts.Communicate(text, voice_id)
    await communicate.save(output_file)

    print(GOODBYE_MESSAGE)
    msvcrt.getch()

if __name__ == "__main__":
    print(WELCOME_MESSAGE)
    asyncio.run(_main())
