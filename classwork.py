print ("eligibility for Discount ")
age = int (input ("Enter your age: "))
student = input ("Are you a student? (yes/no): ")
if (age <= 12 or (age >= 13 and age <=  18 and student == "yes" )):
    print ("YOu are eligible for a discount on the movie ticket.")
else:
    print ("You are not eligible for a discount on the movie ticket")
