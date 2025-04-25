class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User(username={self.username}, password={'*' * len(self.password)})"


class Proxy:
    def __init__(self, ip_address, port, protocol, is_active=True,
                 last_checked=None, response_time=None, country=None,
                 anonymity_level=None):
        self.ip_address = ip_address
        self.port = port
        self.protocol = protocol
        self.is_active = is_active
        self.last_checked = last_checked
        self.response_time = response_time
        self.country = country
        self.anonymity_level = anonymity_level

    def __repr__(self):
        return f"Proxy({self.ip_address}:{self.port}, {self.protocol})"
