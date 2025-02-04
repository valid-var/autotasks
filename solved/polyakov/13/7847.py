from ipaddress import ip_network

for m in range(7, 32):
    n1 = ip_network(f'132.118.34.161/{m}', False)
    node_count = 0
    for addr in n1:
        ip = f'{addr:n}'
        if ip.count("1") == 13:
            node_count += 1
    if node_count == 35:
        print(f"Кол-во нулей в маске: {32 - m}")
    print(f"Checked {m} {node_count}")

