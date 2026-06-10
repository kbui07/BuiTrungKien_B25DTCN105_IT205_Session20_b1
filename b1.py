# Câu 1: Tại sao chương trình báo lỗi ZeroDivisionError: division by zero?
# Phép chia 0 kh hợp lệ
# Câu 2: Nếu xóa ShowMaker thì Chovy sẽ gặp lỗi gì?4
# không thể chuyển chuỗi "ba" thành số nguyên.
# Câu 4: Lợi ích của việc tách hàm calculate_kda()
# Tuân thủ nguyên tắc DRY
# Dễ bảo trì
# Dễ kiểm thử
# Tăng khả năng tái sử dụng

# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
player_stats = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]


def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths

def process_player_stats(player_stats):
    print("--- BANG XEP HANG KDA ---")

    for player in player_stats:
        name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(kills, deaths, assists)

            print(f"Tuyen thu {name} co chi so KDA la: {kda}")

        except ZeroDivisionError:
            print(f"Tuyen thu {name}: KDA Hoan hao (Perfect Game)!")
            continue

        except ValueError:
            print(f"Tuyen thu {name}: Loi du lieu khong hop le!")
            continue

    print("--- HOAN TAT ---")


process_player_stats(player_stats)