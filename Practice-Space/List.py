def listPractice(nums: list[int]) -> bool:

    ###List###

    nums = [0] * 5          #List with 5 zeroes.
    nums = [0] * len(nums)  #List with same length as nums
    [[] for i in range(len(nums) + 1)]  # CHECK THIS!!!!

        ##List Comprehension##

    nums = [x * 2 for x in range(5)]    # [0,2,4,6,8]. Gives a list with some condition
    
        ##Append##
    nums = []
    nums.append(1)      # when adding elements dynamically. may not be used much

    ###Looping###

    #With index and value

    for i,n in enumerate(nums):
        print(i,n)

    nums.reverse()
    nums.sort



    
