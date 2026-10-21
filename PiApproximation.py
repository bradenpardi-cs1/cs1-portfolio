#PiApproximation.py


"""This program will approximate the value of PI within the tolerance the user
gives."""

pi = 3.14159265358979
k = 1

print("We are finding the minimum number of terms needed to get an approximation of pi accurate within our error tolerance.")
print()
error_tol = float(input("Input error tolerance:"))


print("Number of terms \t Pi Approximation")
pi_approx = 0
counter = 1 

while abs(pi - pi_approx) >= error_tol:
    pi_approx = ((4*(-1)**(k+1))) / ((2*k)-1) + pi_approx
    print(counter, "\t\t\t\t\t", pi_approx)
    
    counter += 1
    k += 1

print()
print(f"After {counter - 1} terms, pi is apporximately {pi_approx}.")
print(f"Our error is {abs(pi - pi_approx)} which is less than or equal to {error_tol}")