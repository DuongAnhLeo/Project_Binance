import requests
import json

#Request đến URL này (của Cafef) để có thể lấy API của các mã cổ phiếu
URL = "https://cafef.vn/du-lieu/Ajax/PageNew/DataHistory/PriceHistory.ashx?Symbol="

#Nhập thông tin của mã cổ phiếu, ngày bắt đầu, kết thúc của mã cổ phiếu đó
Symbol = input("Nhập mã cổ phiếu (ví dụ: VHM): ").upper()
StartDate = input("Nhập ngày bắt đầu (định dạng yyyy-MM-dd): ") 
EndDate = input("Nhập ngày kết thúc (định dạng yyyy-MM-dd): ")
#Tạo URL động để request lấy API theo từng mã cổ phiếu mình muốn
queryURL = URL + Symbol + f"&" + f"StartDate=" + StartDate + f"&" + f"EndDate=" + EndDate
response = requests.get(queryURL) 
#Tạo 1 lớp, mỗi lớp này là mỗi cây nến, mỗi cây nến sẽ cần các thông tin như ngày, giá mở cửa, giá đóng cửa.
class Candlestick: 
    #constructor 
    def __init__(self, ):
        pass
if response.status_code == 200:
    try:
        data = response.json()
        # Truy cập vào danh sách dữ liệu 
        records = data.get("Data", {}).get("Data", []) 
        if records:
            for item in records:
                print(f"Ngày: {item.get('Ngay')}") 
                print(f"Giá đóng cửa: {item.get('GiaDongCua')}") 
                print(f"Giá mở cửa: {item.get('GiaMoCua')}") 
                print(f"Giá cao nhất: {item.get('GiaCaoNhat')}")
                print(f"Giá thấp nhất: {item.get('GiaThapNhat')}")
                print(f"Khối lượng giao dịch: {item.get('KhoiLuongKhopLenh')}")
                print("-" * 30)
        else:
            print("Không có dữ liệu cho khoảng thời gian này.")
    except ValueError:
        print("Phản hồi không phải là JSON hợp lệ.") 
else:
    print(f"Lỗi khi gửi yêu cầu: {response.status_code}") 

