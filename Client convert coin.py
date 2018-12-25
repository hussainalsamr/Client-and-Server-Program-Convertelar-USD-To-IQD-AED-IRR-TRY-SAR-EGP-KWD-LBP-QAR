import socket
print ('The Program Converter from USA(Dollar) To IQD,.....,TRY Write by Programer Hussain alsamr ')
print('')
print('1:Iraq(IQD)   2:UAE(AED)   3:Iran(IRR)   4:Saudi Arabia(SAR)   5:Turkey(TRY)')
print('6:Egypt(EGP)  7:Lebanon(LBP)  8:Kuwait(KWD)  9:Qatar(QAR)')
print(" ")
serverip='127.0.0.1'
serverport=12800
BUFFER_SIZE=1024
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
opp=['IQD','AED','IRR','TRY','SAR','EGP','KWD','LBP','QAR']
while 1:
   x=input("pleas inter Money is USA(Dollar) :")
   print('NOTE : Inter Characters Large ')
   op=input('Currency Converter to ( IQD , AED , IRR , TRY , SAR , EGP , KWD , LBP , QAR ) :')
   if op=='IQD':op='IQD'
   if op=='AED':op='AED'
   if op=='IRR':op='IRR'
   if op=='SAR':op='SAR'
   if op=='TRY':op='TRY'
   if op=='EGP':op='EGP'
   if op=='KWD':op='KWD'
   if op=='LBP':op='LBP'
   if op=='QAR':op='QAR'


   message=(op+' '+x)
   client.sendto(message.encode('utf-8'),(serverip,serverport))
   response,address=client.recvfrom(BUFFER_SIZE)
   print (x+'$'' ''='+response.decode('utf-8'))

client.close()