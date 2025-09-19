import socket

cache = {}

dst_ip = str(input("Enter Cache IP: "))

s = socket.socket()
print ("Socket successfully created")

dport = 12346

s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")

def forward_to_server(message):
    server_ip = "10.0.1.3"
    dport2 = 7712
    s2 = socket.socket()
    s2.connect((server_ip, dport2))
    s2.send(message)
    reply = s2.recv(1024).decode()
    s2.close()
    return reply

def get(key, version):
  message = ""
  if key in cache:
    message = version + " 200 OK\r\n" + cache[key] + "\r\n\r\n"
  else :
    message = "ToServer"
  return message

def put(key,value,version):
  cache[key] = value
  message = "ToServer"
  return message

def delete(key , version):
  message = "ToServer"
  if key in cache:
    del cache[key]
  return message

def parse(message):
    request, path, version = message.split(' ', 2)
    #print("Request:", request)
    #print("Path:", path)
    #print("Version:", version)
    versions = version.split('\r')
    reply = ""

    if(request == "GET"):
      loc , key = path.split('=',1)
      reply = get(key , versions[0])
    elif (request == "PUT"):
      slash, loc , key , value = path.split('/',3)
      #print("key ",key)
      #print("value ",value)
      reply = put(key,value,versions[0])
    else :
      slash, loc , key = path.split('/',2)
      #print("key ",key)
      reply = delete(key,versions[0])
    if(reply == "ToServer"):
        reply = forward_to_server(message)
        if request == "GET" :
            if 'OK' in reply:
              temp = reply.split('\r\n') 
              if temp[1] != "":
                cache[key] = temp[1]
    print(reply)
    return reply

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    
    while True:
        recvmsg = c.recv(1024).decode()
        #print("recieved ", recvmsg)
        if recvmsg == "exit":
            print("Closing connection with client", addr)
            break
        else:
            reply = parse(recvmsg)
            c.send(reply.encode())
    c.close()