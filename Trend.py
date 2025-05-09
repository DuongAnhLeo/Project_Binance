#Xu hướng tăng liên tục
def DownTrend(Candles_Map, index, window=3, allow_break=1): 
    if index <= window: 
        return False

    breaks = 0
    for i in range(index - window + 1, index + 1): 
        prev_candles = Candles_Map[i - 1] 
        curr_candles = Candles_Map[i] 
        if prev_candles.get_close_price() <= curr_candles.get_close_price(): 
            breaks += 1
            if breaks > allow_break: 
                return False
    return True  

#Xu hướng giảm liên tục
def UpTrend(Candles_Map, index, window=3, allow_break=1): 
    if index <= window: 
        return False

    breaks = 0
    for i in range(index - window + 1, index + 1): 
        prev_candles = Candles_Map[i - 1] 
        curr_candles = Candles_Map[i] 
        if prev_candles.get_close_price() >= curr_candles.get_close_price(): 
            breaks += 1
            if breaks > allow_break: 
                return False
    return True  