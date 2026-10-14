print("cm","to","inches","to","m","to","km","to","yard")
print("1:cm to km")
print("2:km to cm")
print("3:inches to km")
user_choice=input("what would you like to convert?:")

length_list=("cm","inches","metres","ki lometeres","yard")

if user_choice=="1":
    cm_conv=float(input("how much cm do you want to convert?:"))
    print(float(cm_conv/100))

if user_choice=="2":
    km_conv=float(input("how much km do you want to convert?:"))
    print(float(km_conv*100000))

if user_choice=="3":
    inch_conv=float(input("how much inches would you like to convert?:"))
    print(float(inch_conv/39370.079))