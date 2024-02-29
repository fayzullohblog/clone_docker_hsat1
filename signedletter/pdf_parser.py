import qrcode
from reportlab.pdfgen.canvas import Canvas
from config.settings import MEDIA_ROOT

from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib import styles
import os

class PdfParser:

    def __init__(self, file, domain_name,user):
        self.file = os.path.join(MEDIA_ROOT,file)
        self.domain_name = domain_name
        self.reader = PdfReader(self.file)
        self.user=user


    def create_pdf(self, save_folder_path, page, **kwargs)->str:
        """
            Create pdf file with qrcode image
        """
        # Get the watermark file you just created
        SAVED_FILE_PATH = os.path.join(save_folder_path,f"{page}")
        new_folder_name = str(save_folder_path).split('/')[-1]
        SAVED_FILE_PATH_FOR_QRCODE = f"{self.domain_name}/media/{new_folder_name}/{page}"
        SAVED_FILE_PATH_FOR_MODEL = f"{new_folder_name}/{page}"
      
  
  


        writer = PdfWriter()
        
        with open(SAVED_FILE_PATH,'wb') as file:
            print('--------------->',SAVED_FILE_PATH)
            qr_code_image = self.create_qrcode_image(SAVED_FILE_PATH_FOR_QRCODE)
            watermark_file = self.create_qrcode_pdf(qr_code_image=qr_code_image, **kwargs)
            watermark = PdfReader(open(watermark_file, "rb"))
            
        
            self.reader.pages[0].merge_page(watermark.pages[0]) # merge qrcode pdf file to pdf file
            writer.add_page(self.reader.pages[0]) # add page to pdf file
            print('--------->',file)
            writer.write(file) # write pdf file

             
        with open(SAVED_FILE_PATH,'+rb') as file:
            d=file.read()
            print('-----------34',d)

        return SAVED_FILE_PATH_FOR_MODEL


    
    def create_qrcode_image(self, save_folder_path):
        qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=2,
            )
        qr_code.add_data(save_folder_path)
        qr_code.make(fit=True)
        qr_code_image = qr_code.make_image(fill_color="black", back_color="white")
        qr_code_image.save(os.path.join(MEDIA_ROOT , "data.png"))
        return os.path.join(MEDIA_ROOT , "data.png")


    def create_qrcode_pdf(self,  qr_code_image,  **kwargs):
        """
            Create pdf file with qrcode image
        """
        # if watermark_file doesn't exist, create it
        watermark_file = os.path.join(MEDIA_ROOT , self.file)


        if not os.path.exists(watermark_file):
            
            try:
                with open(watermark_file,'a') as file:
                    file.write('Yangi pdf fayl bush holatda yaratildi')
                    one_pdf=watermark_file.split('/')[-1]
                    return f'{one_pdf} fayli yaratildi ammo ishi bumbush: sababi esa, bazada bunday fayl mavjud emas'
            except IOError as e:
                return f'Xatolik yuz berdi: {e}'
       
        doc = Canvas(watermark_file)
        
        regular_font = "Times-Bold"
        font_size=12

        doc.setFont(regular_font,font_size)
        
        # draw the QR code at the specified coordinates
        doc.drawImage(qr_code_image, 270, 80)
     
        if kwargs:
            #data
            data_1 = self.user.full_name()
            data_2 = self.user.party_name


            
            #coordinates
            x_path_1 = kwargs.get('x_path_1', 0)
            y_path_1 = kwargs.get('y_path_1', 0)
            
            x_path_2 = kwargs.get('x_path_2', 0)
            y_path_2 = kwargs.get('y_path_2', 0)
            #draw data
        
            doc.drawString(x_path_1, y_path_1, data_1)
            doc.drawString(x_path_2, y_path_2, 'Boshqarma boshlig\'ining')
            doc.drawString(88, 115, data_2)

            regular_font_data3="Helvetica"
            font_size_data3=8
            
            # doc.setFont(regular_font_data3,font_size_data3)
            # data_3 = self.user.user_number_litter
            # doc.drawString(540, 728, data_3)
            
            #TODO: add more data to pdf file
        doc.save()
        return watermark_file