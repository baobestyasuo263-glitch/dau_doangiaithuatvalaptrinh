class Solution(object):

    def wordPattern(self, pattern, s):

        # Tách chuỗi thành danh sách từ
        words = s.split()

        # Nếu số lượng khác nhau -> sai ngay
        if len(pattern) != len(words):
            return False

        # Map ký tự -> từ
        char_to_word = {}

        # Map từ -> ký tự
        word_to_char = {}

        # Duyệt từng vị trí
        for i in range(len(pattern)):

            c = pattern[i]
            w = words[i]

            # Nếu ký tự đã tồn tại
            if c in char_to_word:

                # Nhưng map khác từ hiện tại
                if char_to_word[c] != w:
                    return False

            else:
                # Lưu mapping
                char_to_word[c] = w

            # Kiểm tra chiều ngược lại
            if w in word_to_char:

                if word_to_char[w] != c:
                    return False

            else:
                word_to_char[w] = c

        return True