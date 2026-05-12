import os
import fitz  # PyMuPDF

def combinar_pdfs_pasta(pasta_entrada, pasta_saida):
    
    # Cria a pasta de saída caso ela não exista
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Percorre todas as pastas dentro da pasta principal
    for pasta in os.listdir(pasta_entrada):

        pasta_caminho = os.path.join(pasta_entrada, pasta)

        # Verifica se é realmente uma pasta
        if os.path.isdir(pasta_caminho):

            print(f"\n📂 Processando pasta: {pasta}")

            # Cria um novo PDF vazio
            pdf_combinado = fitz.open()

            arquivos_processados = 0

            # Ordena os arquivos para manter sequência correta
            arquivos_pdf = sorted(os.listdir(pasta_caminho))

            # Percorre todos os arquivos da pasta
            for arquivo in arquivos_pdf:

                arquivo_caminho = os.path.join(pasta_caminho, arquivo)

                # Verifica se o arquivo é PDF
                if arquivo.lower().endswith('.pdf'):

                    try:
                        print(f"   ➜ Adicionando: {arquivo}")

                        # Abre PDF atual
                        pdf_atual = fitz.open(arquivo_caminho)

                        # Adiciona páginas ao PDF combinado
                        pdf_combinado.insert_pdf(pdf_atual)

                        # Fecha o PDF atual
                        pdf_atual.close()

                        arquivos_processados += 1

                    except Exception as erro:
                        print(f"   ❌ Erro ao processar {arquivo}: {erro}")

            # Salva apenas se houver PDFs processados
            if arquivos_processados > 0:

                caminho_saida = os.path.join(
                    pasta_saida,
                    f"{pasta}_COMBINADO.pdf"
                )

                # Salva PDF final
                pdf_combinado.save(caminho_saida)
                pdf_combinado.close()

                print(f"✅ PDF combinado salvo em:")
                print(f"   {caminho_saida}")

            else:
                print("⚠ Nenhum PDF encontrado nesta pasta.")

    print("\n🚀 Combinação concluída com sucesso!")


if __name__ == "__main__":

    # Pasta contendo subpastas com PDFs
    pasta_entrada = r"C:\PASTAS"

    # Pasta onde os PDFs combinados serão salvos
    pasta_saida = r"C:\PASTAS COMBINADAS"

    combinar_pdfs_pasta(pasta_entrada, pasta_saida)
