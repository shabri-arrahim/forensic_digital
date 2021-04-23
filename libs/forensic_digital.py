import adbutils
from ppadb.client import Client as AdbClient


class AdbSetup:
    device = None
    def __init__(self):
        self.client = adbutils.AdbClient(host="127.0.0.1", port=5037)
        self.device = self.client.device()
        print(self.device)
    
    # get client    
    def get_client(self):
        return self.client
    
    # get device
    def get_device(self):
        return self.device
    
    # get device informations
    def get_device_information(self):
        device_information_column =[
            "Device Info"
        ]
        
        device_label = [
            "Name",
            "Model",
            "Device",
            "Version Release",
            "Mother Board",
            "CPU Version",
            "CPU Brand",
            "Manufacture",
            "IP Address",
        ]
        
        device_information_value = [
            f"Name: {self.device.getprop('ro.product.name')}",
            f"Model: {self.device.getprop('ro.product.model')}",
            f"Device: {self.device.getprop('ro.product.device')}",
            f"Version Release: {self.device.getprop('ro.build.version.release')}",
            f"Mother Board: {self.device.getprop('ro.product.board')}",
            f"CPU Version: {self.device.getprop('ro.product.cpu.abi')}",
            f"CPU Brand: {self.device.getprop('ro.product.cpu.abi2')}",
            f"Manufacture: {self.device.getprop('ro.product.manufacturer')}",
            f"IP Address: {self.device.getprop('dhcp.wlan0.ipaddress')}",
        ]
        
        device_information = {
            'column': device_information_column or None,
            'value': device_information_value or None,
            'label': device_label or None,
        }

        return device_information

    # get installed package list
    def get_package_list(self):
        return self.device.shell("pm list packages -f -3").split('\n')

    # get memory info
    def get_memory_info(self):
        return self.device.shell("cat /proc/meminfo")

    # do backup
    def backup(self):
        for app in self.device.shell("pm list packages -f -3"):
            self.device.shell(f"backup -apk -shared -all -f {app}/backup.ab")    
    
    # for app in device1.shell("pm list packages -f -3"):
    #     print(device1.pull(f"$( echo ${app} | sed 's/^package://' | sed 's/base.apk=/base.apk /').apk", "digital.apk"))
    
    # print(device1.shell("run-as com.corp.whatsapp cat /data/data/com.corp.whatsapp/databases/data.db")