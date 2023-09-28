import dns.resolver
# url = input("Please input your url ")
# host = url

host = "hackthissite.org"
record_types = {
    1: 'A',
    2: 'MX',
    3: 'AAAA',
    4: 'SOA',
    5: 'NS'
}

print("Please select any of the below options ")
for choice, record_type in record_types.items():
    print(f"{choice}: {record_type}")

choice = int(input('Input your choice '))

if choice in record_types:
    selected_record_type = record_types[choice]
    print(f"The below are the {selected_record_type} records for {host}")
    
    ip = dns.resolver.resolve(host, selected_record_type)
    for i in ip:
        print(i)

elif choice == 123:
    print("Below are all the available DNS records")
    
    for record_type in record_types.values():
        print(f"{record_type} records:")
        ip = dns.resolver.resolve(host, record_type)
        for i in ip:
            print(i)

else:
    print("Invalid choice")