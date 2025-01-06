"""#Ask user for name
name = input("What's your name? ") 
#Remove whitespace
name = name.strip()
#Capitalize user name
name = name.title() 
#Say hello 
print(f"Hello, {name}")""" 

"""#Ask user for name
name = input("What's your name? ").strip().title()
#Say hello 
print(f"Hello, {name}")"""

"""#Ask user for name
name = input("What's your name? ").strip().title()
#Create Function
def hello():
    print(f"Hello, {name}")
#Call Function 
hello()"""

def main(): 
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(user_name):
    print(f"Hello, {user_name}")

main()