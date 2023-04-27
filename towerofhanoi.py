def tower_of_hanoi(n, start_peg, end_peg, aux_peg):
    if n == 1:
        print(f"Move disk 1 from {start_peg} to {end_peg}")
        return
    
    tower_of_hanoi(n-1, start_peg, aux_peg, end_peg)
    print(f"Move disk {n} from {start_peg} to {end_peg}")
    tower_of_hanoi(n-1, aux_peg, end_peg, start_peg)
    
# Example usage
tower_of_hanoi(3, 'A', 'C', 'B')
