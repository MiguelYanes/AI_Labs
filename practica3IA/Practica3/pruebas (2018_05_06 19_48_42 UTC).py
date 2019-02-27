from connect4game import *

conecta4 = Connect4Game(5,5)
print conecta4.__str__()
conecta4.result_state(3)
print conecta4.__str__()

conecta4.result_state(0)
conecta4.result_state(1)
conecta4.result_state(2)
conecta4.result_state(0)

print conecta4.__str__()


conecta4.result_state(0)
conecta4.result_state(2)
conecta4.result_state(0)
conecta4.result_state(1)
conecta4.result_state(0)
print conecta4.__str__()

print "***sucesores***"
for sucesor in conecta4.successors():
    print "Accion: " + str(sucesor[0])
    print sucesor[1].__str__()
