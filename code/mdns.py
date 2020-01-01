"""
    This module is dedicated to MDNS
    class：
        mDNS_BrowserThread(Used to continuously check mDNS)
"""

import time

from PySide2.QtCore import QThread, Signal
from zeroconf import ServiceBrowser, ServiceListener, Zeroconf


class MDNSBrowserThread(QThread):
    """
    This is a QT thread that gets the MDNS information and sends it to the UI
    thread via the get_sub_new signal.
    """
    get_sub_new = Signal(str)

    def __init__(self, parent=None, **func_task) -> None:
        super().__init__(parent)
        self.ID_list = []
        self.zeroconf = Zeroconf()
        self.listener = MyListener()

    def __def__(self) -> None:
        self.wait()

    def run(self) -> None:
        """
        The data of the searched device is refreshed every second,
         and each update is converted into a string and sent to the interface(name ip port data)
        """
        print('mDNS_BrowserThread start !')
        ServiceBrowser(
            self.zeroconf,
            '_ewelink._tcp.local.',
            listener=self.listener
        )
        while True:
            if self.listener.all_sub_num > 0:
                # Copy from the listener's dictionary to the current file
                dict = self.listener.all_info_dict.copy()
                for x in dict.keys():
                    # print('new updata ID：',x[8:18])
                    info = dict[x]
                    info = self.zeroconf.get_service_info(info.type, x)
                    print('updata', x, 'info', 'len', len(str(info)), info)
                    if info is not None:
                        data = info.properties
                        cur_str = (x[8:18] + '\n' +
                                   parse_address(info.address) + '\n' +
                                   str(info.port) + '\n' +
                                   str(data))
                        self.get_sub_new.emit(cur_str)
            # Send deleted devices
            if len(self.listener.all_del_sub) > 0:
                for x in self.listener.all_del_sub:
                    cur_str = x[8:18] + '\nDEL'
                    self.get_sub_new.emit(cur_str)
            time.sleep(0.5)


class MyListener(ServiceListener):
    """
    This class is used for the mDNS browsing discovery device, including
    calling the remove_service and add_service properties to ServiceBrowser,
    and also contains broadcasts for querying and updating existing devices.
        Dictionary
        all_info_dict:Qualified device information in the current network
        [keys:info.name，val:info]
    """

    def __init__(self) -> None:
        self.all_del_sub = []
        self.all_info_dict = {}
        self.all_sub_num = 0
        self.new_sub = False

    def remove_service(self, zeroconf: Zeroconf, type: str, name: str) -> None:
        """
        This function is called for ServiceBrowser.
        This function is triggered when ServiceBrowser discovers that some
        device has logged out
        """
        print('inter remove_service()')
        if name not in self.all_info_dict:
            return
        self.all_sub_num -= 1
        del self.all_info_dict[name]
        self.all_del_sub.append(name)
        print('self.all_info_dict[name]', self.all_info_dict)
        print(f'Service {name} removed')

    def add_service(self, zeroconf: Zeroconf, type: str, name: str) -> None:
        """
        This function is called for ServiceBrowser.This function is triggered
        when ServiceBrowser finds a new device
        When a subdevice is found, the device information is stored into the
        all_info_dict
        """
        self.new_sub = True
        print('inter add_service()')
        self.all_sub_num += 1
        info = zeroconf.get_service_info(type, name)

        if info.properties[b'type'] != b'diy_plug':
            return

        self.all_info_dict[name] = info
        if name in self.all_del_sub:
            self.all_del_sub.remove(name)
            print(f'Service {name} added, service info: {info}')

    def flash_all_sub_info(self) -> None:
        """
        Update all found subdevice information
        """
        info_list = list(self.all_info_dict.keys())
        for x in info_list:
            current_info = self.all_info_dict[x]
            name = current_info['name']
            type = current_info['type']
            info = self.zeroconf.get_service_info(type=type, name=name)
            current_info['info'] = info
            self.all_info_dict[x] = current_info['info']


def main() -> None:
    zeroconf = Zeroconf()
    listener = MyListener()
    ServiceBrowser(zeroconf, '_ewelink._tcp.local.', listener=listener)

    while True:
        if listener.all_sub_num > 0:
            all_info_dict = listener.all_info_dict.copy()
            for x in all_info_dict.keys():
                info = all_info_dict[x]
                info = zeroconf.get_service_info(info.type, x)
                if info is not None:
                    data = info.properties
                    cur_str = (x[8:18] + '  ' +
                               parse_address(info.addresses[0]) + '  ' +
                               str(info.port) + '  ' +
                               str(data))
                    print(cur_str)
        if len(listener.all_del_sub) > 0:
            for x in listener.all_del_sub:
                cur_str = x[8:18] + '\nDEL'
                print(cur_str)
        time.sleep(0.5)


def parse_address(address: bytes) -> str:
    add_list = []
    for i in range(4):
        add_list.append(int(address.hex()[(i * 2):(i + 1) * 2], 16))
    return '.'.join(map(str, add_list))


if __name__ == '__main__':
    main()
