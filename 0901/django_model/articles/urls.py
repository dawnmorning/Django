from django.urls import path
from . import views  #articles 내에 있는 views import

app_name = 'articles'
urlpatterns = [
    path('lotto/',views.lotto, name = 'lotto'), # 해당 경로의 이름을 lotto라고 정의
    path('index/',views.index, name = 'index'),
    # Variable routing 사용시 주의점
    # 1. 변수 명과 views.py의 함수 인자의 이름이 같아야 한다.
    # 2. variable routing이 설정되면 반드시 매개변수로 받아야 한다.
    # 3. variable routing이 적용된 주소에는 반드시 값이 들어가 있어야 한다.
    path('hello/<name>/<int:age>/',views.hello, name = 'hello'), # Variable routing  # name에 변수를 담는다.
    path('new/', views.new, name='new'),
    path('create/',views.create, name='create'),
    # 글 조회를 위한 deatil
    path('detail/<post_id>/', views.detail, name = 'detail'),
    # 글 수정을 위한 edit
    path('edit/<post_id>', views.edit, name = 'edit'),
    path('update/<post_id>',views.update, name = 'update'),
    # 글 삭제를 위한 edit
    path('delete/<post_id>', views.delete, name = 'delete'),

]