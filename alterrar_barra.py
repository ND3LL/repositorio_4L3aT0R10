#Criei uma variável 'path' para armazenar o caminho que vc deseja alterar a '/'
path = r'/home/nd3ll/Documentos/Faculdade/Faculdade de Direito/7_semestre'

# printa o path antigo
print(path)

# Altera o a '/' para '\'
path = path.replace(r'/', '\\')

# printa o path novo
print(path)
