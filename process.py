import sys

def main():
    number = sys.argv[1]
    text = sys.argv[2]
    
    result_text = f"You entered the number {number} and the word '{text}'. "
    result_text += f"Reversed word: {text[::-1]}"
    
    print(result_text)
    
if __name__ == "__main__":
    main()

/* style.css */
.container {
    width: 50%;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    text-align: center;
    background: #f9f9f9;
}
input {
    display: block;
    margin: 10px auto;
    padding: 10px;
}
input[type="submit"] {
    background: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
}