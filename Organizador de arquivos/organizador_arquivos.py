import os

audios = ['.mp3', '.wav']
videos = ['.mp4', '.mov', '.avi']
imagens = ['.jpg', '.jpeg', '.png']
documentos = ['.txt', '.log', '.pdf']

def determinar_extensao(arquivo):
    ext = arquivo.rfinder('.')
    extensao = arquivo[ext:]

    return extensao
    

def organizador(diretorio):
    audios = os.path.join(diretorio, "audios")
    videos = os.path.join(diretorio, "videos")
    imagens = os.path.join(diretorio, "imagens")
    documentos = os.path.join(diretorio, "documentos")
    outros = os.path.join(diretorio, "outros")

    if not os.path.isdir(audios):
        os.mkdir(audios)
    if not os.path.isdir(videos):
        os.mkdir(videos)
    if not os.path.isdir(imagens):
        os.mkdir(imagens)
    if not os.path.isdir(documentos):
        os.mkdir(documentos)
    if not os.path.isdir(outros):
        os.mkdir(outros)

    arquivos = os.listdir(diretorio)
    novo_arquivo = ''

    for arquivo in arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):

            extensao = determinar_extensao(arquivo)
            if extensao in audios:
                novo_arquivo = audios
            elif extensao in videos:
                novo_arquivo = videos
            elif extensao in imagens:
                novo_arquivo = imagens
            elif extensao in documentos:
                novo_arquivo = documentos
            else:
                novo_arquivo = outros
            
            os.rename(os.path.join(diretorio, arquivo), os.path.join(novo_arquivo, arquivo))
        
if __name__ == "__main__":
    organizador('testes')
    