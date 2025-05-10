# Case này là xu hướng giảm của thị trường

""" Nến Búa: Là nến mà trong 1 xu hướng giảm liên tiếp của thị trường, xuất hiện một nến bất thường,
tức là giá đóng cửa gần bằng giá mở cửa (Cây nến hôm đấy phải ), bóng nến dưới dài 
"""
#Nến búa
def Hammer(candle) -> bool: 
    openPrice = candle.get_open_price() 
    closePrice = candle.get_close_price() 
    highPrice = candle.get_high_price() 
    lowPrice = candle.get_low_price() 

    body = abs(closePrice - openPrice) #Thân nến 
    low_shadow = min(openPrice, closePrice) - lowPrice 
    up_shadow = highPrice - max(openPrice, closePrice)

    return low_shadow >= 1.5 * body and up_shadow <= body*0.5 
    #bóng dưới dài gấp 2 lần thân nến, bóng trên thấp
    
"""Mẫu hình xuyên thấu: Tương tự mẫu hình mây đen bao phủ, mẫu hình xuyên thấu xuất
hiện tong xu hướng giảm của thị trường. Gồm có 2 nến: Nến thứ nhất là nến giảm, nến thứ 2
 là nến tăng xuyên thấu > 1/2 thân của nến thứ nhất""" 
#Mẫu hình xuyên thấu 
def PiercingLine(candle1, candle2):
    # Nến 1 là giảm (thân đỏ)
    if candle1.get_close_price() >= candle1.get_open_price():
        return False

    # Nến 2 là tăng (thân xanh)
    if candle2.get_close_price() <= candle2.get_open_price():
        return False

    # Mức 1/2 thân nến thứ 1
    midpoint_candle1 = (candle1.get_open_price() + candle1.get_close_price()) / 2

    # Điều kiện Xuyên Thấu (Piercing Line)
    return (candle2.get_open_price() < candle1.get_close_price() and
            candle2.get_close_price() > midpoint_candle1)

"""Mẫu hình nhấn chìm tăng: Là mẫu hình xuất hiện trong xu hướng giảm của thị trường,
gồm có 2 nến. Nến thứ nhất là 1 nến giảm, nến thứ 2 là nến tăng, nuốt trọn nến thứ 1 """

#Mẫu hình nhấn chìm tăng 
def BullishEngulfing(candle1, candle2):
    # Nến 1 là giảm (thân đỏ)
    if candle1.get_close_price() >= candle1.get_open_price():
        return False

    # Nến 2 là tăng (thân xanh)
    if candle2.get_close_price() <= candle2.get_open_price():
        return False

    # Thân nến 2 bao trùm toàn bộ thân nến 1
    return (candle2.get_open_price() < candle1.get_close_price() and
            candle2.get_close_price() > candle1.get_open_price())
