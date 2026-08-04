import sys
def time_slots_consolidation():
    input= sys.stdin.read().split()
    if not input:
        return          
    n = int(input[0])     
    intervals = []     
    idx = 1     
    for i in range(n):         
        start = int(input[idx])         
        end = int(input[idx+1])         
        intervals.append((start, end))         
        idx = idx+ 2           
    intervals.sort(key=lambda x: x[0])      
    merged = []     
    for i in intervals:         
        if not merged or merged[-1][1] < i[0]:             
            merged.append(i)         
        else:             
            merged[-1] = (merged[-1][0], max(merged[-1][1], i[1]))      
    for start, end in merged:
        print(f"{start} {end}")  
if __name__ == '__main__':     
    time_slots_consolidation()
