from xml.dom import minidom

dataTree  = minidom.parse("data.xml")
group = dataTree.documentElement

persons = group.getElementsByTagName("person")

for person in persons:
    print("=----------PERSON-----------=")
    if person.hasAttribute('id'):
        print(f'ID : {person.getAttribute('id')}')
    print(f'Name : {person.getElementsByTagName('name')[0].childNodes[0].data}')
    print(f'Age : {person.getElementsByTagName('age')[0].childNodes[0].data}')
    print(f'Weight : {person.getElementsByTagName('weight')[0].childNodes[0].data}')
    print(f'Height : {person.getElementsByTagName('height')[0].childNodes[0].data}')

newPerson = dataTree.createElement('person')
newPerson.setAttribute('id','6')

name = dataTree.createElement('name')
name.appendChild(dataTree.createTextNode('Johnson Ali'))

age = dataTree.createElement('age')
age.appendChild(dataTree.createTextNode('19'))

weight = dataTree.createElement('weight')
weight.appendChild(dataTree.createTextNode('66'))

height = dataTree.createElement('height')
height.appendChild(dataTree.createTextNode('6.5'))

newPerson.appendChild(name)
newPerson.appendChild(age)
newPerson.appendChild(height)
newPerson.appendChild(weight)

group.appendChild(newPerson)

dataTree.writexml(open('data.xml','w'))