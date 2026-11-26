class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []

        for s in strs:
            encoded.append(f"{len(s)}#{s}")

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:

        decoded_string_list = []

        cursor_position = 0

        while cursor_position < len(s):
            delimiter_position = s.find("#", cursor_position) #val, start

            word_len = int(s[cursor_position:delimiter_position])

            decoded_string_list.append(s[delimiter_position + 1 : 
            delimiter_position + 1 + word_len])

            cursor_position = delimiter_position + 1 + word_len

        return decoded_string_list