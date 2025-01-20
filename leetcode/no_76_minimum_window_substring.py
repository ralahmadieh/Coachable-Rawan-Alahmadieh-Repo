from collections import Counter

def minWindow(s: str, t: str):
    freq_table_t = Counter(t)
    freq_table_window = Counter()
    left = 0
    min_length = float('inf')
    answer = ""
    have, need = 0, len(freq_table_t)  # Track how many characters match the desired frequency

    for right in range(len(s)):
        if s[right] in freq_table_t:
            freq_table_window[s[right]] += 1
            if freq_table_window[s[right]] == freq_table_t[s[right]]:
                have += 1

        while have == need:  # All characters matched
            # Update the result if the current window is smaller
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                answer = s[left:right + 1]

            # Shrink the window from the left
            if s[left] in freq_table_t:
                freq_table_window[s[left]] -= 1
                if freq_table_window[s[left]] < freq_table_t[s[left]]:
                    have -= 1
            left += 1

    return answer