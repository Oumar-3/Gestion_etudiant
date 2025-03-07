from	django.urls	import	path	
from	.views	import	*


urlpatterns	=	[	
    	
    path('',	index,	name='index'),	
    path('blog',	blog,	name='blog'),
    path('etudiants/', liste_etudiants, name='etudiants'),
    path('etudiants/ajouter/', ajouter_etudiant, name='ajouter_etudiant'),
    path('etudiants/modifier/<int:id>/', modifier_etudiant, name='modifier_etudiant'),
    path('etudiants/supprimer/<int:id>/', supprimer_etudiant, name='supprimer_etudiant'),
    
]	