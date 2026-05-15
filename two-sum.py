class Solution:
    def twoSum(self,nums,target):
        da_gap={}#Dung de luu: so-< vi tri

        for i in range(len(nums)): # duyet tung vi tri trong mang nums
            so=nums[i]# Lay gia tri tai vi tri i
            so_can_tim = target - so #Tinh so con thieu de tong = target
            if so_can_tim in da_gap:
                # Neu so can tim da xuat hien trong do
                #Thi ta tim dc 2 so thoa man 
                return [da_gap[so_can_tim],i]
                #Tra ve vi tri so da gap va vi tri can tim
            da_gap[so]=i
            #De luu so hien tai va vi tri cua no

