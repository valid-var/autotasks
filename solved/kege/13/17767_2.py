import ipaddress

# Так как слева мы указываем не адрес сети, а адрес узла 228.172.236.0 (при адресе сети 228.172.224.0)
# чтобы метод это понял, и вырезал адрес сети, нужно подать strict=False
ip_range = ipaddress.ip_network("106.184.0.0/255.248.0.0", False)

count = 0
for ip in ip_range:
    ones_count = bin(int(ip))[2:].count("1")
    if ones_count % 2 != 0:
        count += 1

print(count)

