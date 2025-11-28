#megnyitási módok
#r: olvasás
#w: írás, fájlt hoz létre ha létezik ilyen nevű fájl már, felül írja az eredetit
#x: Írás fájlt hoz létre ha létezik ilyen nevű fájl már, hibát ad
#a: a létező fájl végére hozzáfűz, ha még nem létezik ilyen nevű, akkor létrehozza
#a+: hozzáfűzést és olvasást is lehtővé tesz

with open('kimenet.txt', 'w', encoding='utf-8') as adatfolyam: #lehet docx is a fájl kiterjesztése
    print('lorem ipsum', file=adatfolyam) #tényleges fájlba írás
    print('\nUt aliquam lectus vitae feugiat mollis. Aliquam vitae maximus neque. Curabitur commodo porta quam, non condimentum justo feugiat in. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nunc ornare at dolor nec hendrerit. Cras facilisis rutrum ex, quis ornare urna vestibulum ac. Integer dapibus tincidunt eros, eu congue sapien hendrerit eu. Sed nibh urna, pretium ac magna vel, tincidunt molestie nulla. Sed eget purus libero. Nullam ornare tellus nec malesuada ornare. Integer suscipit elit ac erat efficitur convallis id a nulla. Morbi sed dictum nulla.', file=adatfolyam)
    print('\nSuspendisse potenti. In in sem in mauris efficitur auctor non ac mi. In iaculis viverra imperdiet. Nam vitae arcu quis mi iaculis sodales non sit amet urna. Integer id metus id nibh rutrum mollis sit amet a est. Mauris vitae ante tincidunt, ullamcorper enim nec, interdum dolor. Nunc velit nisi, facilisis in ante et, malesuada porta enim. Nulla sit amet nibh rutrum, pretium libero tempor, egestas elit. Ut pretium ut magna eget sagittis. Interdum et malesuada fames ac ante ipsum primis in faucibus.', file=adatfolyam)
    print("A fájlba írás sikeresen megtörtént!")
