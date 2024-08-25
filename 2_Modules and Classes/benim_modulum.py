"""
Asil Can Yılmaz tarafından 14.03.2023 tarihinde yazılmıştır.
"""

favori_sayim = 12

def factorial(n):
    """
    Bu fonksiyon 1'den büyük tam sayıların faktoriyelini hesaplar
    1'den küçük veya tam sayı değeri olmayan değeri hesaplayamaz, -1 sonucunu üretir.
    """
    if n % 1 != 0 or n < 1:
        return -1
    elif n == 1:
        return n
    else:
        return n * factorial(n-1)