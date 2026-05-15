class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups={} #Dung tu dien de nhom cac anagrams

        for s in strs:
            key="".join(sorted(s))
            #sap xep cac ki tu trong chuoi s 
            #sorted(s) tach chuoi s thanh tung ky tu sap xep theo bang chu cai 
            #join ghep cac phan tu trong list thanh mot chuoi
            #"" dung de noi lien va khong co khoang trong 
            if key not in groups: 
                #Neu key chua co trong groups thi taoj danh sach moi
                groups[key] =[]
            groups[key].append(s)
            #Them s vao danh tuong ung trong groups
        return list(groups.values()) 
        #tra ve danh sach cac nhom  


        