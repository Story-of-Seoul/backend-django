
DATABASES = {
    'default': {
        
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'storyofseoul_db',
        # 'USER': 'root',
        # 'PASSWORD': 'dudqls1659',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        
        'USER': 'yongcloud',
        'NAME': 'storyofseoul_db',
        'PASSWORD': 'tjdnfdmldldirl',
        'HOST': '15.164.163.30',
        'PORT': '3306',
        
    }
}

EMAIL={
    'EMAIL_BACKEND' : 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_USE_TLS' : 'True',
    'EMAIL_PORT' : 587,
    'EMAIL_HOST' : 'smallbean99s@gmail.com',
    'EMAIL_HOST_PASSWORD' : '1659dudqls',
    'REDIRECT_PAGE' : 'http://127.0.0.1:8000/account/signin/'
}