import base64

def main():
    encoded_code = b'cjN2M3JzM19tMw=='  
    encoded_flag = b'SFRGe3IzdjNyNTNfM25nMW4zM3IxbmdfcjBjazV9'  

    secret_code = base64.b64decode(encoded_code).decode()
    flag = base64.b64decode(encoded_flag).decode()

    user_input = input("Enter the secret code: ")

    if user_input == secret_code:
        print(f"Congratulations! The flag is {flag}")
    else:
        print("Wrong code, try again!")

if __name__ == "__main__":
    main()
