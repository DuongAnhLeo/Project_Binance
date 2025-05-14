#Case này là xu hướng tăng của thị trường

"""Nến người treo cổ: nếu xuất hiện sau xu hướng tăng của thị trường, mẫu
 hình có thể đảo chiều
"""
#Hanging Man 
def HangingMan(candle):
    openPrice = candle.get_open_price() 
    closePrice = candle.get_close_price() 
    highPrice = candle.get_high_price() 
    lowPrice = candle.get_low_price()
    
    body = abs(closePrice - openPrice) #Thân nến 
    low_shadow = min(openPrice, closePrice) - lowPrice 
    up_shadow = highPrice - max(openPrice, closePrice)
    
    return low_shadow >= 1.5 * body and up_shadow <= body*0.6
    #bóng dưới dài gấp 2 lần thân nến, bóng trên thấp


"""Mẫu hình Mây đen bao phủ

Là nến xuất hiện sau xu hướng tăng củ thị trường, gồm có 2 nến: nến thứ nhất là nến tăng,
nến thứ 2 là nến giảm bao phủ hơn 1/2 nến thứ 1
""" 
#Mẫu hình mây đen bao phủ
def DarkCloudCover(candle1, candle2):
    # Nến 1 là tăng (thân xanh)
    if candle1.get_close_price() <= candle1.get_open_price():
        return False 

    # Nến 2 là giảm (thân đỏ) 
    if candle2.get_close_price() >= candle2.get_open_price():
        return False
    
    #Mức 1/2 thân nến thứ 1
    midpoint_candle1 = (candle1.get_open_price() + candle1.get_close_price()) / 2
    
    # Điều kiện Mây Đen Bao Phủ
    return (candle2.get_open_price() > candle1.get_close_price() and
            candle2.get_close_price() < midpoint_candle1 and 
            candle2.get_close_price() > candle1.get_open_price())

"""Mẫu hình Nhấn Chìm Giảm: Là mẫu hình xuất hiện trong xu hướng tăng của thị trường,
báo hiệu dấu hiệu tiêu cực. Gồm có 2 nến: Nến 1 là nến tăng, Nến 2 là 1 nến giảm nuốt trọn
nến 1""" 
#Mẫu hình Nhấn chìm giảm
def BearishEngulfing(candle1, candle2):
    # Nến 1 là tăng (thân xanh)
    if candle1.get_close_price() <= candle1.get_open_price():
        return False

    # Nến 2 là giảm (thân đỏ)
    if candle2.get_close_price() >= candle2.get_open_price():
        return False

    # Điều kiện thân nến 2 bao trùm toàn bộ thân nến 1
    return (candle2.get_open_price() >= candle1.get_close_price() and
            candle2.get_close_price() <= candle1.get_open_price())