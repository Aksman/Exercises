# EXERCISE
# Create a function that determines if two strings are anagrams of each other.

def areAnagrams(s1: str, s2: str, ignoreNonAlphanumeric: bool = False) -> bool:
    if ignoreNonAlphanumeric:
        s1 = ''.join([c for c in s1 if c.isalnum()])
        s2 = ''.join([c for c in s2 if c.isalnum()])
    
    return sorted(s1.lower()) == sorted(s2.lower())

# Example usage
# This block only runs when the script is run directly.
if __name__ == '__main__':
    import sys
    text1 = sys.argv[1] if len(sys.argv) > 1 else 'listen'
    text2 = sys.argv[2] if len(sys.argv) > 2 else 'silent'

    print(text1)
    print(text2)
    print(f"These are {'' if areAnagrams(text1, text2) else 'not '}anagrams.")
