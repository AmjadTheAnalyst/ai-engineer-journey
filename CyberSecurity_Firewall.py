# ==============================================================================
# 🏢 PROBLEM: Automated Cyber-Security Firewall (Hard Level)
# ==============================================================================
# You are programming the conditional logic for a network security firewall.
# The firewall evaluates incoming web requests and decides whether to 
# "Allow", "Block", or flag the request for "MFA" (Multi-Factor Authentication).
#
# 📥 Inputs to create:
# 1. ip_location (str): The country origin of the request (e.g., "US", "DE", "CN")
# 2. login_attempts (int): Number of failed login attempts in the last 10 minutes
# 3. request_hour (int): The hour of the request in 24-hour format (0 to 23)
# 4. is_trusted_device (str): "yes" or "no" if the device signature is recognized
#
# 📋 Firewall Logic Rules (Priority order matters!):
#
# 1. SANCTIONED LIST (Highest Priority)
#    - If the `ip_location` is "CN" (China), "RU" (Russia), or "KP" (North Korea),
#      the request is instantly **"Block"**. 
#    - EXCEPTION: If the device `is_trusted_device` is "yes" AND the `request_hour`
#      is during regular business hours (8 to 17 inclusive), degrade the penalty 
#      from Block to **"MFA"** instead.
#
# 2. BRUTE FORCE PROTECTION
#    - If `login_attempts` is 3 or 4, the request requires **"MFA"**.
#    - If `login_attempts` is 5 or more, the request is instantly **"Block"**.
#
# 3. ANOMALOUS TIME AND DEVICE DETECTOR
#    - If the request occurs during late-night hours (before 6 AM OR after 22 PM):
#      * If it is a trusted device ("yes"), **"Allow"** it.
#      * If it is NOT a trusted device ("no"), **"MFA"** is required.
#
# 4. DEFAULT BEHAVIOR
#    - Any request that does not trigger the strict security flags above is **"Allow"**.
#
# 🧪 Test Cases to verify your logic:
# - location="RU", attempts=1, hour=12, trusted="no"  -> Expected: "Block" (Sanctioned)
# - location="CN", attempts=1, hour=10, trusted="yes" -> Expected: "MFA"   (Sanctioned Exception)
# - location="US", attempts=5, hour=14, trusted="yes" -> Expected: "Block" (Brute Force)
# - location="DE", attempts=2, hour=23, trusted="no"  -> Expected: "MFA"   (Late night untrusted)
# - location="US", attempts=0, hour=14, trusted="no"  -> Expected: "Allow" (Normal traffic)
# ==============================================================================

# Write your solution below:
ip_location = input("The country origin of the request ")
login_attempts = int(input("Number of failed login attempts in the last 10 minutes "))
request_hour = int(input("The hour of the request in 24-hour format (0 to 23) "))
trusted_device = input("Is the device signature is recognized? ")

# 1. SANCTIONED LIST (Highest Priority)
#    - If the `ip_location` is "CN" (China), "RU" (Russia), or "KP" (North Korea),
#      the request is instantly **"Block"**. 
#    - EXCEPTION: If the device `is_trusted_device` is "yes" AND the `request_hour`
#      is during regular business hours (8 to 17 inclusive), degrade the penalty 
#      from Block to **"MFA"** instead.
if (ip_location in {"CN", "RU", "KP"}):
    if trusted_device == "yes" and request_hour>=8 and request_hour<=17 :
        print("Penalty is degraded from BLOCK to MFA") 
    else:
        print("Highest Priorty: BLOCKED")

# 2. BRUTE FORCE PROTECTION
#    - If `login_attempts` is 3 or 4, the request requires **"MFA"**.
#    - If `login_attempts` is 5 or more, the request is instantly **"Block"**.
elif (login_attempts in (3,4)):
    print("MFA")
elif login_attempts >= 5:
    print("Block")
# 3. ANOMALOUS TIME AND DEVICE DETECTOR
#    - If the request occurs during late-night hours (before 6 AM OR after 22 PM):
#      * If it is a trusted device ("yes"), **"Allow"** it.
#      * If it is NOT a trusted device ("no"), **"MFA"** is required.
elif request_hour >22 or request_hour <6:
    if (trusted_device == "yes"):
        print("Allow")
    elif (trusted_device == "no"):
        print("MFA")
# 4. DEFAULT BEHAVIOR
#    - Any request that does not trigger the strict security flags above is **"Allow"**.
else: 
    print("Allow")