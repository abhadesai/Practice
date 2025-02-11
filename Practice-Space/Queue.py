from collections import deque


def QueuePractice() -> None:

    #Create from double ended queue (deque)

        queue = deque()

    #Create from list

        my_list = [1,2,3]

        queue = deque(my_list)

        queue.append(1)     # append to front
        queue.appendleft(1) # append to back
        queue.popleft()     #remove element from the front
        queue.pop()         # remove element from back

    #Check if queue is empty

        if len(queue) == 0:
                return True
    
    #Get size of the queue

        size = len(queue)
    
    #Remove all elements

        queue.clear()
        queue.appendleft()

