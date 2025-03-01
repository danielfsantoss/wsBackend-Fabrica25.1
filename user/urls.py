from django.urls import path 

patterns = [
  path('criar/', 'user.views.criar'),
  path('listar/', 'user.views.listar'),
  path('editar/', 'user.views.editar'),
  path('deletar/', 'user.views.deletar'),
]
