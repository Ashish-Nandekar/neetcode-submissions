class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        //convert string to char array
        char[] a = s.toCharArray();
        char[] b = t.toCharArray();

        //Sort it in ascending order
        Arrays.sort(a);
        Arrays.sort(b);

        return Arrays.equals(a, b);
    }
}
