// Leetcode 242
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        // This is used to store how many of each character has been found in the strings (the frequency of each)
        // Since all will be lowercase alphabet numbers, we can use a size of 26, and get the proper value by
        // subtracting the integer value of the character 'a'. To be able to handle all characters, make the array
        // of size 256 and don't subtract 'a'
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
            freq[t.charAt(i) - 'a']--;
        }
        // After adjusting the frequencies, they should all be zero. If any are not, return false
        for (int i = 0; i < 26; i++) {
            if (freq[i] != 0) {
                return false;
            }
        }
        return true;
    }
}