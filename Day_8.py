#  Name - Sarthak Sanjay Sonpatki
# Day-8
# all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang',
# 'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']
#
# Take user input:
#   - name, email
#
# Create user dictionary with the keys:
#   - name, email, courses
#   user = {
#     'name': 'Harsh',
#     'email': 'harsh@gmail.com',
#     'courses': []
#   }
#
# Show menu
#   1. All courses
#     -- show all courses
#     -- user will select one course
#     -- add the selected course to user profile
#   2. My courses
#     -- show enrolled courses
#   3. Show profile
#     -- display name and email of user
#   0. Exit
#
# while True:
#   print -- show the menu
#   choice = input('Enter your choice : ')
#   if choice == 0:
#     exit(1)
#   elif choice == 1:
#     show all courses
#   elif choice == 2:
#     show enrolled courses
#   elif choice == 3:
#       Display user profile

all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi', 'Go lang',
                'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']

name = input("Enter your name : ")
email = input("Enter your email : ")
courses=[]
user = {'name': name, 'email': email, 'courses': [courses]}

while True:
    print("\nMENU")
    print("1. All Courses")
    print("2. My Courses")
    print("3. Show Profile")
    print("4. Edit Profile")
    print("0. Exit")
    ch=int(input("Enter your choice : "))

    if ch==0:
        print("Thank you for Enrolling!")
        break

    elif ch==1:
        print("\nAll Courses are:-")
        for i in range(len(all_courses)):
            print(f"{i+1}. {all_courses[i]}")
        a=int(input("Enter the course :"))
        courses.append(all_courses[a - 1])
        all_courses.pop(a-1)
        for j in range(len(all_courses)):
            print(f"{j + 1}. {all_courses[j]}")

    elif ch==2:
        print("\nYour Enrolled Courses are:-")
        for i in range(len(courses)):
            print(f"{i+1}. {courses[i]}")
        if courses == []:
            print("No course enrolled.")

    elif ch==3:
        print('\nPROFILE:-','\nName= ',user['name'],'\nEmail= ',user['email'])
        if courses == []:
            print("No course enrolled.")
        else:
            for i in range(len(courses)):
                print('Courses = ',f"{i + 1}. {courses[i]}")

    elif ch==4:
        print("\nWhat You Want To edit? ")
        print("1. Name")
        print("2. Email")
        print("3. My Courses")
        h = int(input("Enter your choice : "))
        if h==1:
            new_name= input("Enter New name : ")
            user['name']= new_name
        elif h==2:
            new_email=input("Enter New email : ")
            user['email']=new_email
        elif h==3:
            for i in range(len(courses)):
                print('Courses = ',f"{i + 1}. {courses[i]}")
            c=int(input("Enter : "))
            courses.pop(c-1)
        print('PROFILE-', '\nName= ', user['name'], '\nEmail= ', user['email'])
        if courses == []:
            print("No course enrolled.")
        else:
            for i in range(len(courses)):
                print('Courses = ', f"{i + 1}. {courses[i]}")
