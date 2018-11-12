import sys
import binascii
import struct
import time
from bluepy.btle import Scanner, DefaultDelegate,Peripheral,UUID

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print ("Discovered device "+dev.addr+" with RSSI="+str(dev.rssi))
        elif isNewData:
            print ("Received new data from", dev.addr)

def scan():
    scanner = Scanner().withDelegate(ScanDelegate())
    devices = scanner.clear()
    devices=scanner.start()
    devices=scanner.process(timeout=10)
    devices=scanner.stop()

def scan_services(mac_address):
    p = Peripheral(mac_address)
    services=p.getServices()
    for service in services:
        print (service)

def get_characteristics(mac_address):
    p = Peripheral(mac_address)
    chList = p.getCharacteristics()
    print ("Handle      UUID        Properties")
    print ("----------------------------------")
    for ch in chList:
        print("0x"+format(ch.getHandle(),'02x')+"   "+str(ch.uuid)+"    "+ch.propertiesToString())
def get_data_from_service(mac_address,service_uuid, characteristics):
    p = Peripheral(mac_address)
    service_status = p.getServiceByUUID(service_uuid)
    ch = service_status.getCharacteristics(characteristics)[0]
    if ch.supportsRead():
        val = binascii.b2a_hex(ch.read())
        print (int("0x"+val,0))
        time.sleep(1)
    print (str(ch))

def menu():
    i=1
    while (i!=0):
        print ("Digite a opcao desejada:\r\n")
        print ("1) Scanear dispositivos BT LE\r\n"
               "2)Scanear servicos de dispositivo BT LE\r\n"
               "3)Capturar dados de dispositivo BT LE\r\n"
               "4)Outro digito sair")
        opt = input()
        if opt == '1':
            scan()
        elif opt == '2':
            print ("Digite o MAC do dispositivo BT LE\r\n")
            mac_address=input()
            if(mac_address):
                scan_services(mac_address)
            else:
                print ("Digite o MAC corretamente")
        elif opt == '3':
            print ("Digite o MAC e o serviço a ser buscado")
            mac_address=input()
            print ("Digite o serviço BTLE a ser consultado")
            service = input()
            if (mac_address and service):
                get_data_from_service(mac_address,service)
        elif opt=='4':
            print ("Digite o MAC a ser buscado")
            mac_address=input("Digite o MAC a ser buscado\r\n")
            get_characteristics(mac_address)
        else:
            i=0

menu()