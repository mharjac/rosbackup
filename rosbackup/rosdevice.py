from netmiko import ConnectHandler


class ROSDevice():
    def __init__(self, host, username, password):
        self.device = {
            'device_type': 'mikrotik_routeros',
            'host':   host,
            'username': username,
            'password': password
        }
        self.dev_connection = ConnectHandler(**self.device)

    def get_config(self):
        return self.dev_connection.send_command_timing('export', delay_factor=4)


