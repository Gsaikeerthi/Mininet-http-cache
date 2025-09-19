import socket

key_val_dict = {
                "key1": "value1",
                "key2": "value2",
                "key3": "value3",
                "key4": "value4",
                "key5": "value5",
                "key6": "value6",
                }


dst_ip = str(input("Enter Server IP: "))

s = socket.socket()
print ("Socket successfully created")

dport = 12346

s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")

def get(key, version):
  message = ""
  if key in key_val_dict :
    message = version + " 200 OK\r\n" + key_val_dict[key] + "\r\n\r\n"
  else :
    message = version + " 404 NOT FOUND\r\n\r\n"
  return message

def put(key,value,version):
  message =""
  if key in key_val_dict:
    message = version + " 200 OK\r\n\r\n"
  else :
    message = version + " 201 CREATED\r\n\r\n"
  key_val_dict[key] = value
  return message

def delete(key , version):
  message = ""
  if key in key_val_dict:
    del key_val_dict[key]
    message = version + " 200 OK\r\n\r\n"
  else :
    message = version + " 404 NOT FOUND\r\n\r\n"
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
    return reply

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    
    while True:
        recvmsg = c.recv(1024).decode()
        if recvmsg == "exit":
            print("Closing connection with client", addr)
            break
        else:
            reply = parse(recvmsg)
            c.send(reply.encode())
    c.close()