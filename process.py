import sys

def main():
    if len(sys.argv) < 3:
        print("Error: Missing input arguments.")
        return
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Error: The number must be an integer.")
        return

    text = sys.argv[2]

    result_text = f"You entered the number {number} and the word '{text}'. "
    result_text += f"Reversed word: {text[::-1]}"
    
    print(result_text)
    
if __name__ == "__main__":
    main()