# Import the PDFReader and DocumentParser objects
import PyPDF2
# Lendo um arquivo pdf, colocar o r para ele entender o caminho
arquivo = r"C:\Users\jasantos\JupyterProjects\CV_GAVB_Jaqueline Alves.pdf"
# Read file and get parser
lerPdf = PyPDF2.PdfFileReader(arquivo)
pagina = lerPdf.getPage(1)
conteudo = pagina.extractText()
print(conteudo)
