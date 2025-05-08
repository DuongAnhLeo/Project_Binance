import requests
import json
from datetime import datetime
from Draw import draw_candlestick_chart
from Case_1 import Hammer
from Trend import DownTrend, UpTrend

#Request đến URL này (của Cafef) để có thể lấy API của các mã cổ phiếu
URL = "https://cafef.vn/du-lieu/Ajax/PageNew/DataHistory/PriceHistory.ashx?Symbol=" 

#Nhập thông tin của mã cổ phiếu, ngày bắt đầu, kết thúc của mã cổ phiếu đó 
Symbol = input("Nhập mã cổ phiếu (ví dụ: VHM): ").upper() 
StartDate = input("Nhập ngày bắt đầu (định dạng yyyy-MM-dd): ") 
EndDate = input("Nhập ngày kết thúc (định dạng yyyy-MM-dd): ") 
#Tạo URL động để request lấy API theo từng mã cổ phiếu mình muốn
queryURL = URL + Symbol + f"&" + f"StartDate=" + StartDate + f"&" + f"EndDate=" + EndDate
response = requests.get(queryURL) 
#Tạo 1 lớp, mỗi lớp này là mỗi cây nến, mỗi cây nến sẽ cần các thông tin như giá mở cửa, giá đóng cửa
#giá cao nhất trong ngày, giá thấp nhất trong ngày
class Candlestick:
    def __init__(self, open_price, close_price, high_price, low_price, date):
        self._open_price = open_price
        self._close_price = close_price
        self._high_price = high_price
        self._low_price = low_price
        self.date = date

    # Lấy giá trị của cây nến
    def get_open_price(self): return self._open_price
    def get_close_price(self): return self._close_price
    def get_high_price(self): return self._high_price
    def get_low_price(self): return self._low_price
    def __str__(self):
        return f"Open: {self._open_price}, Close: {self._close_price}, High: {self._high_price}, Low: {self._low_price}"
#Tạo 1 Map với key: số thứ tự nến Value: Cây nến
Candlestick_Map = {} 

#Thông tin mà mình đã lấy được từ URL của mã chứng khoán đó. 
if response.status_code == 200:
    try:
        data = response.json()
        # Truy cập vào danh sách dữ liệu 
        records = data.get("Data", {}).get("Data", []) 
        #Vì trong URL đang có vấn đề về thứ tự (bị ngược) nên chúng ta cần lật lại 
        start_dt = datetime.strptime(StartDate, "%Y-%m-%d") 
        end_dt = datetime.strptime(EndDate, "%Y-%m-%d") 
        # Tạo 1 list để đảo ngược thời gian 
        Reversed_Time = []  
        for item in reversed(records): 
            date_str = item.get("Ngay")  # VD: "25/04/2025"
            date_obj = datetime.strptime(date_str, "%d/%m/%Y") 
            if start_dt <= date_obj <= end_dt: #So sánh nếu ngày đó không nằm trong khoảng [start, end] thì không thêm vào
                Reversed_Time.append(item) 
        i = 0 #đếm số cây nến 
        if records:
            for i, item in enumerate(Reversed_Time, start=1):
                Date = item.get('Ngay') 
                ClosePrice = item.get('GiaDongCua') 
                OpenPrice = item.get('GiaMoCua') 
                HighPrice = item.get('GiaCaoNhat')
                LowPrice = item.get('GiaThapNhat') 

                #Bỏ qua nếu thiếu dữ liệu đóng cửa, mở cửa...
                if None in (OpenPrice, ClosePrice, HighPrice, LowPrice):
                    continue

                #Thêm những dữ liệu cần cho vào cây nến (Candlestick) 
                Candle = Candlestick(float(OpenPrice), float(ClosePrice), float(HighPrice), float(LowPrice), date_obj)
                Candle.date = date_obj  # Gán ngày cho đối tượng để dùng khi vẽ biểu đồ
                Candlestick_Map[i] = Candle #Gán cây nến với số thứ tự  

            #In danh sách các nến 
            print("\n----Danh Sách Các Nến----")
            for key, value in Candlestick_Map.items(): 
                print(f"Nến số {key}: {value}") 

            for i in range(4, len(Candlestick_Map) + 1):  # Bắt đầu từ nến thứ 4 vì cần đủ 3 cây trước để xét xu hướng
                if DownTrend(Candlestick_Map, i - 1):  # xu hướng giảm kết thúc tại i-1
                    hammer_candle = Candlestick_Map[i]
                    if Hammer(hammer_candle):
                        print(f"Nến số {i} là NẾN BÚA sau xu hướng giảm. Khả năng đảo chiều tăng!")

                if UpTrend(Candlestick_Map, i - 1):
                    print(f"Nến số {i} nằm sau xu hướng tăng.")

            #Mô phỏng lại biểu đồ của các cây nến
            draw_candlestick_chart(Candlestick_Map, symbol=Symbol)
        else: 
            print("Không có dữ liệu cho khoảng thời gian này.") 
    
    except ValueError:
        print("Phản hồi không phải là JSON hợp lệ.") 
else:
    print(f"Lỗi khi gửi yêu cầu: {response.status_code}") 