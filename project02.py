import numpy as np
import matplotlib.pyplot as plt


total_marks = np.random.randint(1, 101, 100)

print("Marks:\n", total_marks)

# Average, minimum ,maximum
print("\nAverage marks:", np.mean(total_marks))
print("Minimum marks:", np.min(total_marks))
print("Maximum marks:", np.max(total_marks))

# Pass and Fail
passed = np.sum(total_marks >= 33)
failed = np.sum(total_marks < 33)

print("\nPassed students:", passed)
print("Failed students:", failed)

# Pass percentage
pass_percentage = (passed / len(total_marks)) * 100
print(f"Pass percentage: {pass_percentage:.2f}%")

# Grades
A = np.sum(total_marks >= 90)
B = np.sum((total_marks >= 75) & (total_marks < 90))
C = np.sum((total_marks >= 60) & (total_marks < 75))
D = np.sum((total_marks >= 45) & (total_marks < 60))
E = np.sum((total_marks >= 33) & (total_marks < 45))
F = np.sum(total_marks < 33)

print("\nGrades:")
print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)
print("E:", E)
print("F:", F)

# Top 5 ans Bottom 5 marks
sorted_marks = np.sort(total_marks)

print("\nTop 5 marks:", sorted_marks[-5:])
print("Bottom 5 marks:", sorted_marks[:5])

# Histogram
plt.hist(total_marks, bins=10)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")
plt.show()