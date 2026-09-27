def check_pin_safety(pin):
    issues = []
    score = 0

    # Check if input is numeric and has valid length (4 to 8 digits)
    if not pin.isdigit():
        return 0, ["PIN must contain only numbers."]
    
    if len(pin) >= 4:
        score += 1
    else:
        issues.append("Too short: Use at least 4 digits (6+ recommended).")

    if len(pin) >= 6:
        score += 1

    # Check for repeated digits (e.g., "1111")
    if len(set(pin)) == 1:
        issues.append("Extremely weak: All digits are identical.")
        return 1, issues
    else:
        score += 1

    # Check for simple sequential patterns (ascending or descending)
    ascending = "0123456789"
    descending = "9876543210"
    if pin in ascending or pin in descending:
        issues.append("Weak pattern: Sequential numbers are easy to guess.")
    else:
        score += 1

    # Check for common birthday/year patterns (starting with 19 or 20)
    if pin.startswith(("19", "20")) and len(pin) == 4:
        issues.append("Risky pattern: Looks like a birth year.")
    else:
        score += 1

    return max(1, score), issues

def get_verdict(score):
    if score <= 1:
        return "VERY WEAK"
    elif score == 2:
        return "WEAK"
    elif score == 3:
        return "FAIR"
    elif score == 4:
        return "STRONG"
    else:
        return "VERY STRONG"

# Example usage:
if __name__ == "__main__":
    user_pin = input("Enter a PIN to check: ")
    score, issues = check_pin_safety(user_pin)
    print(f"\nScore: {score} / 5")
    print(f"Verdict: {get_verdict(score)}")
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No major vulnerabilities detected!")
