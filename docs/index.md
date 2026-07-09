

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2"><img src="images/Image0.jpg"
style="width:1.38681in;height:1.47153in"
alt="logo_IGN_pour_lettre" /></td>
<td style="font-size: 24px;text-align: center;"><p><strong>Plugin QGis Assistant odonyme</strong></p>
<p><strong>V1.4.2</strong></p></td>
</tr>
<tr>
<td style="font-size: 16px;text-align: center;">Développeur  : Gérôme PECHEUR (IGN)</td>
</tr>
</tbody>
</table>

## Sommaire


- [1. Prérequis](#prerequis)
- [2. Résumé](#resume)
- [3. Installation](#installation)
- [4. Présentation](#presentation)
- [5. Mode de sélection](#mode-de-selection)
  - [5.1 Sélection unique](#selection-unique)
  - [5.2 Sélection multiple](#selection-multiple)
  - [5.3 Affichage du sens de numérisation et des INSEE](#affichage-du-sens-de-numerisation-et-des-insee)
- [6. Modifications](#modifications)
- [7. Renommage](#renommage)
- [8. A propos de](#a-propos-de)
- [9. Annexes](#annexes)
  - [9.1 Installation d'openpyxl](#installation-dopenpyxl)  


  
<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="prerequis" style="color: white;margin:0;" >1. Prérequis</h2>
</div>

Version de QGIS 3 : 3.28 ou supérieure.  
Le plugin « PluginsManager » doit préalablement être installé : 
[PluginsManager-qgis-plugin sur GitHub](https://github.com/IGNF/maitre-qgis-plugin/releases/download/version_finale/PluginsManager.zip)

Ce plugin est utilisable sur la couche éditable Tronçon_de_route de la BDTopo. 

Le fonctionnement de certaines fonctionnalités nécessite l’installation de :
- [ShortestPath-qgis-plugin sur GitHub](https://github.com/IGNF/ShortestPath-qgis-plugin/releases/download/version_finale/IGN_ShortestPath.zip)  
- [DigitizingDirection-qgis-plugin sur GitHub](https://github.com/IGNF/DigitizingDirection-qgis-plugin/releases/download/version_finale/IGN_DigitizingDirection.zip)


Si le package « openpyxl » n’est pas installé sur le poste, le message d’erreur ci-dessous apparaît lors d’une transaction.  


<div  style="text-align: center;"> 
	<img  src="images/Image1.png" /> 
</div>

Voir la procédure en annexe à la fin de ce document.  

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="resume" style="color: white;margin:0;" >2. Résumé</h2>
</div>

Ce plugin est une aide à la saisie des odonymes portés par les tronçons de route de la BDTopo.
L’interface permet de :  
-	Saisir ou **modifier** les odonymes (Noms collaboratifs gauche et droite) d’un ou plusieurs tronçons.  
-	Saisir ou **modifier** les alias gauche et droite d’un ou plusieurs tronçons.  
-	**Visualiser** les Nom BAN (gauche et droite)  
-	De sélectionner tous les tronçons entre 2 tronçons sélectionnés.  
-	De sélectionner tous les tronçons de même odonyme d’une commune sélectionnée.  
-	**D’afficher** le sens de numérisation des tronçons de route BDTopo.  
  
  
<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="installation" style="color: white;margin:0;" >3. Installation</h2>
</div> 

Ouvrir QGIS.  
Allez dans **Extensions/Installer/Gérer les extensions**, cliquez sur **Installer depuis un ZIP**, sélectionner le fichier ZIP puis cliquez sur **Installer le plugin**.  

<div  style="text-align: center;"> 
	<img  src="images/Image2.png" /> 
</div> 
 
   
  
<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="presentation" style="color: white;margin:0;" >4. Présentation</h2>
</div> 
  
<div  style="text-align: center;"> 
	<img  src="images/Image3.png" /> 
</div>  

Le bouton ![Image4](images/Image4.png) permet d’afficher l’historique des versions et d’ouvrir la documentation du plugin.  
Le bouton ![Image5](images/Image5.png) affiche ou masque le sens de numérisation des tronçons de route.
(Nécessite l’installation du plugin "DigitizingDirection")  

Le bouton ![Image6](images/Image6.png) permet de sélectionner tous les tronçons de la commune compris entre 2 tronçons sélectionnés.
(Nécessite l’installation du plugin "ShortestPath")  

Le bouton ![Image7](images/Image7.png) permet de sélectionner tous les tronçons de la commune de même nom collaboratif (gauche OU droite).  
Le bouton ![Image8](images/Image8.png) permet de modifier la couleur des tronçons sélectionnés dans QGIS. Ça peut être utile suivant la symbologie appliquées pour les tronçons dans QGIS.  

Le bouton ![Image9](images/Image9.png) valide les modifications faites dans la couche du projet. Pour répercuter les modifications dans la BDUni il faut sauvegarder avec le plugin Espace Collaboratif IGN.  

La case à cocher ![Image10](images/Image10.png) permet de modifier ou non simultanément le côté droit et gauche du tronçon sélectionné.  

![Image11](images/Image11.png) le point d’exclamation signifie que les tronçons sélectionnés n’ont pas tous le même nom collaboratif (dérouler la liste pour contrôler)  

Le code insee de la commune limite les actions aux seuls tronçons de la commune indiquée (chemin le plus court, même nom …)  

<div  style="text-align: center;"> 
	<img  src="images/Image23.jpg" height = 300/> 
</div>

A l’ouverture de l’outil, il y a une vérification de la présence dans le projet des couches nécessaires.  
Afficher l’état du modèle permet de vérifier les permissions sur chaque attribut.  
Ces permissions sont définies dans le projet en fonction des guichets en saisie directe dans la BDTOPO.  
  


<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="selection-unique" style="color: white;margin:0;" >5. Mode de sélection</h2>
</div> 

<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="selection-unique" style="color: white;margin:0;" >5.1 Sélection unique</h2>
</div>


-	On ne sélectionne qu’un seul tronçon avec l’outil de sélection de QGIS  

<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="selection-multiple" style="color: white;margin:0;" >5.2 Sélection multiple</h2>
</div>

- Sélection multiple de tronçons portant le même nom collaboratif gauche OU droit, on sélectionne un tronçon, on clique sur le bouton ![Image7](images/Image7.png) le résultat est une sélection de tous les tronçons portant le même nom collaboratif gauche OU droit et inclus dans la commune dont le code insee est affiché dans l’interface.  
 
-	Sélection multiple avec l’outil de saisie. Dans QGIS on peut sélectionner manuellement un ensemble de tronçons  

-	Sélection multiple de tronçons contigües : on sélectionne 2 tronçons (le premier tronçon du début de rue et le dernier tronçon de la fin de rue), <mark>Ces 2 tronçons doivent être visibles à l’écran et être connectés</mark>. Ensuite on clique sur « trajet le plus court ». Le résultat est une sélection de tous les tronçons entre le premier et le deuxième sélectionnés respectant l’algorithme du chemin le plus court. Un contrôle visuel est toutefois nécessaire afin de vérifier si les tronçons sont bien ceux désirés. <mark>La sélection regroupe uniquement les tronçons contenus dans la commune choisie.</mark>  
 
<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="affichage-du-sens-de-numerisation-et-des-insee" style="color: white;margin:0;" >5.3 Affichage du sens de numérisation et des INSEE</h2>
</div>

-	Accessible via ![Image5](images/Image5.png)  
Ce bouton permet d’afficher sur les tronçons les sens de numérisations, les codes INSEE et les odonymes.  
Utile lorsque l’on travaille en limite de commune afin de savoir quel nom collaboratif correspond à celui de la commune choisie avant de le modifier.  
 
<div  style="text-align: center;"> 
	<img  src="images/Image12.png" /> 
</div>  

<div  style="text-align: center;"> 
	<img  src="images/Image13.jpg" /> 
</div>  
  


<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="modifications" style="color: white;margin:0;" >6. Modifications</h2>
</div>

Une fois la sélection faite, il suffit de renseigner un nouveau nom collaboratif gauche et/ou droit.
Le (ou les) nom collaboratif à modifier apparaît en bleu.  


<div  style="text-align: left;"> 
	<img  src="images/Image14.png" /> 
</div>

Si on désire modifier simultanément les 2 noms collaboratifs, il faut activer le « verrou » ![Image10](images/Image10.png)  sinon les 2 champs seront indépendants.  
**Ne pas les lier est utile en limite de commune.**  

Si les tronçons sélectionnés n’ont pas le même nom collaboratif (gauche ou droit) un panneau point d’exclamation le signale. Il faut dérouler la liste des noms et sélectionner celui choisi.  

<div  style="text-align: left;"> 
	<img  src="images/Image15.png" /> 
</div>



<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="renommage" style="color: white;margin:0;" >7. Renommage</h2>
</div>

Pour valider les modifications faites dans l’outil il faut cliquer sur ![Image16](images/Image16.png)  
Un message QGIS confirme la prise en compte des modifications.  

![Image17](images/Image17.png)  

![Image18](images/Image18.jpg)  

-	<mark>IMPORTANT</mark> : il faut impérativement être connecté à l’espace collaboratif via le plugin Espace collaboratif  

Avant l’utilisation du plugin ou juste après une validation, lorsque QGIS demande de vous connecter si ce n’est pas déjà fait. Sinon les modifications seront effectives dans QGIS ET non dans l’espace collaboratif.  

-	Ne pas oublier de renseigner l’INSEE de la commune à traiter.  
SI le cadre « INSEE de la commune à traiter » est vide, il suffit soit de sélectionner un premier tronçon pour le remplir, soit de le remplir manuellement.  
Une fois l’INSEE renseigné, on ne peut que le modifier manuellement.  

-	Si on essaye de modifier un nom collaboratif droite ou gauche d’un tronçon en dehors de la commune choisie, la modification et la contribution directe ne se feront pas.  
On aura alors ce message :  ![Image19](images/Image19.png) 


<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="a-propos-de" style="color: white;margin:0;" >8. A propos de</h2>
</div>

Accessible via ![Image4](images/Image4.png).  

<div  style="text-align: center;"> 
	<img  src="images/Image20.png" /> 
</div>  

Cette boîte permet de suivre l’évolution des différentes versions ainsi que d’afficher cette documentation.  


<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="annexes" style="color: white;margin:0;" >9. Annexes</h2>
</div>

<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="installation-dopenpyxl" style="color: white;margin:0;" >9.1 Installation d'openpyxl</h2>
</div>


Ouvrir l’invite de commande, se placer dans le répertoire « bin » de l’installation de QGIS :  
Exemple :  

![Image21](images/Image21.png)  

Puis taper la commande : python-qgis-ltr.bat -m pip install openpyxl  

![Image22](images/Image22.png)  

Le package s’installe, vous n’avez plus qu’à relancer QGIS.  