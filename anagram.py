l=['opp', 'poo', 'aba','opo']
# nl=[]

# for word in l:
#     m=''.join(sorted(word))
#     if m not in nl:
#         nl.append(m)
# nl.sort()        
# print(nl)

ns=set()
for word in l:
    m=''.join(sorted(word))
    ns.add(m)
print(sorted(ns))        
