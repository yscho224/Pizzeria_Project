from django.urls import path, include
from . import views

app_name = 'user'
'''
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name= 'register'),
]