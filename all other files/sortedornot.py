def check(nums) -> bool:
        f=False
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1]:
                pass
            elif nums[i]<nums[i-1] and not f:
                f=True
                if nums[-1]<=nums[i] and nums[0]>nums[-1]:
                    pass
                else:
                     return False
            else:
                return False


        return True
print(check([2,4,1,3]))