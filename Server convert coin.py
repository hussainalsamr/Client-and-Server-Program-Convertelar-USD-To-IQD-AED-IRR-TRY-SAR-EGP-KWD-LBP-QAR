import socket
def con(message):
    numbers=[]
    parameters=[]
    coin_op=['IQD','AED','IRR','TRY','SAR','EGP','KWD','LBP','QAR']
    parameters=message.split()
    if len(parameters)>2:return 'Invalid request:you most inter only two Parameters'
    if not (parameters[1].isdigit()): return 'Invalid request:second parameters must be digits'
    if not (parameters[0] in coin_op): return  "Invalid request: first parameters must be one of ('IQD','AED','IRR','TRY','SAR','EGP','KWD','LBP','QAR)"
    if (parameters[0]=='IQD'):return (float(parameters[1]) *1190.1078,'IQD')
    if (parameters[0] == 'AED'): return (float(parameters[1])*3.6725,'AED' )
    if (parameters[0] == 'IRR'): return (float(parameters[1])*41997.86,'IRR')
    if (parameters[0] == 'TRY'): return (float(parameters[1])*5.3162,'TRY')
    if (parameters[0] == 'SAR'): return (float(parameters[1]) * 3.7500, 'SAR')
    if (parameters[0] == 'EGP'): return (float(parameters[1]) * 17.9063, 'EGP')
    if (parameters[0] == 'KWD'): return (float(parameters[1]) * 0.3040, 'KWD')
    if (parameters[0] == 'LBP'): return (float(parameters[1]) * 1507.5, 'LBP')
    if (parameters[0] == 'QAR'): return (float(parameters[1]) * 3.640, 'QAR')

serverport=12800
BUFFER_SIZE=1024
serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind(('',serverport))
print('The server is ready to receive port 12800')
while 1:

    message,clientaddress=serversocket.recvfrom(BUFFER_SIZE)
    message=message.decode('utf-8')
    response=str(con(message))
    par = message.split()
    serversocket.sendto(response.encode('utf-8'),clientaddress)
    print(str( par[1])+'$'' ''='+str(response))

serversocket.close()
