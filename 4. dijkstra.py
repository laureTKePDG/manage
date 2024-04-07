def dijkstra(sommet, source='1'):
    assert all(sommet[u][v] >= 0 for u in sommet.keys() for v in sommet[u].keys())
    precedent = {x:None for x in sommet.keys()}
    dejaTraite = {x:False for x in sommet.keys()}
    distance =  {x:float('inf') for x in sommet.keys()}
    distance[source] = 0
    a_traiter = [(0, source)]
    while a_traiter:
        dist_noeud, noeud = a_traiter.pop()
        if not dejaTraite[noeud]:
            dejaTraite[noeud] = True
            for voisin in sommet[noeud].keys():
                dist_voisin = dist_noeud + sommet[noeud][voisin]
                if dist_voisin < distance[voisin]:
                    distance[voisin] = dist_voisin
                    precedent[voisin] = noeud
                    a_traiter.append((dist_voisin, voisin))
        a_traiter.sort(reverse=True)
    return distance, precedent

sommet={}
sommet['1']={'2':7,'3':1}
sommet['2']={'4':4,'6':1}
sommet['3']={'2':5,'5':2,'6':7}
sommet['4']={}
sommet['5']={'2':2,'4':5}
sommet['6']={'5':3}

distance, precedent = dijkstra(sommet)
print('Distances minimum :',distance)
print('Liste des précédents :', precedent)
