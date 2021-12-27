"""pandora_trading_solutions_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from quote.urls import router as quotes_router
from news.urls import router as news_router
from prediction.urls import router as prediction_router
from daily_analysis.urls import router as daily_analysis_router

from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/quotes/', include(quotes_router.urls)),
    path('api/news/', include(news_router.urls)),
    path('api/predictions/', include(prediction_router.urls)),
    path('api/daily-analysis/', include(daily_analysis_router.urls)),
]
