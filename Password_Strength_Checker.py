import re

def password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 chars).")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$ etc).")

    # Common passwords check (basic)
    common_passwords = ["password", "123456", "qwerty", "letmein", "admin"]
    if password.lower() in common_passwords:
        feedback.append("Avoid common passwords.")
        score = min(score, 2)

    # Final evaluation
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions to improve:")
    for f in feedback:
        print(f" - {f}")