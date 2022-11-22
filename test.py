from pymystem3 import Mystem
text = "красивый сын, красив и умен мой друг, красивому парню, красивого кота, красивые люди"
m = Mystem()
lemmas = m.analyze(text)
print(lemmas)