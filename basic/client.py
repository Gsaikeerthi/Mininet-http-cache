import socket

serverIP = "10.0.1.2"

dst_ip = str(input("Enter dstIP: "))
s = socket.socket()

print(dst_ip)

port = 12346

s.connect((dst_ip, port))
def send_request(request):
    s.send(request.encode())
    response = s.recv(1024).decode()
    print(response)  
while True:
    request_type = input("Enter request type('get','put','delete' & 'exit' to exit): ").upper()
    
    if request_type == 'EXIT':
        send_request(request_type.lower())
        break
    
    key = input("Key no: ")

    if request_type == "GET":
        request = "GET /assignment1?request=" + key + " HTTP/1.1\r\n\r\n"
    elif request_type == "PUT":
        value = input("Enter value: ")
        request = "PUT /assignment1/" + key + "/" + value + " HTTP/1.1\r\n\r\n"
    elif request_type == "DELETE":
        request = "DELETE /assignment1/" + key + " HTTP/1.1\r\n\r\n"
    else :
        print("Please enter a valid request: GET/PUT/DELETE.")
        continue
    send_request(request)
s.close()
