"""Great! Let's code the Towers of Hanoi solution in Python. The classic recursive solution moves n disks from source rod to target rod using auxiliary rod:"""

def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n-1, auxiliary, target, source)

# Example: Move 3 disks from rod A to rod C using rod B.
towers_of_hanoi(3, 'A', 'C', 'B')

