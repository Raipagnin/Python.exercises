#leia o nome de uma cidade e diga se ela comeca com o nome 'Santo'
#name = str(input('Em qual cidade vc nasceu?: ')).strip().title()
#city = name.split()
#print('Santo'in city[0])

#name = str(input('Em qual cidade vc nasceu: ')).strip()
#print(name[:5].title() == 'Santo')

cid = str(input('Em que cidade você nasceu? ')).lower().strip().split()
print('A sua cidade começa com santo? {}'.format('santo' in cid[0:5]))

# tanto na aula, como eu mesm nao pensei que ex: SANTORINI ia dar true, ou com hifen ex: SANTO-DAIME
