#   Nom ......... : fredOnGithub
#   Role ........ : MAKE-SFZ-FILES-FOR-WAVS-SEQUENCE-SYNTH-LIBRARY
#   Auteur ...... : fredOnGithub
#   Version ..... : V2 du 26/8/2021
#   Licence ..... : GPL-3.0 License
#   Compilation :___

import os

def rec_les_rep(r, l):
    if os.path.isdir(r):
        os.chdir(r""+r)
        l.append(os.getcwd())
        for i in os.listdir(os.getcwd()):
            rec_les_rep(i, l)
        os.chdir(r"..")


def lister_liste(l):
    n = 1
    for i in l:
        print(n, i)
        n += 1


def go(repDesWavs, repDesFSZ):
    A = """
    <control>
    <global>
    <group> 
    """
    l = []
    rec_les_rep(repDesWavs, l)

    # liste des répertoires avec des wavs
    m = []
    for i in l:
        for k in os.listdir(i):
            if '.wav' in k:
                m.append(i)
                break

    # va dans rep du shell car si on donne un chemin diff de celui du script pour le rep d'analyse...
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # print(os.getcwd())

    # création du répertoire des fichiers FSZ
    if not os.path.exists(repDesFSZ):
        os.makedirs(repDesFSZ)
    else:
        print('Répertoire existe')

    # dans chaque rép où il y a des wavs créer un fichiers .fsz et le remplir
    n = 1
    for repI in m:
        s = repI.replace('\\', '/')
        nomRep = s.split('/')[-1]  # le dernier rép du chemin
        nomFich = repDesFSZ+'/'+nomRep+'.sfz'
        fichier = open(nomFich, "w")
        fichier.write(A)
        o = 1
        for repOuFich in os.listdir(repI):
            if '.wav' in repOuFich:
                s = repI+'/'+repOuFich
                s = "<region> sample="+s+" key="+str(o)
                s = s.replace('\\', '/')
                fichier.write(s+"\n")
                o += 1
        fichier.close()


go('<dir of wavs>', '<dir which will contain sfz files ')


# suppression de la limitation MAX_PATH https://docs.python.org/fr/3/using/windows.html

# voir https://www.youtube.com/watch?v=gmTmy6Byx6g
