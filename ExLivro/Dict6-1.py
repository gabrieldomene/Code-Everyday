#6-1Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name , last_name , age , and city . Print each
#piece of information stored in your dictionary.

nome = input("Nome: ")
sobrenome = input("\nSobrenome: ")
idade = int(input("\nIdade: "))
cidade = input("\nCidade: ")

info_person = {"nome" : nome, "sobrenome" : sobrenome, "idade" : idade, "cidade" : cidade}
print(info_person)
