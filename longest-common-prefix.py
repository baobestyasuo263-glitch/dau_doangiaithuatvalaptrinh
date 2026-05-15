class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: #Neu mang rong thi tra ve ""
            return ""
        for i in range(len(strs[0])):#Duyet tung ki tu
            ch = strs[0][i]
            #Lay vi tri dau tien trong danh sach 
            ##Lay vi tri thu i
            #Gan cho ch
            for s in strs:#So sanh cac ki nay voi cac chuoi con lai 
                if i >= len(s) or s[i] != ch:
                #Neu do dai hoac khac ky tu
                #Kiem tra do dai cua ki tu
                # Ky tu thu i cua chuoi s co giong ch khong
                #Chi can 1 trong 2 dk dung thi dung luon
                    return strs[0][:i] 
                    #Tra ve chuoi tu dau den truoc ki tu i

        return strs[0]