# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:				
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

def solution(ransom, magazine):
    magazine_letters = list(magazine)
    for letter in ransom:
        if letter in magazine_letters:
            magazine_letters.remove(letter)
        else:
            return False
    return True
