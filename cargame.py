commands = ""
count = 0 
start = False
stop = False
while True:
    commands = input("> ").lower()
    if commands== 'start':
        if not start:
            print("Car started")
            start = True
            stop= False
        else:
            print("Car already started")
    elif commands=="stop":
        if start:
            if not stop:
                print("Car stopped")
                stop = True
                start= False
            else:
                print("Car already stopped")
        else:
            print("car not started yet.")
    elif commands =="help":
         print("start - to start the car\nstop - to stop the car\nexit - to exit the game")
    elif commands=="exit":
        break
    else:
        print("invalid command")

