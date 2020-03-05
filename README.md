# -web-JP-hospital


## プロジェクト起動方法
- Djangoインストール
```djangotemplate
pip install Django
```

- 起動
```djangotemplate
python manage.py runserver
```



## Django よく使えるコマンド

> プロジェクト作成
```djangotemplate
django-admin startproject <project name>
```

> アプリ作成
```djangotemplate
django-admin startapp <app name>
```

> 既存DB情報をModelに反映
```djangotemplate
python manage.py inspectdb > <app name>/models.py
```