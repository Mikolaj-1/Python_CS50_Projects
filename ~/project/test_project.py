from project import adding_word

def test_adding_word():
    assert adding_word(["- - - - - ","- - - - - ","- - - - - ","- - - - - ","- - - - - ","- - - - - "],"woods","japan",0)==["W O O D S ","- - - - - ","- - - - - ","- - - - - ","- - - - - ","- - - - - "]
    assert adding_word(["W O O D S ","- - - - - ","- - - - - ","- - - - - ","- - - - - ","- - - - - "],"japan","liver",1)==["W O O D S ","J A P A N ","- - - - - ","- - - - - ","- - - - - ","- - - - - "]
    assert adding_word(["C O A S T ","W O O D S ","J A P A N ","- - - - - ","- - - - - ","- - - - - "],"funds","liver",3)==["C O A S T ","W O O D S ","J A P A N ","F U N D S ","- - - - - ","- - - - - "]


