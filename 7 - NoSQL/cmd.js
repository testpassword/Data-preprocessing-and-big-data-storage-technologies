/* How many documents are in the base globalStudent in collection student so that the value of the field name is equal to “Semen”? (7) 
There is a mistake in exercise, name should be 'Simon'*/
db.student.find({ name: "Simon" }).count()

// Please specify the names of students (from the collection student) whose surname (field surname) is “Ivanova”.
db.student.find({ surname: "Ivanova" }).pretty()
