command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started.")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
>start- to start the race
>stop- to stop the car
>quit- to quit the race
              """)
    elif command == "quit":
        break



