-- What is the group of the student 236178? (P3101)
SELECT Group_Code FROM STUDENT 
WHERE Student_ID=236178

-- What is the number of students in the group T3130 of the table STUDENT? (18)
SELECT COUNT(*) FROM STUDENT 
WHERE GROUP_CODE='T3130'

-- Find the average score for the exercise 7 for all students of the faculty corresponding to the letter B (all group codes start with the letter B). (98)
SELECT AVG(Score) FROM STUDENT_TEST 
    JOIN STUDENT ON STUDENT_TEST.Student_ID=STUDENT.Student_ID 
WHERE GROUP_CODE LIKE 'B%' AND Test_ID=7

-- What is the number of students scored for exactly 5 exercises? (2)
SELECT COUNT(*) FROM (
    SELECT Student_ID FROM STUDENT_TEST 
    GROUP BY Student_ID HAVING 
    COUNT(*)=5
)