import tools
from tools import Person
def main()->None:
    print(tools.PI)
    print(tools.NAME)
    print(tools.get_weather())
    p1=tools.get_person("剋來噁",16,100)
    print(p1.name)
    print(p1.age)
    print(p1.score)
    p2=tools.get_person("claire",16,100)
    print(p2.name)
    print(p2.age)
    print(p2.score)
   
if __name__=="__main__":
    main()