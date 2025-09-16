range ( star, stop, step )
step mặc định = 1
(a) range(5)
→ Từ 0 đến 4, bước nhảy 1.
Kết quả: [0, 1, 2, 3, 4]

(b) range(5, 10)
→ Từ 5 đến 9, bước nhảy 1.
Kết quả: [5, 6, 7, 8, 9]

(c) range(5, 20, 3)
→ Từ 5 đến nhỏ hơn 20, bước nhảy 3.
Kết quả: [5, 8, 11, 14, 17]

(d) range(20, 5, -1)
→ Từ 20 đến lớn hơn 5, bước nhảy -1.
Kết quả: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

(e) range(20, 5, -3)
→ Từ 20 đến lớn hơn 5, bước nhảy -3.
Kết quả: [20, 17, 14, 11, 8]

(f) range(10, 5)
→ Mặc định bước nhảy = +1, nhưng 10 > 5 nên không chạy.

(g) range(0)
→ Từ 0 đến nhỏ hơn 0 → không có giá trị.

(h) range(10, 101, 10)
→ Từ 10 đến ≤ 100, bước nhảy 10.
Kết quả: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

(i) range(10, -1, -1)
→ Từ 10 đến ≥ 0, bước nhảy -1.
Kết quả: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

(j) range(-3, 4)
→ Từ -3 đến 3, bước nhảy +1.
Kết quả: [-3, -2, -1, 0, 1, 2, 3]

(k) range(0, 10, 1)
→ Từ 0 đến 9, bước nhảy 1.
Kết quả: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]