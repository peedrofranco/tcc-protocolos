import socket
import ssl

hostname = 'www.google.com.br'
context = ssl.create_default_context()
teste = ssl.wrap_socket(context)
print(teste)

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.__doc__)
        # print(f"Type: {str(ssock.type)} "
        #       f"\nFamily: {str(ssock.family)} "
        #       f"\nProtocol: {str(ssock.proto)} "
        #       f"\nTeste: {str(ssock)}")