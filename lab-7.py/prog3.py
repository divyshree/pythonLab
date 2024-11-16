""""3. Create two classes Teacher and Author, each with their own description() method to describe 
the profession. Then, create a subclass TutorAuthor that inherits from both Teacher and Author. 
Use this subclass to call the description() method from each parent class. Use the super() function 
to resolve any conflicts if necessary."""
# Answer:
class Teacher:
    def description(self):
        print("I am a teacher. I teach students.")

class Author:
    def description(self):
        print("I am an author. I write books.")

class TutorAuthor(Teacher, Author):
    def description(self):
        super().description()  # Call the method from the first parent class
        print("I am also an author and a teacher.")

# Create an instance of TutorAuthor
tutor_author = TutorAuthor()
tutor_author.description()

