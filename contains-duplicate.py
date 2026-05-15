class Solution:
    def containsDuplicate(self,nums):
        da_gap=set() # Danh sach de luu cac so da gap 

        for so in nums: # duyet tung so trong mang 
            if so in da_gap: # So da xuat hien truoc do
                return True # Co trung
            da_gap.add(so)# Neu chua co thi them vao danh sach
        return False # Duyet xong ma khong bi trung 