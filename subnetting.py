def subnetting(ip, mask, n):
    # Convertir la dirección IP y la máscara de subred a binario
    ip_bin = ''.join([bin(int(x)+256)[3:] for x in ip.split('.')])
    mask_bin = ''.join([bin(int(x)+256)[3:] for x in mask.split('.')])
    
    # Calcular la longitud de la máscara de subred en bits
    mask_len = mask_bin.count('1')
    
    # Calcular el número de hosts por subred
    hosts_per_subnet = 2**(32-mask_len) // n
    
    # Crear la lista de subredes
    subnets = []
    for i in range(n):
        # Calcular la dirección de red y de broadcast de la subred
        subnet_id = ip_bin[:mask_len] + bin(i*hosts_per_subnet)[2:].zfill(32-mask_len)
        broadcast_id = ip_bin[:mask_len] + bin((i+1)*hosts_per_subnet-1)[2:].zfill(32-mask_len)
        
        # Convertir la dirección de red y de broadcast de la subred a decimal
        subnet_id_dec = '.'.join([str(int(subnet_id[i:i+8], 2)) for i in range(0, 32, 8)])
        broadcast_id_dec = '.'.join([str(int(broadcast_id[i:i+8], 2)) for i in range(0, 32, 8)])
        
        # Añadir la subred a la lista
        subnets.append((subnet_id_dec, broadcast_id_dec))
    
    return subnets


subnets = subnetting('192.168.1.0', '255.255.255.0', 4)
print(subnets)
