import qrcode
import base64
import io


class QrcodeGenerator():


    def get_qr_code(linked_link):
        bio = io.BytesIO()
        data = f'http://127.0.0.1:8000/{linked_link}'
        qr = qrcode.make(data)
        qr.save(bio, 'png')
        img_str = base64.b64encode(bio.getvalue())
        return img_str.decode()