from configparser import ConfigParser
from datetime import datetime
from random import randint, seed
from time import sleep

from playsound import playsound
from pyvolume import custom  # type: ignore

# pylint: disable=pointless-string-statement
"""

Seagull Scaring v1.4
By Gabriel Alonso-Holt.

The days of having me run around scaring seagulls manually are over! 
With Seagull Scaring, you can just start the program, 
choose a time to scare seagulls for, 
and relax as the seagulls fly away every 1-5 minutes.

Instructions:

1. Start program ("python main.py" is preferred, it's your choice how to run it, not mine)
2. Type "y" at the prompt and choose a time to scare seagulls for in seconds.
3. Every (minimum wait time - maximum wait time) minutes or seconds, you will hear a seagull squawk.
4. At least 1 seagull should fly away every time the noise is played.
5. When the program finishes, you will see finish time and approximate number of seagulls scared.

"""


def main() -> None:
    """This function contains all of the code in the program.
    This code will only execute if ran directly.

    """

    seed()
    seagulls: int = 0
    FMT: str = "%d.%m.%y %H:%M:%S"

    sounds: list[str] = [
        "seagull",
        "sad seagull",
        "angry seagull",
        "confused seagull",
        "disgust seagull",
        "alarm seagull",
        "Seagull 2",
        "robot seagull",
        "sea gull",
    ]

    # create a parser object
    parser: ConfigParser = ConfigParser()
    parser.read(r"ss_config.ini")

    config: list[str] = parser.sections()

    print("--------------------------------------------")
    print("\tSeagull Scaring v1.4")
    print("\tBy Gabriel Alonso-Holt.")
    print("--------------------------------------------")
    print()

    match parser[config[0]]["use_this_config"]:

        # decide whether or not to use config
        case "yes":

            print("Config file found!")
            print("Using settings from ss_config.ini")

            sound_path: str = (
                rf"media\{parser[config[0]]["default_sound"].replace(" ", "_")}.wav"
            )
            timer: int = int(parser[config[0]]["scaring_time"])
            min_time: int = int(parser[config[0]]["min_time"])
            max_time: int = int(parser[config[0]]["max_time"])
            answer: str = parser[config[0]]["autostart"]
            delay: int = int(parser[config[0]]["autostart_delay"])
            volume: int = int(parser[config[0]]["default_volume"])
            print("[*] Setting volume...")
            custom(percent=volume)
            print(f"Waiting {delay:,} seconds...")

            sleep(delay)

        # manually input settings
        case _:

            answer: str = input(
                "Are you sure you want to begin seagull scaring? (y/n) "
            ).lower()
            timer: int = int(
                input("How long do you want to run the program for? (in seconds) ")
            )
            min_time: int = int(input("Minimum time to wait: (in seconds) "))
            max_time: int = int(input("Maximum time to wait: (in seconds) "))
            volume: int = int(input("Volume (1-100): "))
            custom(percent=volume)
            print()

            print("You must now choose a sound.")
            print("The options are: ")
            print("1. seagull")
            print("2. sad seagull")
            print("3. angry seagull")
            print("4. confused seagull")
            print("5. disgust seagull")
            print("6. alarm seagull")
            print("7. Seagull 2")
            print("8. robot seagull")
            print("9. sea gull")
            print("Input your choice.")
            sound: int = int(input("Sound (1-9): "))
            print()

            # Replace sound string
            sound_path: str = rf"media\{sounds[sound - 1].replace(" ", "_")}.wav"

    if answer in ("y", "yes"):

        # Scare seagulls in a loop until user defined timer expires
        while timer > 0:

            pause: int = randint(a=min_time, b=max_time)
            seagulls += 1
            playsound(sound_path)
            print(f"A seagull was scared on {datetime.now():{FMT}}")
            print(f"Approximately {seagulls:,} seagull(s) were scared.")
            timer -= pause
            sleep(pause)

        print(f"{seagulls:,} seagulls (approx.) were scared.")
        print(f"The time is {datetime.now():{FMT}}.")

        if parser[config[0]]["ask_log_file"] == "no":

            # Save log file
            with open(file=r"ss_log.txt", mode="a", encoding="utf-8") as file:
                file.write(
                    f"Approximately {seagulls:,} seagull(s) were scared on {datetime.now():{FMT}}"
                )
                print("File saved to ss_log.txt")

        else:

            log_file: str = input(
                "Do you want to save results to a log file? (yes/no) "
            ).lower()

            match log_file:

                case "yes":
                    with open(file=r"ss_log.txt", mode="a", encoding="utf-8") as file:
                        file.write(
                            f"Approximately {seagulls:,} seagull(s) were scared on {datetime.now():{FMT}}"
                        )
                        print("File saved to ss_log.txt")

                case "no":
                    print("No log file saved.")

                case _:
                    print("Invalid choice.")

        # input() for pause
        input("Press any key to quit... ")

    elif answer == "n":
        print("No seagull scaring today.")

    else:
        print("You must type 'y' or 'n'!")


if __name__ == "__main__":
    main()
