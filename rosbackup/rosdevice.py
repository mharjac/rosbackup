from netmiko import ConnectHandler


class ROSDevice():
    def __init__(self, host, username, password, delay):
        self.device = {
            'device_type': 'mikrotik_routeros',
            'host':   host,
            'username': username,
            'password': password,
            'global_delay_factor': delay
        }
        self.dev_connection = ConnectHandler(**self.device)

    def get_config(self):
        return self.dev_connection.send_command_timing('export')


