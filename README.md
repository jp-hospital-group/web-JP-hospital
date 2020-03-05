# -web-JP-hospital


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