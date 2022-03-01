mochilajedi = ['algo', 'algo', 'algo', 'algo', 'algo', 'algo']
mochilajedi2 = ['algo', 'algo', 'algo', 'algo', 'algo', 'Sable']
mochilajedi3 = ['algo', 'Sable', 'algo', 'algo', 'algo', 'algo']
mochilajedi4 = ['Sable', 'algo', 'algo', 'algo', 'algo', 'algo']

def sable_mochila(mochilajedi):
    if len(mochilajedi) == 0 or mochilajedi[-1] == 'Sable':
        return len(mochilajedi)
    else:
        return sable_mochila(mochilajedi[:-1])

pos_sable = sable_mochila(mochilajedi3)

if pos_sable == 0:
    print('El sable no esta en la mochila')
else:
    print('El sable esta en la mochila, objetos sacados: ', len(mochilajedi) - pos_sable)