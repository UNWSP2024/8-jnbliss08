# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

courses = []
while True:
    course_ID = input('Enter course ID: ')
    course_name = input('Enter course name: ')
    courses.append((course_ID, course_name))
    more_courses = input('do you want to enter another course? (y/n)')
    if more_courses == 'N' or more_courses == 'n' or more_courses == 'no':
        break

subject = input('Enter subject name: ')

found = False
for course_ID, course_name in courses:
    if course_ID.split()[0] == subject:
        print(f'Course ID: {course_ID} {course_name}')
        found = True

if not found:
    print(f'no courses found for {subject} ')