from django.urls import path
from .views import *

urlpatterns = [
    path('regs',superreg.as_view(),name='regs'),
    path('suc',sucs,name='suc'),
    path('logs/',superlog.as_view(),name='logs'),
    path('add',addvehicle.as_view(),name='add'),
    path('sdis',superdisplay.as_view(),name='sdis'),
    path('supd/<pk>',editsuper.as_view(),name='supd'),
    path('supv/<pk>',superview.as_view(),name='supv'),
    path('sdel/<pk>',deletesuper.as_view(),name='sdel'),
    path('ind/',index),
    path('rega',adminreg.as_view(),name='rega'),
    path('loga',adminlog.as_view(),name='loga'),
    path('disa',admindisplay.as_view(),name='disa'),
    path('upda/<pk>',adminedit.as_view(),name='upda'),
    path('adv/<pk>',adminview.as_view(),name='adv'),
    path('usr',userreg.as_view(),name='usr'),
    path('usl',userlog.as_view(),name='usl'),
    path('usd',userdisplay.as_view(),name='usd'),
    path('sup',super,name='sup')
]