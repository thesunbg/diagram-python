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


with Diagram("D??y C??ng ngh???, k??? thu???t, k??? to??n", filename='office/day_ben_trai', show=False):
    with Cluster("Kh??ng gian gi???a"):
        Custom("Thang m??y", elevator_icon) - Blank("") - Blank("") - Blank("") - Blank("") - Blank("") - Custom('C???a ra v??o', door_icon)
    with Cluster("D??y ngo??i"):
        with Cluster("Ph??a trong"):
            Custom("Nguy???n ?????c Th???nh", male_icon) - Custom("Nguy???n Huy Ho??ng", male_icon) - Custom("B??n tr???ng", chair_icon) -\
            Custom("Nguy???n M???nh D??ng", male_icon) - Custom("B??i V??n H???", male_icon) - Custom("B??n tr???ng", chair_icon) - Blank("")
        with Cluster("Ph??a ngo??i"):
            Custom("B??n tr???ng", chair_icon) - Custom("B??n tr???ng", chair_icon) - Custom("?????ng V???n Ti???u", male_icon) - \
            Custom("Nguy???n Ti???n Vi???t", male_icon) - Custom("Ph???m Qu???c Chung", male_icon) - Custom("L?? Ch??? H???u H??", male_icon) - Blank("")
    with Cluster("D??y trong"):
        with Cluster("Lonely Zone"):
            ceo = [Custom("Nguy???n V??n ????", male_icon)]
        with Cluster("Ph??a ngo??i"):
            [ceo - Custom("Tr???nh Qu???c Ho??n ?????t", male_icon)] - Custom("Nguy???n Trung Ki??n", male_icon) - Custom("H?? V??n H??ng", male_icon) - \
            Custom("L????ng V??n Minh", male_icon) - Custom("Phan ????nh Kh??nh", male_icon) - Custom("????? V??n Thi??n", male_icon)
        with Cluster("Ph??a trong"):
            [ceo - Custom("Nguy???n Minh H???i", male_icon)] - Custom("V?? Tr???ng Ki??n", male_icon) - \
            Custom("Tr???n Qu???c Trung", male_icon) - Custom("Ki???u Th??? Hi???n", female_icon) - \
            Custom("V?? Th??? Thu Trang", female_icon) - Custom("Nguy???n Thu??? Linh", female_icon)
        
    

with Diagram("D??y Kinh doanh - Marketing - H??? tr??? k??? thu???t - Nghi???p v???", filename='office/day_ben_phai', show=False, direction="TB"):
    with Cluster("D??y ngo??i"):
        with Cluster("Ph??a trong"):
            Custom("Nguy???n V??n D??n", male_icon) - Custom("Nguy???n V??n Minh", male_icon) - Custom("Nguy???n B???o Linh", male_icon) -\
            Custom("Nguy???n ?????c Hu???nh", male_icon) - Custom("Ph???m ?????c Vi???t", male_icon) - \
            Custom("V?? Ki???u My", female_icon) - Custom("Nguy???n Thanh Huy???n", female_icon) - Custom("L???i Minh Quang", male_icon) -\
            Custom("Nguy???n Vi???t B???c", male_icon)
        with Cluster("Ph??a trong"):
            Custom("B??i ?????c Ho??", male_icon) - Custom("Nguy???n H???u Ph??c", male_icon) - Custom("B??n tr???ng", chair_icon) - \
            Custom("Ph???m Minh Ph????ng", female_icon) - Custom("Nguy???n Th???o Linh", female_icon) - \
            Custom("Nguy???n Th??? Thu H??", female_icon) - Custom("Nguy???n Th??? Thu??? Chi", female_icon) -\
            Custom("L?? Th??? H?? Thanh", female_icon) - Custom("V?? Thu Uy??n", female_icon)
    with Cluster("D??y trong"):
        with Cluster("C???a ra v??o"):
            cua_ra_vao = Blank("C???a ra v??o")
        with Cluster("T?????ng"):
            tuong = Blank("T?????ng")
        with Cluster("Khu sinh ho???t chung"):
            khu_sinh_hoat_chung = [Custom("Gi?????ng ng???", bed_icon), Custom("B??n u???ng n?????c", desk_circle_icon)]
        with Cluster("Ph??a ngo??i"):
            [khu_sinh_hoat_chung - Custom("Ph???m H???i Anh", female_icon)] - Custom("Nguy???n Anh D??ng", male_icon) -\
            Custom("L?? Th??? H???u", female_icon) - Custom("????? Th??? H???ng Ng???c", female_icon) - \
            Custom("H??? ?????c Tr??", male_icon) - Custom("Nguy???n Th??? Thanh Thu??", female_icon)
        with Cluster("Ph??a trong"):
            [khu_sinh_hoat_chung - Custom("Tr???n Xu??n H???u", male_icon)] - Custom("Ph???m Thu??? Ninh", female_icon) -\
            Custom("B??n tr???ng", chair_icon) - \
            Custom("Nguy???n An H???i", male_icon) - Custom("Nguy???n V??n Linh", male_icon) - Custom("Ho??ng V??n T??ng", male_icon)
        cua_ra_vao - tuong - khu_sinh_hoat_chung
    