from diagrams import Diagram, Cluster
from diagrams.generic.blank import Blank
from diagrams.custom import Custom
from urllib.request import urlretrieve
import os

module = 'office'
project_dir = os.path.dirname(os.path.abspath(__file__))
print(project_dir)

male_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSC4D8kOabwe8e6c1xJEOjn_006gXxXJD9Ung&usqp=CAU'
male_icon = 'man.icon'
if not os.path.exists(project_dir + '/man.icon'):
    print('download man.icon')
    urlretrieve(male_url, male_icon)

female_url = 'https://p.kindpng.com/picc/s/164-1648741_mom-icon-png-customer-icon-transparent-png-png.png'
female_icon = 'woman.icon'
if not os.path.exists(project_dir + '/woman.icon'):
    print('download woman.icon')
    urlretrieve(female_url, female_icon)

chair_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ58fVIhfBq3JnYdd3wtg9giZiPhYNzGEMX1Q&usqp=CAU'
chair_icon = 'chair.icon'
if not os.path.exists(project_dir + '/chair.icon'):
    print('download chair.icon')
    urlretrieve(chair_url, chair_icon)

elevator_url = 'https://st2.depositphotos.com/6025596/9459/v/950/depositphotos_94590862-stock-illustration-elevator-icon-lift-symbol.jpg'
elevator_icon = 'elevator.icon'
if not os.path.exists(project_dir + '/elevator.icon'):
    print('download elevator.icon')
    urlretrieve(elevator_url, elevator_icon)

door_url = 'https://cdn-icons-png.flaticon.com/512/59/59801.png'
door_icon = 'door.icon'
if not os.path.exists(project_dir + '/door.icon'):
    print('download door.icon')
    urlretrieve(door_url, door_icon)

desk_circle_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRP6WIocmgH-MEpzEQPYYkVV9pXKLbhTKCxog&usqp=CAU'
desk_circle_icon = 'desk-circle.icon'
if not os.path.exists(project_dir + '/desk-circle.icon'):
    print('download desk-circle.icon')
    urlretrieve(desk_circle_url, desk_circle_icon)

bed_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjuT0CU-25imSzGacX-954Q7fptJGnNjx0kQ&usqp=CAU'
bed_icon = 'bed.icon'
if not os.path.exists(project_dir + '/bed.icon'):
    print('download bed.icon')
    urlretrieve(bed_url, bed_icon)


with Diagram("Dãy Công nghệ, kỹ thuật, kế toán", filename='office/day_ben_trai', show=False):
    with Cluster("Không gian giữa"):
        Custom("Thang máy", elevator_icon) - Blank("") - Blank("") - Blank("") - Blank("") - Blank("") - Custom('Cửa ra vào', door_icon)
    with Cluster("Dãy ngoài"):
        with Cluster("Phía trong"):
            Custom("Nguyễn Đức Thịnh", male_icon) - Custom("Nguyễn Huy Hoàng", male_icon) - Custom("Bàn trống", chair_icon) -\
            Custom("Nguyễn Mạnh Dũng", male_icon) - Custom("Bùi Văn Hổ", male_icon) - Custom("Bàn trống", chair_icon) - Blank("")
        with Cluster("Phía ngoài"):
            Custom("Bàn trống", chair_icon) - Custom("Bàn trống", chair_icon) - Custom("Đặng Vặn Tiễu", male_icon) - \
            Custom("Nguyễn Tiến Việt", male_icon) - Custom("Phạm Quốc Chung", male_icon) - Custom("Lê Chử Hữu Hà", male_icon) - Blank("")
    with Cluster("Dãy trong"):
        with Cluster("CEO"):
            ceo = [Custom("Nguyễn Văn Đô", male_icon)]
        with Cluster("Phía ngoài"):
            [ceo - Custom("Trịnh Quốc Hoàn Đạt", male_icon)] - Custom("Nguyễn Trung Kiên", male_icon) - Custom("Hà Văn Hùng", male_icon) - \
            Custom("Lương Văn Minh", male_icon) - Custom("Phan Đình Khánh", male_icon) - Custom("Đỗ Văn Thiên", male_icon)
        with Cluster("Phía trong"):
            [ceo - Custom("Nguyễn Minh Hải", male_icon)] - Custom("Vũ Trọng Kiên", male_icon) - \
            Custom("Trần Quốc Trung", male_icon) - Custom("Kiều Thị Hiền", female_icon) - \
            Custom("Vũ Thị Thu Trang", female_icon) - Custom("Nguyễn Thuỳ Linh", female_icon)
        
    

with Diagram("Dãy Kinh doanh - Marketing - Hỗ trợ kỹ thuật - Nghiệp vụ", filename='office/day_ben_phai', show=False, direction="TB"):
    with Cluster("Dãy ngoài"):
        with Cluster("Phía trong"):
            Custom("Nguyễn Văn Dân", male_icon) - Custom("Bàn trống", chair_icon) - Custom("Nguyễn Văn Minh", male_icon) -\
            Custom("Nguyễn Bảo Linh", male_icon) - Custom("Nguyễn Đức Huỳnh", male_icon) - Custom("Phạm Đức Việt", male_icon) - \
            Custom("Võ Kiều My", female_icon) - Custom("Nguyễn Thanh Huyền", female_icon) - Custom("Nguyễn Việt Bắc", male_icon)
        with Cluster("Phía trong"):
            Custom("Bùi Đức Hoà", male_icon) - Custom("Nguyễn Hữu Phúc", male_icon) - Custom("Bàn trống", chair_icon) - \
            Custom("Phạm Minh Phương", female_icon) - Custom("Nguyễn Thảo Linh", female_icon) - \
            Custom("Nguyễn Thị Thu Hà", female_icon) - Custom("Nguyễn Thị Thuỳ Chi", female_icon) -\
            Custom("Lê Thị Hà Thanh", female_icon) - Custom("Vũ Thu Uyên", female_icon)
    with Cluster("Dãy trong"):
        with Cluster("Cửa ra vào"):
            cua_ra_vao = Blank("Cửa ra vào")
        with Cluster("Tường"):
            tuong = Blank("Tường")
        with Cluster("Khu sinh hoạt chung"):
            khu_sinh_hoat_chung = [Custom("Giường ngủ", bed_icon), Custom("Bàn uống nước", desk_circle_icon)]
        with Cluster("Phía ngoài"):
            [khu_sinh_hoat_chung - Custom("Phạm Hải Anh", female_icon)] - Custom("Nguyễn Anh Dũng", male_icon) -\
            Custom("Lê Thị Hậu", female_icon) - Custom("Đỗ Thị Hồng Ngọc", female_icon) - \
            Custom("Hồ Đức Trí", male_icon) - Custom("Nguyễn Thị Thanh Thuý", female_icon)
        with Cluster("Phía trong"):
            [khu_sinh_hoat_chung - Custom("Trần Xuân Hậu", male_icon)] - Custom("Phạm Thuỳ Ninh", female_icon) -\
            Custom("Bàn trống", chair_icon) - \
            Custom("Nguyễn An Hải", male_icon) - Custom("Nguyễn Văn Linh", male_icon) - Custom("Hoàng Văn Tùng", male_icon)
        cua_ra_vao - tuong - khu_sinh_hoat_chung
    