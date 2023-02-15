# from wsgiref.util import request_uri


# code reuse 
# memory alloctaion 

class Mobile:
    model='S22'
    processor='snapdragon'
    display='6inches'
    camera='128mp'
    ram='4GB'
    color='blue'

    def power_on(self):
        print('switch on')

    def power_off(self):
        print('switch off')

    def camera_on(self):
        print('camera on')

Mobile1 =Mobile()
Mobile2=Mobile()
Mobile1.power_on()
Mobile2.power_on()
print(Mobile1.model)




# class Mobile:

# # constructor work when we create an object 

#     def __init__(self,model,display,processor,camera,ram,color):
#         # print('constructor')
#         self.model_=model
#         self.display_=display
#         self.processor_=processor
#         self.camera_=camera
#         self.ram_=ram
#         self.color_=color 
#     def power_on(self):
#         print('switch on')
#         # print(self.camera_)

#     def power_off(self):
#         print('switch off')

#     def camera_on(self):
#         print('camera on')

# mobile1=Mobile('S22','6in','qualcon','64mp','4GB','blue')
# print(mobile1.ram_)
# mobile2=Mobile('Redmi','6in','snapdragon','128mp','8GB','black')
# print(mobile2.display_)
# print(mobile2.color_)
# mobile1.power_on()
# mobile2.power_off()