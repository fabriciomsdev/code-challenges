const revertString = (str: string): string => {
    return str.split('').reverse().join('');
}

const isValid = (subString: string, greatestPalindromic: string): boolean => {
    const isPalindromic = subString === revertString(subString);
    const greatestLenght = greatestPalindromic?.length ?? 0;
    const greatest =  subString.length > greatestLenght;

    return isPalindromic && greatest;
}

const getGreatestPalindromic = (text: string): string => {
    let greatestPalindromic = null;

    for (let i = 0; i < text.length; i++) {
        for (let j = i + 1; j < text.length; j++) {
            const subString = text.slice(i, j);
            if (subString && isValid(subString, greatestPalindromic)) greatestPalindromic = subString;
        }

        const subString = text.slice(i);
        if (subString && isValid(subString, greatestPalindromic)) greatestPalindromic = subString;
    }
    
    return greatestPalindromic;
}

function longestPalindrome(s: string): string {
    return getGreatestPalindromic(s);
};
