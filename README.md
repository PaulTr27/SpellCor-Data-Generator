# SpellCor-Data-Generator

## Overview
This is a repository containings data generators for spell correcting models of LHP-CoTAI NLP study group.

## Base pipeline/data generator types
*Insert here (type, tables, papers ,etc.)*
<pre>
In Vietnamese letters there are:
17 alone consonants: b c d đ g h k l m n p q r s t v x
10 mix consonants: ch gh gi kh ng ngh nh th tr qu
6 vowels: a e i o u y and each vowel has some diacritical marks
a: a à á ả ã ạ ă ằ ắ ẳ ẵ ặ â ầ ấ ẩ ẫ ậ (15)
e: e è é ẻ ẽ ẹ ê ề ế ể ễ ệ (10)
i: i ì í ỉ ĩ ị (5)
o: o ò ó ỏ õ ọ ơ ờ ớ ở ỡ ợ ô ồ ố ổ ỗ ộ (15) 
u: u ù ú ủ ũ ụ ư ừ ứ ử ữ ự (10)
y: y ỳ ý ỷ ỹ ỵ (5)
</pre>

**Types of Error in Vietnamese**
Number | Label  | Description | Example |
------| -------- | -------- | ------- |
0 | No error | There isn't any spelling error in this text | "Đây là một câu đúng." (This is a correct sentence)
1 | Telex typing error     | A mistyping in telex  | "Cais gif" instead of "Cái gì"(What)
2 | VNI typing error | A mistyping in VNI | "Cai1 gi2" instead of "Cái gì"
3| Mising diacritical marks | Vietnamese words that have diacritical marks do not have the same meaning as don't have | "M**a**" is a ghost but "M**ã**" is a horse 
4| Excess letter error | Accidentally type extra letter | "Nước**c**" instead of "Nước" (Water)
5 | Missing letter error | Accidentally type missing letter | "Tá" instead of "Tá**o**" (Apple)
6 | Wrong spelling | Replace a right vowel, consonants or mix consonant to a wrong one | Example in below

In Wrong Spelling there are 6 errors (will update more errors in future):
Number | Type of wrong spelling | Description | Example |
-----| ------ | -----| -----|
1 | Wrong starting letter between "d" and "gi" | Pronouncing "d" and "gi" are quite the same in Vietnam so usually typing the wrong consonant | "Cái **d**ì" instead of "Cái **gì**"
2 | Wrong starting letter between "l" and "r" | Pronouncing "l" and "r" are quite the same in Vietnam so usually typing the wrong consonant | "Cái **l**ăng" instead of "Cái **r**ăng"(tooth)
3 | Wrong starting letter between "b" and "p" | Pronouncing "b" and "p" are quite the same in Vietnam so usually typing the wrong consonant | "Con **p**ò" instead of "Con **b**ò" (Cow)
4 |  Wrong starting letter between "x" and "s" | Pronouncing "x" and "s" are quite the same in Vietnam so usually typing the wrong consonant | "**S**ui" instead of "**X**ui" (Unlucky)
5 | Wrong starting letter between "c" and "k" | There is a rule in Vietnamese when chosing "c" and "k". if a letter after the consonant is "i", "y", "e" or "ê" then the consonant is "k". Another case will use the "c" consonant. | "**K**ỵ sĩ" (horseman), "**K**ênh TV" (TV channel), "**C**ơm" (Rice), "**C**á" (Fish)
6 | Wrong starting letter between "ch" and "tr" | Pronouncing "ch" and "tr" are quite the same in Vietnam so usually typing the wrong consonant | "Con **tr**ó" instead of "Con **ch**ó" (Dog)
