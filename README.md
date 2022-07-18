# INSERTION SORT PROJESI
- [22,27,16,2,18,6]
- Yukarıda verilen dizinin sort türüne göre aşamalarını yazınız.
- Big-O gösterimini yazınız.
- Time Complexity:
* Average Case: Aradığımız sayının ortada olması
* Worst Case: Aradığımız sayının en sonda olması
* Best Case: Aradığımız sayının dizinin başında olması
- Diziyi sıraladıktan sonra 18 sayısı hangi case kapsamına girer yazınız.
- [7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.

### CEVAPLAR

#### 1. Sort Aşamaları
- Temel Durum: [22,27,16,2,18,6]
* Aşama1: [22|,27,16,2,18,6]
* Aşama2: [22,27|,16,2,18,6]
* Aşama3: [16,22,27|,2,18,6]
* Aşama4: [2,16,22,27|,18,6]
* Aşama5: [2,16,18,22,27|,6]
* Aşama6: [2,6,16,18,22,27]

### 2. Big-O Gösterimi
- Worst Case: O(n^2)
- Average Case: O(n^2)
- Best Case: O(n)

### 3. Time Compplexity
- Best Case: [2,6,16,18,22,27]
- Worst Case: [27,22,18,16,6,2]

### 4. 18 Sayısı Hangi Case Kapsamına Girer?
- Dizi son halini aldığında [2,6,16,18,22,27] "18" sayısı ortalarda yazılabilir. O halde average case kapsamına girer.

### [7,3,5,8,2,9,4,15,6] Dizisinin Insertion Sort'a Göre İlk 4 Adımı

- A1: [7|,3,5,8,2,9,4,5,6]
- A2: [3,7|,5,8,2,9,4,5,6]
- A3: [3,5,7|,8,2,9,4,5,6]
- A4: [3,537,8|,2,9,4,5,6]




<!---
skryezrn/skryezrn is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
