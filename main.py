from operations import add ,subtract,multiply,divide,modulus,power
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
                print(f'result :{num1}+{num2} = {add(num1,num2)}')
            elif choice == '2' :
                print(f'result :{num1}-{num2} = {subtract(num1,num2)}')
            elif choice == '3' :
                print(f'result :{num1}*{num2} = {multiply(num1,num2)}')
                
            elif choice =='4' :
                print(f'result :{num1}/{num2} = {divide(num1,num2)}')
                
            elif choice == '5' :
                print(f'result :{num1}^{num2} = {power(num1,num2)}')
            elif choice == '6' : 
                print(f'result :{num1}%{num2} = {modulus(num1,num2)}')
                
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
            
if __name__ == "__main__":
    main()