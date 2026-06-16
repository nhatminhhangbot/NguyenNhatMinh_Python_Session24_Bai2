# Hậu quả của việc để thuộc tính points tự do: gây lỗi logic tính toán và làm sai lệch dữ liệu khi xuất hiện điểm âm
# Decorator cần sử dụng: @property và @points.setter
# Code đúng:

class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        if isinstance(points, int) and points >= 0:
            self.__points = points
        else:
            self.__points = 0
            print("Dữ liệu điểm khởi tạo không hợp lệ! Đã đặt về 0.")

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, new_points):
        if not isinstance(new_points, int) or new_points < 0:
            print("Dữ liệu điểm không hợp lệ!")
        else:
            self.__points = new_points

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount
        else:
            print("Số điểm cộng thêm phải là số nguyên dương!")

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


# 1. Khởi tạo thẻ thành viên
card1 = MemberCard("Le Van C", 100)
print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")

# 2. Thử nghiệm tính năng bảo mật dữ liệu (Validation)
# Thu ngân gõ nhầm điểm âm
print("[Thu ngân gán points = -50]")
card1.points = -50

# Thu ngân gõ nhầm chuỗi
print("[Thu ngân gán points = 'một trăm']")
card1.points = "một trăm"

# Kiểm tra lại điểm xem có bị thay đổi không (Phải giữ nguyên là 100)
print(f"Điểm của {card1.customer_name} sau các lần gõ lỗi: {card1.points}")

# 3. Thử nghiệm hàm tiện ích kiểm tra Voucher từ Class
bill_check_1 = 250000
result_1 = MemberCard.is_eligible_for_voucher(bill_check_1)
print(f"Hóa đơn {bill_check_1:,} VNĐ có được tặng Voucher không? -> {result_1}")

bill_check_2 = 150000
result_2 = MemberCard.is_eligible_for_voucher(bill_check_2)
print(f"Hóa đơn {bill_check_2:,} VNĐ có được tặng Voucher không? -> {result_2}")
