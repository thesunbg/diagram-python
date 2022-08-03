from diagrams import Diagram, Cluster
from diagrams.generic.blank import Blank
from diagrams.custom import Custom
from urllib.request import urlretrieve
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

man_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSC4D8kOabwe8e6c1xJEOjn_006gXxXJD9Ung&usqp=CAU'
man_icon = 'man.icon'
if not os.path.exists(project_dir + '/man.icon'):
    print('download man.icon')
    urlretrieve(man_url, man_icon)

woman_url = 'https://p.kindpng.com/picc/s/164-1648741_mom-icon-png-customer-icon-transparent-png-png.png'
woman_icon = 'woman.icon'
if not os.path.exists(project_dir + '/woman.icon'):
    print('download woman.icon')
    urlretrieve(woman_url, woman_icon)

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


with Diagram("Dãy Công nghệ, kỹ thuật, kế toán", show=False):
    with Cluster("Không gian giữa"):
        Custom("Thang máy", elevator_icon) - Blank("") - Blank("") - Blank("") - Blank("") - Blank("") - Custom('Cửa ra vào', door_icon)
    with Cluster("Dãy ngoài"):
        with Cluster("Phía trong"):
            Custom("Nguyễn Đức Thịnh", man_icon) - Custom("Nguyễn Huy Hoàng", man_icon) - Custom("Bàn trống", chair_icon) -\
            Custom("Nguyễn Mạnh Dũng", man_icon) - Custom("Bùi Văn Hổ", man_icon) - Custom("Bàn trống", chair_icon) - Blank("")
        with Cluster("Phía ngoài"):
            Custom("Bàn trống", chair_icon) - Custom("Bàn trống", chair_icon) - Custom("Đặng Vặn Tiễu", man_icon) - \
            Custom("Nguyễn Tiến Việt", man_icon) - Custom("Trần Quốc Trung", man_icon) - Custom("Lê Chử Hữu Hà", man_icon) - Blank("")
    with Cluster("Dãy trong"):
        with Cluster("CEO"):
            ceo = [Custom("Nguyễn Văn Đô", man_icon)]
        with Cluster("Phía ngoài"):
            [ceo - Custom("Trịnh Quốc Hoàn Đạt", man_icon)] - Custom("Nguyễn Trung Kiên", man_icon) - Custom("Hà Văn Hùng", man_icon) - \
            Custom("Lương Văn Minh", man_icon) - Custom("Phan Đình Khánh", man_icon) - Custom("Đỗ Văn Thiên", man_icon)
        with Cluster("Phía trong"):
            [ceo - Custom("Nguyễn Minh Hải", man_icon)] - Custom("Vũ Trọng Kiên", man_icon) - \
            Custom("Trung", man_icon) - Custom("Kiều Thị Hiền", woman_icon) - \
            Custom("Vũ Thị Thu Trang", woman_icon) - Custom("Nguyễn Thuỳ Linh", woman_icon)
        
    

with Diagram("Dãy Kinh doanh - Marketing - Hỗ trợ kỹ thuật - Nghiệp vụ", show=False, direction="TB"):
    with Cluster("Dãy ngoài"):
        with Cluster("Phía trong"):
            Custom("Nguyễn Văn Dân", man_icon) - Custom("Hồ Đức Trí", man_icon) - Custom("Nguyễn Văn Minh", man_icon) -\
            Custom("Nguyễn Bảo Linh", man_icon) - Custom("Nguyễn Đức Huỳnh", man_icon) - Custom("Phạm Đức Việt", man_icon) - \
            Custom("Võ Kiều My", man_icon) - Custom("Nguyễn Thanh Huyền", man_icon) - Custom("Nguyễn Việt Bắc", man_icon)
        with Cluster("Phía trong"):
            Custom("Bùi Đức Hoà", man_icon) - Custom("Nguyễn Hữu Phúc", man_icon) - Custom("Bàn trống", chair_icon) - \
            Custom("Phạm Minh Phương", woman_icon) - Custom("Nguyễn Thảo Linh", woman_icon) - \
            Custom("Nguyễn Thị Thu Hà", woman_icon) - Custom("Nguyễn Thị Thuỳ Chi", woman_icon) -\
            Custom("Lê Thị Hà Thanh", woman_icon) - Custom("Vũ Thu Uyên", woman_icon)
    with Cluster("Dãy trong"):
        with Cluster("Cửa ra vào"):
            cua_ra_vao = Blank("Cửa ra vào")
        with Cluster("Tường"):
            tuong = Blank("Tường")
        with Cluster("Khu sinh hoạt chung"):
            khu_sinh_hoat_chung = [Custom("Giường ngủ", bed_icon), Custom("Bàn uống nước", desk_circle_icon)]
        with Cluster("Phía ngoài"):
            [khu_sinh_hoat_chung - Custom("Phạm Hải Anh", woman_icon)] - Custom("Nguyễn Anh Dũng", man_icon) -\
            Custom("Nguyễn Thị Thanh Thúy", woman_icon) - Custom("Đỗ Thị Hồng Ngọc", woman_icon) - \
            Custom("Lê Thị Hậu", woman_icon)
        with Cluster("Phía trong"):
            [khu_sinh_hoat_chung - Custom("Trần Xuân Hậu", man_icon)] - Custom("Phạm Thuỳ Ninh", woman_icon) -\
            Custom("Nguyễn An Hải", man_icon) - Custom("Nguyễn Văn Linh", man_icon) - Custom("Hoàng Văn Tùng", man_icon)
        cua_ra_vao - tuong - khu_sinh_hoat_chung
    