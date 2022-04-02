dicionario = [
    {'Nome': 'Thiago', 'telefone': 31989190738},
    {'Nome': 'Ana Clara', 'Telefone': 35825882}
]

dicionario.each do |posicao|
    posicao.each do |chave, valor|
        nome = valor
        puts nome
    end
end
