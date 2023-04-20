LECTEUR MUSIQUE:


Ce lecteur de musique qui utilise la bibliothèque Pygame pour jouer des fichiers audio au format MP3. 
Il utilise également la bibliothèque Tkinter pour créer une interface graphique permettant à l'utilisateur de sélectionner et de jouer des chansons.

Le script initialise Pygame Mixer et crée une fenêtre Tkinter. Il contient plusieurs fonctions pour ajouter des chansons à une liste, supprimer des chansons de la liste, 
lire des chansons, arrêter la lecture de chansons, passer à la chanson suivante et mettre en pause la lecture de chansons.

La fonction play_time est utilisée pour afficher la durée de lecture de la chanson en cours et pour mettre à jour la barre de progression en conséquence. 
La fonction add_song est utilisée pour ajouter une chanson unique à la liste de lecture, tandis que la fonction add_many_songs est utilisée pour ajouter plusieurs 
chansons à la liste de lecture en une seule fois. La fonction delete_song est utilisée pour supprimer une chanson de la liste de lecture, tandis que la fonction 
delete_all_songs est utilisée pour supprimer toutes les chansons de la liste de lecture.

Le script utilise également la bibliothèque PIL pour afficher des images d'album associées aux chansons dans la liste de lecture.
