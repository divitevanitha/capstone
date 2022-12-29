import os, ipaddress

os.system('cls') #os,system will clear the console at the start of the execution
while True:
    ip = input("enter Ip address:")
    try:
        print(ipaddress.ip_address(ip))
        print("ip valid")
    except:
        print('-' *50)
        print('ip is not valid')
    finally:
        if ip == 'mango':
            print('script Finished')
            break