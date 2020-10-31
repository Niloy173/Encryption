import PyPDF2,os

path = "C:\\Python\\Python38\\Pdf and Word\\New folder" # set your path

pdfWriter = PyPDF2.PdfFileWriter()

try:

    def encrypt(root,password):
        for folder,subfolder,filename in os.walk(root):

            for file in filename:

                if file.endswith('.pdf'):

                    file_path = os.path.join(os.path.abspath(folder),file)

                    pdfobj = open(file_path,'rb')

                    pdfReader = PyPDF2.PdfFileReader(pdfobj)

                    if pdfReader.isEncrypted is False:

                        for page in range(pdfReader.numPages):

                            pdfWriter.addPage(pdfReader.getPage(page))

                        pdfWriter.encrypt(password)

                        newpath = file_path[:-4] + '_encrypt.pdf'

                        result_pdf = open(newpath,'wb')

                        pdfWriter.write(result_pdf)

                        result_pdf.close()

except Exception as e:
    print(e)



if __name__ == '__main__':

    p = input("enter a password : ")

    encrypt(path,p)
                        

