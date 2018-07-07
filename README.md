# Django Demo without DB

## Environment

### Download & Install Python
[Python 3.6.4](https://www.python.org/downloads/)

### Set Python Home
```
D:\Code\Tools\Python36\Scripts
```
### Install Django and plugins
```
pip install django
pip install pep8
pip install autopep8
pip install ptvsd
```

## Development Tools
### Download & Install Visual Studio Code(VSCode)
[Visual Studio Code](https://code.visualstudio.com/download)

### Install VSCode plugins (Ctrl + Shift + X)
Find the plugins and install
* python
* vscode-icons

### Edit VSCode Setting
- User Settings 
```js
"editor.tabSize": 2,
"editor.fontSize": 12
"workbench.iconTheme": "vscode-icons"
```
- Workspace Settings
```js
"python.pythonPath": "D:/Code/Tools/Python36/python.exe",
"python.linting.pep8Enabled": true,
"python.linting.pylintEnabled": false,
"editor.formatOnSave": true,
```

### Debug Settings (Ctrl+Shift+D)
* DEBUG -> Add Configuration -> python
* そのまま保存
* DEBUG -> Python:Django、歯車をクリックする
4. [args: --noreload]を削除する
5. F5(2回)で起動後、http://localhost:8000/は確認できる

## Project Settings
### Initial
```
django-admin startproject Django
cd Django
python ./manage.py startapp demo
```

### PEP Rules
`setup.cfg`
```
[pep8]
max-line-length = 160
ignore = E111,E114
indent-size = 2
```

### Template Path
`Django\settings.py`
```py
TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # ここから
            # html template path
            os.path.join(BASE_DIR, 'demo\\templates')
            # ここまで
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### URLs
```py
import sys
from django.http import HttpResponse

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 追加
    path('demo/hotel/', include('demo.urls'))
]
```

## Project
- `apps.py`
```py
from django.apps import AppConfig


class DemoConfig(AppConfig):
  name = 'demo'
```
- `urls`
```py
from django.conf.urls import url
from django.urls import path
from .hotel.list.view import ExListView
from .hotel.edit.view import ExEditView

urlpatterns = [
    path('', ExListView.as_view(template_name='list.html'), name='list'),
    path('create/', ExEditView.as_view(template_name='edit.html', mode='create'), name='create'),
    path('detail/<int:hotel_id>/', ExEditView.as_view(template_name='edit.html', mode='detail'), name='detail'),
    path('update/<int:hotel_id>/', ExEditView.as_view(template_name='edit.html', mode='update'), name='update'),
    path('delete/<int:hotel_id>/', ExEditView.as_view(template_name='edit.html', mode='delete'), name='delete')
]
```