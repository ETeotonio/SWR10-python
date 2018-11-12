from bluepy.btle import Scanner, Peripheral
from scanDelegate import ScanDelegate
import binascii
import time

class accessMethods():
    def scan(self):
        scanner = Scanner().withDelegate(ScanDelegate())
        devices = scanner.clear()
        devices = scanner.start()
        devices = scanner.process(timeout=10)
        devices = scanner.stop()

    def scan_services(self,mac_address):
        p = Peripheral(mac_address)
        services = p.getServices()
        for service in services:
            print(service)

    def get_characteristics(self,mac_address, service_uuid):
        p = Peripheral(mac_address)
        chList = p.getCharacteristics()
        chList = p.getCharacteristics(uuid=service_uuid)
        print("Handle      UUID        Properties")
        print("----------------------------------")
        for ch in chList:
            print("0x" + format(ch.getHandle(), '02x') + "   " + str(ch.uuid) + "    " + ch.propertiesToString())

    def get_data_from_service(self,mac_address, service_uuid, characteristics):
        p = Peripheral(mac_address)
        service_status = p.getServiceByUUID(service_uuid)
        ch = service_status.getCharacteristics(characteristics)[0]
        if ch.supportsRead():
            val = binascii.b2a_hex(ch.read())
            val1 = val.decode('utf-8')
            print (str(ch),binascii.unhexlify(val1))
            time.sleep(1)