
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    """
    Function to find the maximum profit and the number of jobs done.
    Jobs input can be a list of objects or tuples (id, deadline, profit).
    """
    
    # 1. Sort jobs by profit in descending order
    # Assuming jobs are objects for clarity, or we can handle tuples
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # 2. Find max deadline to create slots
    max_deadline = 0
    for job in jobs:
        max_deadline = max(max_deadline, job.deadline)
        
    # 3. Create a schedule array (1-based indexing for convenience)
    # slots[i] = True means time slot i-1 to i is occupied
    slots = [False] * (max_deadline + 1)
    
    count_jobs = 0
    total_profit = 0
    job_sequence = []
    
    # 4. Iterate through sorted jobs and assign slots
    for job in jobs:
        # Try to find a free slot from its deadline down to 1
        # We cap at max_deadline in case a job has a huge deadline but we only care about relative order
        for j in range(min(max_deadline, job.deadline), 0, -1):
            if not slots[j]:
                slots[j] = True
                total_profit += job.profit
                count_jobs += 1
                job_sequence.append(job.id)
                break
                
    return count_jobs, total_profit, job_sequence

# ---------------------------------------------------
# Driver Code
# ---------------------------------------------------
if __name__ == "__main__":
    # Test Case 1
    # Format: (id, deadline, profit)
    jobs_data1 = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
    jobs_objects1 = [Job(id, d, p) for id, d, p in jobs_data1]
    
    # Test Case 2
    jobs_data2 = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 3, 15)]
    jobs_objects2 = [Job(id, d, p) for id, d, p in jobs_data2]

    test_cases = [
        (jobs_objects1, (2, 60)),
        (jobs_objects2, (3, 142))
    ]
    
    print(f"{'Description':<20} | {'Expected (Ct, Prof)':<20} | {'Result':<20} | {'Status'}")
    print("-" * 75)
    
    for i, (jobs_input, expected) in enumerate(test_cases):
        count, profit, seq = job_scheduling(jobs_input)
        result_tuple = (count, profit)
        status = "PASSED" if result_tuple == expected else "FAILED"
        print(f"{f'Test Case {i+1}':<20} | {str(expected):<20} | {str(result_tuple):<20} | {status}")
        print(f"   Selected Job IDs: {seq}")
