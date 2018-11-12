from accessMethods import accessMethods

def menu():
    i=1
    accessMethod = accessMethods()
    while (i!=0):
        print ("Digite a opcao desejada:\r\n")
        print ("1) Scanear dispositivos BT LE\r\n"
               "2)Scanear servicos de dispositivo BT LE\r\n"
               "3)Capturar dados de dispositivo BT LE\r\n"
               "4)Outro digito sair")
        opt = input()
        if opt == '1':
            accessMethod.scan()
        elif opt == '2':
            mac_address=input("Digite o MAC do dispositivo BT LE\r\n")
            if(mac_address):
                accessMethod.scan_services(mac_address)
            else:
                print ("Digite o MAC corretamente")
        elif opt == '3':
            mac_address=input("Digite o MAC e o serviço a ser buscado")
            service = input("Digite o serviço BTLE a ser consultado")
            characteristics=input("Digite a caracteristica")
            if (mac_address and service):
                accessMethod.get_data_from_service(mac_address,service,characteristics)
        elif opt=='4':
            mac_address=input("Digite o MAC a ser buscado\r\n")
            service = input("Digite o serviço BTLE a ser consultado")
            accessMethod.get_characteristics(mac_address,service)
        else:
            i=0

menu()