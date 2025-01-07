#Create a program that calculates E=MC^2 round(kg*(300000000 ** 2))
def main(): 
    mass = float(input())
    convert(mass)

def convert(kg):
    converted_kg = round(kg * (300000000 ** 2))
    print(f"{converted_kg}:.0f")

main()