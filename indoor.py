def whisper():
    name = input("What's yout name? ").lower().strip()
    hello(name)

def hello(user_name):
    print(f"Hello, {user_name}")

whisper()