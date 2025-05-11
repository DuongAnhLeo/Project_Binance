import pandas as pd
import mplfinance as mpf
from datetime import datetime
from mplfinance import make_addplot

def draw_candlestick_chart(candlestick_map, symbol="Mã cổ phiếu"):
    """
    Nhận dữ liệu từ dict cây nến và vẽ biểu đồ nến.
    Mỗi cây nến trong dict phải có dạng: key = int, value = Candlestick instance.
    """
    candles = []
    for i, candle in candlestick_map.items():
        if not hasattr(candle, 'date'): 
            continue  # Bỏ qua nếu không có ngày

        date = candle.date
        open_price = candle.get_open_price()
        high_price = candle.get_high_price()
        low_price = candle.get_low_price()
        close_price = candle.get_close_price()

        if None in (open_price, high_price, low_price, close_price):
            continue

        candles.append({
            "Date": date,
            "Open": float(open_price),
            "High": float(high_price),
            "Low": float(low_price),
            "Close": float(close_price)
        })

    if not candles:
        print("Không có dữ liệu hợp lệ để vẽ biểu đồ.")
        return

    df = pd.DataFrame(candles)
    df.set_index("Date", inplace=True)

# Vẽ biểu đồ nến + đường dữ liệu
    close_prices = df["Close"]
    offset = (close_prices.max() - close_prices.min()) * 0.3  # Khoảng cách ~1cm
    shifted_close = close_prices - offset

    shifted_parallel = close_prices + offset  # Đường song song với đường

    add_plot = [make_addplot(shifted_close, color='blue', width=1.2, label='Dữ liệu thật'),
                make_addplot(shifted_parallel, color='red', width=1.2, linestyle='dotted', label='Đường dự đoán')]

    mpf.plot(df, type='candle', style='charles',
             title=f"Biểu đồ {symbol}",
             volume=False,
             addplot=add_plot,
             ylabel='Giá',
             ylabel_lower=''
            )

