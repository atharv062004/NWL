import socket
def main():
    print('Select choice ')
    print('')
    c=int(input('1) Host Name 2) Host IP : ') )

    if c==1:
        host=input('\n Enter Host name : ')
        try:
            address=socket.gethostbyname(host)
            print('host name :',host)
            print('IP addr :',address)
        except socket.gaierror:
            print('Not found')
            
    elif c==2:
        host=input('\n Enter IP : ')
        try:
            address=socket.gethostbyaddr(host)
            print('host name :',host)
            print('IP addr :',address)
        except socket.herror:
            print('Not found')
            
    else:
        print('Invalid')


if __name__=='__main__':
 main()