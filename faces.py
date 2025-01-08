def main(): 
    reply = input("Type a message and add either a frowny face or a smiley face: ").replace(":)", "😊").replace(":(", "☹️")
    faces(reply)

def faces(response):
    print(f"{response}")

main()
