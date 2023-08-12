
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started....")
    elif command == "stop":
      print ("Car stopped.")
    elif command == "help":
       print("""
      start - to start the car
      stop - to stop
      quit - to quit
             """)
    elif command == "quit":
       break
    else: 
       print( "sorry, i don't understand that")






