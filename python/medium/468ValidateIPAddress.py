class Solution:
    # Sub functions for each type make this problem easier. Check each using the conditions given
    def validIPAddress(self, IP: str) -> str:
        def isIPv4():
            if not IP.count(".") == 3:
                return False
            try:
                block = IP.split(".")
                for s in block:
                    if not (str(int(s)) == s and 0 <= int(s) <= 255):
                        return False
                return True
            except:
                return False

        def isIPv6():
            if not IP.count(":") == 7:
                return False
            try:
                block = IP.split(":")
                for s in block:
                    if len(s) > 4:
                        return False
                    if not (int(s, 16) >= 0 and s[0] != '-'):
                        return False
                return True
            except:
                return False

        if isIPv4():
            return "IPv4"
        if isIPv6():
            return "IPv6"
        return "Neither"
