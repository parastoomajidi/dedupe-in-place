class solution
    def find k(self, nums, val):
        k = 0
        iw = 0
        ir = 0
        
        while(ir < len(nums)):
            if nums[ir] != val:
                k += 1
                nums[iw] = nums[ir]
                iw += 1
            ir += 1

        return k