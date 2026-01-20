import re
AUDIT_FILE = "audit.txt"
def normalize(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def validate(text):
    text = normalize(text)
    reasons = []
    email_pattern = r'[a-zA-Z0-9_$\-]+@[a-zA-Z]+.com'
    phone_pattern = r'\b[6-9]\d{9}\b'
    url_pattern = r'https?://\S{11,}'


    if re.search(email_pattern, text):
        reasons.append("Email detected")
    if re.search(phone_pattern, text):
        reasons.append("Phone number detected")
    if re.search(url_pattern, text):
        reasons.append("URL detected")
    result = "VALID" if not reasons else "INVALID"

    with open(AUDIT_FILE, "a") as f:
        f.write(result + " : " + text + "\n")

    return result, reasons

def main():
    text = input("Enter profile description: ")
    result, reasons = validate(text)
    print("\nValidation Result:", result)
    if reasons:
        print("Reasons:")
        for r in reasons:
            print(r)
    else:
        print("No issues found")

if __name__ == "__main__":
    main()
