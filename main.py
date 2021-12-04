from Cryptanalysis.Code.RSA import *
from Cryptanalysis.Code.RSA.index import wieners_attack

c =  26522332218267598672866890575210142205768811537701140032533741140906840971729228154813138779491487089810076826520540714226799708972013457479414733173382324358102873592826205539157063195844082978520476877927990736566726943328581774765673936639256108920636415375661553841642636318310300685075719828958017487612
n =  125653036681670227747402474722104225091005332168299519410697303864992490097595655106016770983361947355838710309768619288386503670366196312119273952477893844348887249777575681477347809060455675101598512768460495894299148896254894829422878200620127794937040063343630398543874916061758462918422428181361729695211
e =  95672467925223070396804606384683473946643362912524925135325014310437237833132782852285531410802465371566468475173628675259571435239226634950512996149456058355932330647215969027620271430498556422306251076265427277841030991768958069178723844651305348968530436108623692433113504156681228213533835239608618219873

d = wieners_attack(e,n)
print(d)