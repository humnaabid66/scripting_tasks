import ssl
import socket
from datetime import datetime

def get_ssl_expiry(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            return expiry_date

def days_until_expiry(expiry_date):
    today = datetime.utcnow()
    remaining = (expiry_date - today).days
    return remaining

# List of domains to check
domains = ["linkedin.com", "google.com"]

for domain in domains:
    try:
        expiry = get_ssl_expiry(domain)
        days_left = days_until_expiry(expiry)
        print(f"{domain} SSL expires in {days_left} days on {expiry}")
        if days_left < 30:
            print(f"⚠️ ALERT: {domain} certificate is expiring soon!")
    except Exception as e:
        print(f"Failed to check {domain}: {e}")

