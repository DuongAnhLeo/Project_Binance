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
    
    return low_shadow >= 1.5 * body and up_shadow <= body*0.5 
    #bóng dưới dài gấp 2 lần thân nến, bóng trên thấp