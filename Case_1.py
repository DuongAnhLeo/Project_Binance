# Nến búa 
""" Là nến mà trong 1 xu hướng giảm liên tiếp của thị trường, xuất hiện một nến bất thường,
tức là giá đóng cửa gần bằng giá mở cửa (Cây nến hôm đấy phải ), bóng nến dưới dài 
"""

"""Kiểm tra xem nến hiện tại có phải nến búa không""" 
#Nến búa
def Hammer(candle) -> bool: 
    openPrice = candle.get_open_price() 
    closePrice = candle.get_close_price() 
    highPrice = candle.get_high_price() 
    lowPrice = candle.get_low_price() 

    body = abs(closePrice - openPrice) #Thân nến 
    low_shadow = min(openPrice, closePrice) - lowPrice 
    up_shadow = highPrice - max(openPrice, closePrice)

    #if (body == 0): return False 

    return low_shadow >= 1.5 * body and up_shadow <= body*0.3 
    #bóng dưới dài gấp 2 lần thân nến, bóng trên thấp
    

