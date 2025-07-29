
def user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid input. Please enter a number.')
            
def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Exit")
    while True:
        try :
            choice = input("Enter operation (1/2/3/4/5/6/7):")
            
            if choice == '7' :
                print('Goodbye')
                break
            
            if choice not in ('1','2','3','4','5','6','7'):
                print('Invalid choice. Please try again.')
                continue
            
            num1 = user_input('enter number 1 : ')
            num2 = user_input('enter number 2 : ')
            
            if choice == '1':
                pass
            elif choice == '2' :
                pass
            elif choice == '3' :
                pass
            elif choice =='4' :
                pass
            elif choice == '5' :
                pass
            elif choice == '6' : 
                pass
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
            
if __name__ == "__main__":
    main()