import ipaddress

# Function to find class and subnet mask
def get_class_and_mask(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 127:
        return "Class A", "255.0.0.0"
    elif 128 <= first_octet <= 191:
        return "Class B", "255.255.0.0"
    elif 192 <= first_octet <= 223:
        return "Class C", "255.255.255.0"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicasting)", "255.0.0.0"
    elif 240 <= first_octet <= 254:
        return "Class E (Experimental)", "255.0.0.0"
    else:
        return "Invalid", None

# Function to calculate network and broadcast addresses
def calculate_addresses(ip, mask):
    ip_parts = list(map(int, ip.split('.')))
    mask_parts = list(map(int, mask.split('.')))
    
    network_addr = []
    broadcast_addr = []
    
    for i in range(4):
        network_part = ip_parts[i] & mask_parts[i]
        broadcast_part = network_part | (255 - mask_parts[i])
        network_addr.append(str(network_part))
        broadcast_addr.append(str(broadcast_part))
    
    return '.'.join(network_addr), '.'.join(broadcast_addr)

# Main program
if __name__ == "__main__":
    ip = input("ENTER IP: ").strip()
    ip_class, mask = get_class_and_mask(ip)
    
    if mask is None:
        print("Invalid IP address.")
    else:
        print(f"{ip_class} IP Address")
        print(f"SUBNET MASK:\n{mask}")
        
        network, last = calculate_addresses(ip, mask)
        print(f"First IP of block: {network}")
        print(f"Last IP of block: {last}")
