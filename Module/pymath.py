# import random
# cnum =random.randrange(0,100)
# unum=int(input("Enter a number between 0 and 100: "))
# if cnum>unum:
#     print("Computer number is greater than user number",cnum)  
# elif cnum<unum:
#     print("Computer number is less than user number",cnum)
# else:
#     print("Computer number is equal to user number",cnum)
# import os
# os.chdir("C:/Users/jayap/Desktop/New folder")
# i=1
# for file in os.listdir():
#    src=file
#    dst="assign"+str(i)+".txt"
#    os.rename(src,dst)
#    i+=1
#    print(dst)
# import secrets
# import string
# alphabet=string.ascii_letters + string.digits
# #for 20 -character pasword
# password=''.join(secrets.choice(alphabet) for i in range(20))
# print(password)

# import qrcode
# # data='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
# # qr=qrcode.make(data)
# # qr.save("qr_code.png")
# data2={
    
#     'name':'Tanish ',
#     'number':9509913595
# }
# qr=qrcode.make(data2)
# qr.save("Tanish.png")


import cv2
image=cv2.imread("Tanish.png")
detector=cv2.QRCodeDetector()
data,points,straight_qrcode=detector.detectAndDecode(image)
print("Decoded data:",data)
