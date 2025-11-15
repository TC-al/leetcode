class Solution {
    public int[] plusOne(int[] digits) {
        boolean carry = false;
        digits[digits.length - 1]++;
        if (digits[digits.length - 1] == 10) {
            for (int i = 0; i < digits.length; i++) {
                if (carry) {
                    carry = false;
                    digits[digits.length - 1 - i]++;
                }
                if (digits[digits.length - 1 - i] == 10) {
                    if (i == digits.length - 1) {
                        digits[digits.length - 1 - i] = 0;
                        int[] tmp = new int[digits.length+1];
                        for (int j = 0; j < digits.length; j++) {
                            tmp[j+1] = digits[j];
                        }
                        tmp[0] = 1;
                        return tmp;
                    }
                    digits[digits.length - 1 - i] = 0;
                    carry = true;
                }
            }
        }
        return digits;
    }
}