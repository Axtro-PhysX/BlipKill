import random  # Import the random module for shuffling and randomness

def main():
    try:
        # Retrieve a list of process IDs, excluding any IDs that are 1 or lower
        procs = [proc['pid'] for proc in process.list() if proc['pid'] > 1]
        to_snap = len(procs) // 2  # Calculate half of the process count to determine how many to snap
        snapped = set()  # Use a set to store snapped process IDs for efficient look-up and uniqueness

        # Randomly shuffle the list of process IDs to ensure a random selection
        random.shuffle(procs)

        # Loop through the shuffled list and snap processes until half are terminated
        for i, proc in enumerate(procs):
            if len(snapped) >= to_snap:  # Break the loop if enough processes have been snapped
                break
            if proc not in snapped:  # Check if the process is already snapped
                print(f'Adding {proc}')  # Notify that the process is being added to the snapped set
                snapped.add(proc)  # Add the process ID to the snapped set
            else:
                print(f'Failed to add {proc}')  # Notify if the process was already in the snapped set

        # After snapping, terminate each process in the snapped set
        for snap in snapped:
            print(f'KILL {snap}')  # Notify which process is being terminated
            process.kill(snap)  # Call the process.kill method to terminate the process

        print(f'Completed snapping {len(snapped)} processes.')  # Print completion message with count of snapped processes

    except Exception as e:
        print(f"An error occurred: {e}")  # Print any exceptions that occur during the execution

# Entry point of the script
if __name__ == "__main__":
    main()
