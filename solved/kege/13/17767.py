from itertools import product
mask = [255, 255, 240, 0]
ip = [228, 172, 236, 0]


def convert_to_bin(ip_parts: list) -> str:
    return " ".join([bin(part)[2:].ljust(8, "0") for part in ip_parts])


mask_binary = convert_to_bin(mask)

print(mask_binary)

nodes_bits = mask_binary.count("0")

network_masked = [ip[i] & mask[i] for i in range(len(mask))]

network_masked_binary = convert_to_bin(network_masked)
network_bits = network_masked_binary.count("1")

print(network_masked_binary)
print(nodes_bits, network_bits)

count = 0
for variant in product("01", repeat=nodes_bits):
    ones = network_bits + variant.count("1")
    if ones % 5 != 0:
        count += 1

print(count)