def prevent_attack(is_attack):
    if is_attack:
        print("🚨 ALERT: DDoS Attack Detected!")
        print("⚙ Taking Preventive Actions:")
        print("- Blocking suspicious IPs")
        print("- Limiting traffic")
        print("- Activating firewall rules\n")
    else:
        print("✅ Traffic is normal\n")
